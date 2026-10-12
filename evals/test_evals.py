"""Offline harness self-tests; these are not measurements of AI agent effectiveness."""
from pathlib import Path
from tempfile import TemporaryDirectory
import importlib.util
import unittest
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('skillman_eval_runner',ROOT/'run.py')
runner=importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

class EvaluationsHarnessTests(unittest.TestCase):
    def test_all_fixtures_present(self):
        self.assertEqual(set(p.name for p in (ROOT/'tasks').iterdir() if p.is_dir()),{
            'feature-preservation','api-integration','untrusted-input','performance-preservation'})
    def test_prepare_protects_existing_directory(self):
        with TemporaryDirectory() as t:
            p=Path(t)/'run';runner.prepare('feature-preservation',p)
            self.assertTrue((p/'workspace'/'calculator.py').exists())
            with self.assertRaises(FileExistsError):runner.prepare('feature-preservation',p)
    def test_unmodified_fixtures_are_detected_as_unsolved(self):
        for task in ['feature-preservation','api-integration','untrusted-input','performance-preservation']:
            with self.subTest(task=task),TemporaryDirectory() as t:
                p=Path(t)/task;runner.prepare(task,p)
                record=runner.score(task,p,'baseline','harness-smoke',10)
                self.assertEqual(record['status'],'failed',record['stderr'])
    def test_compare_reports_arm_separately(self):
        with TemporaryDirectory() as t:
            p=Path(t);(p/'a.json').write_text('{"task":"x","arm":"baseline","status":"failed"}')
            (p/'b.json').write_text('{"task":"x","arm":"codemaster","status":"passed"}')
            self.assertEqual(len(runner.compare([p/'a.json',p/'b.json'])),2)

if __name__=='__main__':unittest.main()
