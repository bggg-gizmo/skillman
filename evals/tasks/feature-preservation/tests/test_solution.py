import unittest
from calculator import Calculator,add,subtract,multiply,divide
class Tests(unittest.TestCase):
    def test_existing_operators(self):
        self.assertEqual(add(3,7),10)
        self.assertEqual(subtract(3,7),-4)
        self.assertEqual(multiply(3,7),21)
    def test_division(self):
        self.assertEqual(divide(9,3),3)
        self.assertEqual(divide(-7,2),-3.5)
    def test_zero(self):
        with self.assertRaises(ZeroDivisionError):divide(1,0)
    def test_integration(self):
        calc=Calculator()
        self.assertEqual(calc.evaluate('divide',9,3),3)
        self.assertEqual(calc.evaluate('add',3,4),7)
        self.assertEqual(calc.history,[('divide',9,3,3),('add',3,4,7)])
    def test_unsupported(self):
        with self.assertRaisesRegex(ValueError,'unsupported operation'):
            Calculator().evaluate('exponentiate',2,3)
