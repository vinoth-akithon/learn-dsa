import unittest


def summation(n: int) -> int:
    if n < 0:
        raise ValueError("summation can be found for positive integers")
    if n < 2:
        return n
    return n + summation(n-1)


class TestCase(unittest.TestCase):
    def test_negative_integer(self):
        self.assertRaises(ValueError, summation, -1)

    def test_zero(self):
        self.assertEqual(summation(0), 0)

    def test_one(self):
        self.assertEqual(summation(1), 1)

    def test_artibirary_number(self):
        self.assertEqual(summation(5), 15)

if __name__ == "__main__":
    # print(summation(5))
    unittest.main()