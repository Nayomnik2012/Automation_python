import unittest
from Lessons_3_Home_Work import is_year_leap, triangle1

class AssertYearAndTriangle(unittest.TestCase):
    def SetUp(self):
        self.years = is_year_leap(2020)
        self.triangle = triangle1(3, 4, 3)

    