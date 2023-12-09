# test_my_math.py
import unittest
import pytest

from my_math import add_numbers


class TestMyMathFunctions(unittest.TestCase):

    def test_add_numbers(self):
        # Test case 1
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

        # Test case 2
        result = add_numbers(-1, 1)
        self.assertEqual(result, 0)

        # Test case 3
        result = add_numbers(0, 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
