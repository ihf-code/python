import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def modulus(a, b):
    return a % b


class TestAddition(unittest.TestCase):
    def test_addition(self):
        result = add(2, 4)
        self.assertEqual(result, 6)


class TestSubtraction(unittest.TestCase):
    def test_subtraction(self):
        result = subtract(10, 2)
        self.assertEqual(result, 8)


class TestMultiplication(unittest.TestCase):
    def test_multiplication(self):
        result = multiplication(5, 3)
        self.assertEqual(result, 15)


class TestDivision(unittest.TestCase):
    def test_division(self):
        result = division(7, 2)
        self.assertEqual(result, 3.5)


class TestModulus(unittest.TestCase):
    def test_modulus(self):
        result = modulus(10, 3)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
