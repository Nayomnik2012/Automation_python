import unittest
from Lessons_5_Home_Work import ITEmployee

# ЗАДАНИЕ 6
# Задание (на создание тестов c помощью unittest)
# Создайте наборы тестов на написанные функции из прошлого домашнего
# задания:
# 6.1 Написать функцию is_year_leap, принимающую 1 аргумент — год, и
# возвращающую True, если год високосный, и False иначе.
# 6.2 Функция принимает три числа a, b, c. Функция должна определить,
# существует ли треугольник с такими сторонами. Если треугольник
# существует, вернёт True, иначе False.
# 6.3 Функция принимает три числа a, b, c. Функция должна определить,
# существует ли треугольник с такими сторонами и если существует, то
# возвращает тип треугольника Equilateral triangle (равносторонний), Isosceles
# triangle (равнобедренный), Versatile triangle (разносторонний) или не
# треугольник (Not a triangle).
def triangle1(a, b, c):
    if (c >= (a + b)) or (b >= (a + c)) or (a >= (b + c)):
        return False
    else:
        return True

def is_year_leap(year):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return True # Так же можно присвоить переменной True
    else:
        return False # Аналогично

class AssertYearAndTriangle(unittest.TestCase):

    def test_check_year(self):
        res = triangle1(2, 3, 3)
        self.assertTrue(res)

    def test_check_triangle(self):
        ser = is_year_leap(2020)
        self.assertTrue(ser)

if __name__ == "__main__":
    unittest.main()

# Задание 7 (на создание тестов c помощью unittest)
# Создайте наборы тестов на тестирование класса ITEmployee, который вы
# реализовали в Задании 1
# (или Employee, или Person в зависимости до куда вы дошли в выполнении Задания 1).
class ITEmployeeTest(unittest.TestCase):
    def setUp(self):
        self.emp = ITEmployee("Alex Kovalskiy", 1987, "programmer", 6, 300)

    def test_name(self):
        self.assertEqual(self.emp.name(), "Alex")

    def test_lastName(self):
        self.assertEqual(self.emp.last_name(), "Kovalskiy")

    def test_how_year(self):
        a = self.emp.today_data(2020)
        self.assertEqual(a, 33)

    def test_chek_position(self):
        a = self.emp.work(3, 'programmer')
        self.assertEqual(a, "Junior programmer")

    def test_salary(self):
        a = self.emp.money(200)
        self.assertEqual(a, 500)

if __name__ == "__main__":
    unittest.main()
