# ЗАДАНИЕ 1
# Входные данные
# Пользователь вводит строку.
# Выходные данные
# Воспользуйтесь одним print(), но при этом выводите с новой строки:
# 1)Сначала выведите третий символ этой строки.
# 2)Во второй строке выведите предпоследний символ этой строки.
# 3)В третьей строке выведите первые пять символов этой строки.
# 4)В четвертой строке выведите всю строку, кроме последних двух символов.
# 5)В пятой строке выведите все символы с четными индексами (считая, что индексация
#   начинается с 0, поэтому символы выводятся, начиная с первого символа).
# 6)В шестой строке выведите все символы с нечетными индексами, то есть начиная со
#   второго символа строки.
# 7)В седьмой строке выведите все символы в обратном порядке.
# 8)В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# 9)В девятой строке выведите все символы строки через один в обратном порядке, начиная с предпоследнего.
# 10)В десятой строке выведите все символы в обратном порядке без первого и последнего элемента.
# 11)Ну, и напоследок выведите длину данной строки.
# 12)PS: Выловите исключения, если введённая строка слишком короткая. Какого типа исключение надо выловить?
try:
      a = input("Введите данные: ")
      print("1 строка: " + a[2], "2 строка: " + a[-2], "3 строка: " + a[:5], "4 строка: " + a[:-2],
            "5 строка: " + a[::2], "6 строка: " + a[1::2], "7 строка: " + a[::-1], "8 строка: " + a[::-2],
            "9 строка: " + a[-2::-2], "10 строка: " + a[-2:0:-1], "11 Длина строки: " + str(len(a)), sep="\n")
except IndexError:
      print("Вы ввели не достаточно символов!")


# ЗАДАНИЕ 2
# Пользователь вводит строку. Разрежьте её на две части – равные, если длина строки чётная, а
# если длина строки нечётная, то длина первой части должна быть на один символ больше.
# Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.

a = input('Введите данные: ')
if len(a) % 2 == 0:
      d = int(len(a) / 2)
      print(a[d:] + a[:d])
else:
      d = int(len(a) / 2)
      print(a[d:] + a[:d])

# ЗАДАНИЕ 3
# 1) Напишите счетчик с помощью конструкции while, который выводит числа от 0 до 10.
i = 0
while i < 10:
      i += 1
      print(i)

# 2)Напишите счетчик с помощью конструкции while, который выводит числа от 20 до 1.
#   Попробуйте вывести числа в одной строчке, разделённые пробелом

b = 0
while b < 20:
      b += 1
      print(b, end=' ')
      print(end='\n')

# 3) Напишите цикл while, в котором вы, если число чётное, каждую итерацию уменьшаете его
#    в 2 раза. Вы делите целое чётное число на 2 пока от него не останется нечётный остаток.
#    Посчитайте сколько раз вы делили нацело на 2.
s = 0
a = int(input("Введите четное число: "))
while True:
      s += 1
      if a % 2 == 0:
            a = a // 2
            print("Число: " + str(a))
      else:
            print("Количество итераций " + str(s))
            break

# ЗАДАНИЕ № 4
# У вас есть список чисел.
# 1) Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым.
a = [1, "2", 3, 4, 5]
for i in list(a):
    a.remove(i)
    print(a)

# 2) Как сделать это же задание со строкой: напишите цикл, который выводит на экран и
#    «удаляет» первый символ строки, пока она не станет пустой?
a = "123456"
a = list(a)
for i in list(a):
    a.remove(i)
    print(a)

# 3) Напишите цикл, который выводит на экран и удаляет элементы списка от самого
#    маленького до самого большого, пока он не останется пустым.
a = [88885, 1, 333, 36, 4444]
for i in list(a):
    a.sort()
    a.pop()
    print(a)
# 4) ** Дана последовательность натуральных ненулевых чисел, завершающаяся числом 0.
#     Определите, какое наибольшее число подряд идущих элементов этой последовательности
#     равны друг другу.
#(НЕ ПОНИМАЮ ДАННОЕ ЗАДАНИЕ????)------------------------------------


# ЗАДАНИЕ № 5
# Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не
# является числом (любым), то должна выполняться конкатенация, т. е. соединение, строк. В
# остальных случаях введённые числа суммируются.

