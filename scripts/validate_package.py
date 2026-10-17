#!/usr/bin/env python3
"""Check the distributable skill package, optionally against pinned upstream."""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
PIN = "49dd158d1076134a641b33efb035946536778336"
UPSTREAM_VERSION = "1.3.1"
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")


def ensure(ok, message):
    if not ok:
        raise ValueError(message)


def inspect(upstream=None):
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    ensure(manifest.get("$schema") == SCHEMA, "wrong plugin schema")
    ensure(manifest.get("name") == "matt-skills-for-chatgpt", "wrong package name")
    ensure(manifest.get("version") == "0.1.0", "wrong package version")
    ensure(manifest.get("license") == "MIT", "wrong license metadata")
    ui = manifest["extensions"]["com.openai"]["interface"]
    ensure("Unofficial" in manifest.get("description", ""), "missing unofficial attribution")
    ensure(len(ui["shortDescription"]) <= 30, "shortDescription over 30 characters")
    ensure(ui.get("developerName") == "lirtual", "wrong developer")
    ensure(isinstance(ui.get("capabilities"), list), "invalid capabilities")
    ensure((ROOT / "LICENSE").is_file(), "missing LICENSE")
    upstream_note = (ROOT / "UPSTREAM.md").read_text(encoding="utf-8")
    ensure(PIN in upstream_note and UPSTREAM_VERSION in upstream_note, "upstream provenance missing")

    skill_dirs = sorted(d for d in (ROOT / "skills").iterdir() if d.is_dir())
    ensure(len(skill_dirs) == 27, f"expected 27 skills, found {len(skill_dirs)}")
    explicit = 0
    support_count = 0
    for d in skill_dirs:
        skill = d / "SKILL.md"
        agent = d / "agents/openai.yaml"
        ensure(skill.is_file() and agent.is_file(), f"missing Skill or policy: {d.name}")
        content = skill.read_text(encoding="utf-8")
        ensure(content.startswith("---\n"), f"missing frontmatter: {d.name}")
        parts = content.split("---", 2)
        ensure(len(parts) >= 3, f"invalid frontmatter delimiters: {d.name}")
        header = yaml.safe_load(parts[1])
        ensure(isinstance(header, dict), f"invalid Skill YAML: {d.name}")
        ensure(header.get("name") == d.name, f"wrong Skill name: {d.name}")
        ensure(isinstance(header.get("description"), str) and header["description"].strip(),
               f"missing Skill description: {d.name}")
        policy = yaml.safe_load(agent.read_text(encoding="utf-8"))
        ensure(isinstance(policy, dict) and isinstance(policy.get("interface"), dict),
               f"invalid openai.yaml: {d.name}")
        actual = policy.get("policy", {}).get("allow_implicit_invocation", True)
        ensure(isinstance(actual, bool), f"invalid invocation policy: {d.name}")
        is_user = header.get("disable-model-invocation", False) is True
        ensure(actual != is_user, f"policy mismatch: {d.name}")
        explicit += is_user

        for md in d.rglob("*.md"):
            for raw in LINK.findall(md.read_text(encoding="utf-8")):
                ref = raw.split("#", 1)[0].split("?", 1)[0].strip("<>")
                if not ref or re.match(r"^[a-z]+:", ref, re.I) or ref.startswith("/"):
                    continue
                # Upstream templates use illustrative links, not bundled resources.
                if ref == "link" or (md.name == "GLOSSARY-FORMAT.md" and ref.startswith("./src/")):
                    continue
                target = (md.parent / unquote(ref)).resolve()
                ensure(target.is_relative_to(ROOT) and target.exists(),
                       f"broken relative link: {md.relative_to(ROOT)} -> {raw}")
        support_count += sum(p.is_file() and p.name not in ("SKILL.md", "openai.yaml")
                             for p in d.rglob("*"))
    ensure(explicit == 16, f"expected 16 explicit Skills, got {explicit}")
    ensure(support_count == 25, f"expected 25 support files, got {support_count}")

    for p in [ROOT / "plugin.json", ROOT / "LICENSE", ROOT / "UPSTREAM.md",
              *(ROOT / "skills").rglob("*")]:
        ensure(not p.is_symlink(), f"symlink is not permitted: {p}")

    if upstream:
        upstream = Path(upstream).resolve()
        revision = subprocess.check_output(["git", "-C", str(upstream), "rev-parse", "HEAD"],
                                           text=True).strip()
        ensure(revision == PIN, f"upstream must be pinned: {revision}")
        source_manifest = json.loads((upstream / ".claude-plugin/plugin.json").read_text())
        ensure(source_manifest["version"] == UPSTREAM_VERSION, "upstream version changed")
        expected = {Path(s).name: upstream / s.removeprefix("./") for s in source_manifest["skills"]}
        ensure(set(expected) == {p.name for p in skill_dirs}, "skill names differ from upstream")
        modified = []
        for name, source in expected.items():
            src_paths = {p.relative_to(source) for p in source.rglob("*") if p.is_file()}
            dst = ROOT / "skills" / name
            dst_paths = {p.relative_to(dst) for p in dst.rglob("*") if p.is_file()}
            ensure(src_paths == dst_paths, f"support files differ: {name}")
            for rel in src_paths:
                if (source / rel).read_bytes() != (dst / rel).read_bytes():
                    modified.append(f"skills/{name}/{rel.as_posix()}")
        for filename in modified:
            ensure(f"`{filename}`" in upstream_note,
                   f"undocumented adaptation: {filename}")
        ensure((upstream / "LICENSE").read_bytes() == (ROOT / "LICENSE").read_bytes(),
               "source license differs")
        print(f"Compared pinned upstream: {len(expected)} skills, {len(modified)} documented edits")
    print(f"Validated 27 skills, 16 explicit / 11 implicit, {support_count} support files")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream", type=Path, help="checkout at pinned upstream commit")
    args = parser.parse_args()
    try:
        inspect(args.upstream)
    except (ValueError, KeyError, OSError, yaml.YAMLError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
