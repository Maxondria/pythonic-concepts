import unittest

import calc


class TestCalc(unittest.TestCase):
    '''[Test that add() works]

    Description:
        Adds two numbers
    '''

    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(calc.subtract(-1, -2), 1)

    def test_multiply(self):
        self.assertEqual(calc.multiply(-1, 2), -2)

    def test_divide(self):
        self.assertEqual(calc.divide(3, 2), 1.5)
        self.assertEqual(calc.divide(10, 2), 5)

        # Testing errors raised
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