a = input("Введите число: ")
b = input("Введите число: ")
if a.isdigit() and b.isdigit():
    print("Сумма: ", int(a) + int(b))
else:
    print(a + b)

# ЗАДАНИЕ № 6
# Оформляем в функции наши задания на уроке:
# 1) Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите
#    его ввести. Функция возвращает введённое число.
#    Теперь далее для других задач с числами, вы можете пользоваться этой функцией, а не
#    простым input!

def number():
    while True:
        a = input('Введите число 4: ')
        if a == '4':
            print('Правильно! вы ввели: ', a)
            break
        else:
            print('Вы ввели: ', a, " Введите 4")
number()

# 2) Пишем функцию, которая попросит пользователя ввести слово (строка без пробелов в
#    середине, а вначале и в конце пробелы могут быть). Пока он не введёт правильно, просите
#    его ввести. Функция возвращает введённое слово.

def fun2():
    while True:
        a = input('Введи слово: ')
        x = a.strip(' ')
        if x.isalpha() == 1:
            print('Ты ввел: ', a.strip())
            break
        else:
            print('Введите слово!')
fun2()

# Это уже было в предыдущем ДЗ, но теперь оформите это функцией:
# 3) Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
#    если год високосный, и False иначе.

def is_year_leap(year):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return True # Так же можно присвоить переменной True
    else:
        return False # Аналогично

is_year_leap(2020)

# 4) Функция принимает три числа a, b, c. Функция должна определить, существует ли
#    треугольник с такими сторонами. Если треугольник существует, вернёт True, иначе False.

def triangle1(a, b, c):
    if (c >= (a + b)) or (b >= (a + c)) or (a >= (b + c)):
        return False
    else:
        return True

triangle1(3, 3, 3)

# 5) Функция принимает три числа a, b, c. Функция должна определить, существует ли
#    треугольник с такими сторонами и если существует, то возвращает тип треугольника
#    Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный), Versatile triangle
#    (разносторонний) или не треугольник (Not a triangle).

# (Профан, не шарю в треугольниках)------------------------------------

# 6) Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2,
#    y2), вычисляющую расстояние между точками с координатами (x1, y1) и (x2, y2). Считайте
#    четыре действительных числа от пользователя и выведите результат работы этой функции.

# (Профан, не шарю)-------------------------------

# ЗАДАНИЕ № 7
# Создайте строку, в которой написан, какой-то текст. Пример:
# We are not what we should be!
# We are not what we need to be.
# But at least we are not what we used to be
# (Football Coach)
# 1)Посчитайте сколько слов в тексте (разбейте на слова методом строк split)

#----------------

# 2) Удалите знаки препинания в списке слов (пройдитесь циклом все слова и удалите
#    методом strip знаки препинания)
a = ["dsds,", "sasa,", 'sasas,']
while True:
    s = 2
    b = ''.join(a)

# 3) Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
a = ["А", "Б", "В", "Г", "Ж", "З"]
print(sorted(a))

# 4) Посчитать, сколько раз встречается каждое слово.
#    (Подсказка: создавать словарь, где ключи — это слова из текста, а в значениях подсчитываем количество
#    «встречаний» этого слова)

# ------------------

# 5) Слова с большой буквы и с маленькой это все равно одно и тоже слово

# (Профан, не понимаю...) -------------------------------------------


# 6) Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2,
#  y2), вычисляющую расстояние между точками с координатами (x1, y1) и (x2, y2). Считайте
#  четыре действительных числа от пользователя и выведите результат работы этой функции.

# (Профан, не понимаю...) -----------------------------------------------

# ЗАДАНИЕ № 7
# Создайте строку, в которой написан, какой-то текст. Пример:
# We are not what we should be!
# We are not what we need to be.
# 1) Посчитайте сколько слов в тексте (разбейте на слова методом строк split)

a = "We are not what we should be!"
print(len(a.split()))

# 2) Удалите знаки препинания в списке слов (пройдитесь циклом все слова и удалите
#    методом strip знаки препинания)

a = "Привет, я Вас, а ты кто ?"
while a:
    print(a.slit(','))

