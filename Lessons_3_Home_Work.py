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
#(НЕ ПОНИМАЮ ДАННОЕ ЗАДАНИЕ????)


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
