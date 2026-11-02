import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DistributionTests(unittest.TestCase):
    def test_package_validation_without_required_upstream_checkout(self):
        p = subprocess.run(
            [sys.executable, "scripts/validate_package.py"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn("27 skills", p.stdout)
        self.assertIn("16 explicit", p.stdout)

    def test_build_creates_valid_single_plugin_archive(self):
        with tempfile.TemporaryDirectory() as t:
            archive = Path(t) / "candidate.zip"
            p = subprocess.run(
                [sys.executable, "scripts/build_package.py", "--output", str(archive)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
            self.assertTrue(archive.is_file())
            with zipfile.ZipFile(archive) as z:
                files = z.namelist()
                self.assertEqual(len([p for p in files if p.endswith("/SKILL.md")]), 27)
                self.assertEqual(len([p for p in files if p.endswith("/agents/openai.yaml")]), 27)
                self.assertIn("plugin.json", files)
                self.assertIn("LICENSE", files)
                self.assertNotIn("tests/test_distribution.py", files)
                self.assertFalse(any("__pycache__" in p or p.startswith("../") for p in files))
                manifest = json.loads(z.read("plugin.json"))
                self.assertEqual(manifest["name"], "matt-skills-for-chatgpt")
                source = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
                self.assertEqual(manifest["version"], source["version"])
                ui = manifest["extensions"]["com.openai"]["interface"]
                for key in ("logo", "composerIcon"):
                    self.assertIn(ui[key].removeprefix("./"), files)

    def test_validator_rejects_symlinked_package_root_directories(self):
        # Public validation CLI must reject every symlink in the distribution,
        # including the skills/assets roots (not just their descendants).
        for linked_root in ("skills", "assets"):
            with self.subTest(root=linked_root), tempfile.TemporaryDirectory() as t:
                candidate = Path(t)
                for file in ("plugin.json", "LICENSE", "UPSTREAM.md"):
                    shutil.copy2(ROOT / file, candidate / file)
                shutil.copytree(ROOT / "scripts", candidate / "scripts")
                for directory in ("skills", "assets"):
                    target = f"{directory}-original" if directory == linked_root else directory
                    shutil.copytree(ROOT / directory, candidate / target)
                (candidate / linked_root).symlink_to(
                    f"{linked_root}-original", target_is_directory=True
                )

                p = subprocess.run(
                    [sys.executable, "scripts/validate_package.py"],
                    cwd=candidate, capture_output=True, text=True,
                )
                self.assertNotEqual(p.returncode, 0, f"accepted linked {linked_root}")
                self.assertIn("symlink", p.stdout + p.stderr)

if __name__ == "__main__":
    unittest.main()
