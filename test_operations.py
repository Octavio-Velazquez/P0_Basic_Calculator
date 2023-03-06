import unittest

from operations import addition
from operations import subtraction
from operations import multiplication
from operations import division

class OperationsTestCase(unittest.TestCase):
    """This class have all the methods that are doing the testing to the functions."""

    def test_add(self):
        """Funciona?"""
        result = addition(14, 6)
        self.assertEqual(result, 20)

        result = addition(-1, -1)
        self.assertEqual(result, -2)

        result = addition(-1, 1)
        self.assertEqual(result, 0)

    def test_sub(self):
        """Funciona?"""
        result = subtraction(9, 3)
        self.assertEqual(result, 6)
        self.assertEqual(subtraction(0, 7), -7)
        self.assertEqual(subtraction(81, 5), 76)
        self.assertEqual(subtraction(5, 5), 0)

    def test_mult(self):
        """Funciona?"""
        result = multiplication(5, 6)
        self.assertEqual(result, 30)
        self.assertEqual(multiplication(0, 6), 0)
        self.assertEqual(multiplication(-5, 7), -35)
        self.assertEqual(multiplication(-9, -9), 81)
        self.assertEqual(multiplication(1, 13), 13)

    def test_division(self):
        """Funciona?"""
        result = division(4, 2)
        self.assertEqual(result, 2)
        self.assertEqual(division(0, 5), 0)
        self.assertEqual(division(33, 5), 6.6)
        self.assertEqual(division(45, 0), None)

if __name__ == "__main__":
    unittest.main()