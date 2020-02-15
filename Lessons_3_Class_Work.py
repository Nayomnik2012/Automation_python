a = "Hello"
b = "Hub"

print(a, b, sep=', ', end=' :;')
print('20.03.2020')



a = [10, 2, 3, 4, 5, 6]


for i in range(len(a)): # с помощью len() присваеваем индексы
    if a[i] % 2 != 0:
        a[i] += 1
print(a)

# while True:
#     a = input('введите слово без пробелов: ')
#     if a.count(' ') > 0:
#         continue
#     else:
#         break
#
# while True:
#     world = input('dfdfd')
#     if ' ' not in world:
#         break

while True:
    a = input('Введите число: ')
    try:
        x = float(a)
    except ValueError:
        print('Вы ввели не число!')
    else:
        break