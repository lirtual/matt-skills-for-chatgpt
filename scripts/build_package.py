#!/usr/bin/env python3
"""Build a small reproducible Skills-only Agent Plugin archive."""
import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from validate_package import ROOT, inspect


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    inspect()
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    output = (args.output or ROOT / f"dist/{manifest['name']}-{manifest['version']}.zip").resolve()
    files = [ROOT / "plugin.json", ROOT / "LICENSE", ROOT / "UPSTREAM.md"]
    files += sorted(p for p in (ROOT / "skills").rglob("*") if p.is_file())
    files += sorted(p for p in (ROOT / "assets").rglob("*") if p.is_file())
    output.parent.mkdir(parents=True, exist_ok=True)
    if output in files:
        raise ValueError("output would overwrite a plugin source file")
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for file in files:
            arcname = file.relative_to(ROOT).as_posix()
            info = ZipInfo(arcname, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, file.read_bytes())
    print(f"Built {output} with {len(files)} files")


if __name__ == "__main__":
    main()
