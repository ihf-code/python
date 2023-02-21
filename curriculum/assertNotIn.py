import unittest

def find_value(value, lst):
    return value in lst

class TestFindValue(unittest.TestCase):
    def test_find_value(self):
        result = find_value(0, [1, 2, 3, 4, 5])
        self.assertNotIn(result, [True])

if __name__ == '__main__':
    unittest.main()
