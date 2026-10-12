import unittest,tempfile,pathlib
from config_reader import parse_value
class Tests(unittest.TestCase):
    def test_nested_literals(self):
        self.assertEqual(parse_value("{'ports': [80, 443], 'on': True, 'name': 'api'}"),{'ports':[80,443],'on':True,'name':'api'})
    def test_number_and_none(self):
        self.assertEqual(parse_value('42'),42)
        self.assertIsNone(parse_value('None'))
    def test_type_error(self):
        with self.assertRaises(TypeError):parse_value(2)
    def test_malformed(self):
        with self.assertRaises(ValueError):parse_value('1 +')
    def test_no_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=pathlib.Path(tmp)/'owned'
            attack="__import__('pathlib').Path(%r).write_text('executed')" % str(path)
            with self.assertRaises(ValueError):parse_value(attack)
            self.assertFalse(path.exists())
