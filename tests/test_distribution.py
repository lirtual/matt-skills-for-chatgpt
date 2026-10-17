import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = ROOT.parent / "upstream"

class DistributionTests(unittest.TestCase):
    def test_package_matches_pinned_upstream(self):
        p = subprocess.run(
            [sys.executable, "scripts/validate_package.py", "--upstream", str(UPSTREAM)],
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
                self.assertEqual(manifest["version"], "0.1.0")

if __name__ == "__main__":
    unittest.main()
