import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

class PermissionFixtureTests(unittest.TestCase):
    def test_readonly_directory_rejects_synthetic_unapproved_write(self):
        # OS-level negative test only; not evidence of ChatGPT connector authorization.
        with tempfile.TemporaryDirectory() as root:
            folder = Path(root) / "readonly"
            folder.mkdir()
            old_mode = stat.S_IMODE(folder.stat().st_mode)
            try:
                folder.chmod(0o500)
                target = folder / "unapproved.txt"
                cmd = [sys.executable, "-c", "import pathlib,sys;pathlib.Path(sys.argv[1]).write_text('synthetic')", str(target)]
                p = subprocess.run(cmd, capture_output=True, text=True, check=False)
                self.assertNotEqual(p.returncode, 0, "expected OS write protection")
                self.assertFalse(target.exists())
                self.assertTrue("PermissionError" in p.stderr or "Permission denied" in p.stderr)
            finally:
                folder.chmod(old_mode)

if __name__ == "__main__":
    unittest.main()
