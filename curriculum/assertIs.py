import unittest

def return_list():
    return []

class TestReturnList(unittest.TestCase):
    def test_return_list(self):
        result = return_list()
        self.assertIs(result, [])

if __name__ == '__main__':
    unittest.main()
