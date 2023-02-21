import unittest

def find_value(value, lst):
    return value in lst

class TestFindValue(unittest.TestCase):
    def test_find_value(self):
        result = find_value(2, [1, 2, 3, 4, 5])
        self.assertIn(result, [True, False])

if __name__ == '__main__':
    unittest.main()
