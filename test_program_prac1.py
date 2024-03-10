import unittest
from program_prac1 import sqrNumber

class TestSqrNumber(unittest.TestCase):
    def test_sqr_5(self):
        self.assertEqual(sqrNumber(5), 25)

    def test_sqr_8(self):
        self.assertEqual(sqrNumber(8), 64)

    def test_sqr_0(self):
        self.assertEqual(sqrNumber(0), 0)

    def test_sqr_10(self):
        self.assertEqual(sqrNumber(10), 100)

    def test_sqr_1(self):
        self.assertEqual(sqrNumber(1), 1)

if __name__ == '__main__':
    unittest.main()
