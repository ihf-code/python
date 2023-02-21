import unittest

def calculate_pi():
    return 3.14159265358979323846

class TestCalculatePi(unittest.TestCase):
    def test_calculate_pi(self):
        result = calculate_pi()
        self.assertAlmostEqual(result, 3.14, places=2)

if __name__ == '__main__':
    unittest.main()
