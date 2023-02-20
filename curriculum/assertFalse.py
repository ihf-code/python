import unittest


def is_negative(number):
    return number < 0


class TestIsNegative(unittest.TestCase):
    def test_negative_number(self):
        result = is_negative(-8)
        self.assertTrue(result, "-8 is a negative number")

    def test_positive_number(self):
        result = is_negative(5)
        self.assertFalse(result, "8 is not a negative number")


if __name__ == '__main__':
    unittest.main()
