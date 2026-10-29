import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALL = ROOT / 'scripts' / 'install.py'


class InstallTest(unittest.TestCase):
    def run_installer(self, target, *options):
        return subprocess.run([sys.executable, str(INSTALL), '--target', str(target), *options],
                              capture_output=True, text=True, encoding='utf-8')

    def test_dry_run_and_install_match_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'skills'
            result = self.run_installer(target, '--dry-run')
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(target.exists())
            result = self.run_installer(target)
            self.assertEqual(result.returncode, 0, result.stderr)
            source = ROOT / 'skills'
            for original in source.glob('*/SKILL.md'):
                self.assertEqual(original.read_bytes(), (target / original.parent.name / 'SKILL.md').read_bytes())

    def test_conflict_stops_before_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'skills'
            existing = target / 'professional-vietnamese' / 'SKILL.md'
            existing.parent.mkdir(parents=True)
            existing.write_text('keep me', encoding='utf-8')
            result = self.run_installer(target)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(existing.read_text(encoding='utf-8'), 'keep me')
            self.assertEqual([p.name for p in target.iterdir()], ['professional-vietnamese'])


if __name__ == '__main__':
    unittest.main()
