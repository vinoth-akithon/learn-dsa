import unittest

def factorial(n):
    if n < 0:
        raise ValueError("Factorial can be found for positive integers")
    if n == 0:
        return 1
    return n * factorial(n-1)


class TestCase(unittest.TestCase):
    def test_negative_integer(self):
        self.assertRaises(ValueError, factorial, -1)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_artibirary_number(self):
        self.assertEqual(factorial(5), 120)



if __name__ == "__main__":
    # print(factorial(1))
    unittest.main()