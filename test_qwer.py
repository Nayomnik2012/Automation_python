import unittest
from q import is_year_leap

class TestLeapYear(unittest.TestCase):
    def test_year_leap2(self):
        year = 2020
        res = is_year_leap(year)
        self.assertTrue(res)

    def test_year_leap(self):
        year = 1
        res = is_year_leap(year)
        self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()

