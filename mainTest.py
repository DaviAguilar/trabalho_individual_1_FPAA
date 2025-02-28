import unittest
from main import karatsuba

class KaratsubaTestCase(unittest.TestCase):
    def test_karatsuba(self):
        test_cases = [
            (1234, 5678, 1234 * 5678),
            (56, 78, 56 * 78),
            (123, 456, 123 * 456),
            (0, 1234, 0 * 1234),
            (999, 999, 999 * 999),
            (123456789, 987654321, 123456789 * 987654321),
            (123, 456, 123 * 457)  # This test case is expected to fail
        ]

        for x, y, expected in test_cases:
            with self.subTest(x=x, y=y):
                self.assertEqual(karatsuba(x, y), expected)

if __name__ == '__main__':
    unittest.main()