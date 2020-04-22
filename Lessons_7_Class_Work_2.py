# Генерация отчета в HTML
import unittest
from HtmlTestRunner import HTMLTestRunner

test_results = "testResults/"

class OurTestCase(unittest.TestCase):

    def test_method(self):
        self.assertEqual(4, 7)

    def test_method2(self):
        self.assertEqual(4, 4)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=test_results))
