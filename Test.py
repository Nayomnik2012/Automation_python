# 2) Пишем функцию, которая попросит пользователя ввести слово (строка без пробелов в
#    середине, а вначале и в конце пробелы могут быть). Пока он не введёт правильно, просите
#    его ввести. Функция возвращает введённое слово.

a = "Привет, я Вас, а ты кто ?"
while a:
    print(a.strip(','))
