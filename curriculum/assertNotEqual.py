import unittest


def compare_numbers(a, b):
    return a != b


class TestCompareNumbers(unittest.TestCase):
    def test_compare_numbers(self):
        result = compare_numbers(10, 20)
        self.assertNotEqual(result, False)


if __name__ == '__main__':
    unittest.main()
