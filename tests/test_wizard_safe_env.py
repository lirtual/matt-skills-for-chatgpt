import os
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "skills/wizard/template.sh"
DUMMY_SECRET = "synthetic-fixture-secret-NOT-A-REAL-CREDENTIAL"

class WizardEnvSafety(unittest.TestCase):
    def run_fixture(self, env_path):
        template = TEMPLATE.read_text()
        library = template.split("run_wizard() {", 1)[0]
        script = library + "\nrun_wizard() { write_env DEMO_FAKE_SECRET \"" + DUMMY_SECRET + "\"; }\nrun_wizard\n"
        return subprocess.run(["bash", "-c", script], env={**os.environ, "ENV_FILE": str(env_path)}, text=True, capture_output=True)

    def test_wizard_never_prints_secret(self):
        with tempfile.TemporaryDirectory() as t:
            path = Path(t) / ".env"
            r = self.run_fixture(path)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(path.read_text().strip(), "DEMO_FAKE_SECRET='" + DUMMY_SECRET + "'")
            self.assertNotIn(DUMMY_SECRET, r.stdout + r.stderr)
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)

    def test_wizard_rejects_symlink_target_without_mutating_it(self):
        with tempfile.TemporaryDirectory() as t:
            destination = Path(t) / "unrelated.txt"
            destination.write_text("untouched\n")
            symlink = Path(t) / ".env"
            symlink.symlink_to(destination)
            r = self.run_fixture(symlink)
            self.assertNotEqual(r.returncode, 0)
            self.assertEqual(destination.read_text(), "untouched\n")

    def test_wizard_makes_existing_env_private(self):
        with tempfile.TemporaryDirectory() as t:
            path = Path(t) / ".env"
            path.write_text("PREEXISTING=1\n")
            os.chmod(path, 0o644)
            r = self.run_fixture(path)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)
            self.assertIn("PREEXISTING=1", path.read_text())
            self.assertNotIn(DUMMY_SECRET, r.stdout + r.stderr)

if __name__ == "__main__":
    unittest.main()
