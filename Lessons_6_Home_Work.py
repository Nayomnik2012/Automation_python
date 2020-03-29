# ЗАДАНИЕ 1 (Обязательное всем, кроме части со звёздочкой!!!!)
# Тестовое приложение с REST API http://pulse-rest-testing.herokuapp.com/
# Создаём один скрипт:
# Создаём книгу POST /books/, вы запоминаете его id.
import requests
import random
from Lessons_4_Home_Work import liters
import smtplib, ssl

base_url = "http://pulse-rest-testing.herokuapp.com/books/"
data_params = {
    "title": "Изучения Python Automation",
    "author": "Александр Ковальский"
}
post_api = requests.post(base_url, data=data_params)
reg_dict_post = post_api.json()
id_post = reg_dict_post['id']
print(type(id_post))

# Проверяете, что она создалась и доступна по ссылке GET/books/[id]
get_api = requests.get(base_url + str(id_post))
reg_dict_get = get_api.json()
assert reg_dict_post == reg_dict_get

# Проверяете, что она есть в списке книг по запросу GET /books/
get_all_books = requests.get(base_url)
reg_dict_get = get_all_books.json()
def fun1(reg_dict_get):
    for i in reg_dict_get:
        for v, k in i.items():
            if k == id_post:
                return i

get_dict = fun1(reg_dict_get)
get_dict.pop('id')
assert get_dict == data_params, "В списках книг, нет нужной книги!"

# # Измените данные этой книги методом PUT/books/[id]/
data_params = {
    "title": "Изменение книги Python",
    "author": "Alex Kovalskiy"
}
put_api = requests.put(base_url + str(id_post), data=data_params)



# Проверьте, что она изменилась и доступна по ссылке /books/[id]/
get_api = requests.get(base_url + str(id_post))
reg_dict_get = get_api.json()
reg_dict_get.pop('id')
assert data_params == reg_dict_get, "Измененныи данные не совпадают с полученными!"

# Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
get_api = requests.get(base_url)
reg_dict_get = get_api.json()
get_dict = fun1(reg_dict_get)
get_dict.pop('id')
assert get_dict == data_params, "при проверке списка книг, не найдена книга с изменениями"


# Удаляете эту книгу методом DELETE /books/[id].
delete_api = requests.delete(base_url + str(id_post))

# Второй скрипт:
# тоже самое с ролями. Здесь немного поинтересней, т.к. есть связка с
# книгой, которая уже должна существовать. Создайте книгу заранее в
# этом же скрипте, не надейтесь на книги, которые вы видите, их кто-то
# другой может удалить.
url_roles = "http://pulse-rest-testing.herokuapp.com/roles/"

get_all_book = requests.get(base_url)
reg_dict_get = get_all_book.json()
if reg_dict_get == {'detail': 'Not found.'}:
    post_api = requests.post(base_url, data=data_params)
    reg_dict_post = post_api.json()
    id_number = reg_dict_post['id']
    print("нет книг, но создалась новая")
else:
    get_random_element = random.choice(reg_dict_get)
    id_number = get_random_element['id']

number_level = random.randint(1, 1000)

data_params_roles = {
    "name": "Alex",
    "type": "Kovalskiy",
    "level": number_level,
    "book": base_url + str(id_number)
}

post_api_roles = requests.post(url_roles, data=data_params_roles)

# Третий скрипт:
# Поэкспериментируйте создавать книги и роли с неправильными
# данными. Посмотрите тело и статус код ответов.
# Попробуйте создать роль с ссылкой на книгу, которой нет. Посмотрите
# тело и статус код response.
url_roles = "http://pulse-rest-testing.herokuapp.com/roles/"
data_params_roles = {
    "name": "ewewee",
    "type": "Kovalskiy",
    "level": "123",
    "book": "http://pulse-rest-testing.herokuapp.com/books/1"
}

post_api_roles = requests.post(url_roles, data=data_params_roles)
status_api = post_api_roles.json()
print(status_api)
print(post_api_roles.status_code)

# Задание 2
# Задания из класса про работу с файлами на слайдах 4, 8, 9, 10:
# 1. Кто не успел доделываем / тем, кто успел: воспользуйтесь другим способом
# для записи в файл (кто сделал с помощью методов – делают с помощью print,
# кто сделал с помощью print – делают с помощью методов)
# 2. А теперь воспользуйтесь менеджером контекста для файлов (with … as).


# Задание 3
# Записывает в новый файл все слова в алфавитном порядке из другого файла с
# текстом. Каждое слово на новой строке.
# Рядом со словом укажите сколько раз оно встречалось в тексте
with open("files/text.txt", 'r', encoding="utf-8") as new_file:
    for text in new_file:
        a = text.split()

a = [liters(x) for x in a]
b = sorted(a)
result = {i: a.count(i) for i in b}

with open("files/text2.txt", 'w', encoding="utf-8") as new_file:
    for a, v in result.items():
        result = a + ' ' + str(v)
        print(result, end='\n', file=new_file)

# Задание 4
# Жду от вас письмо! (слайды 14-18). Воспользуйтесь менеджером контекста
# (with … as) (слайд 20)
# (Не забудьте для себя понять код из официальной документации – слайд 17).
port = 465  # для SSL подключения
smtp_server = "smtp.gmail.com"
sender_email = "acsk.ndu@gmail.com"  # Ваш емайл
receiver_email = "nayomnik30@gmail.com"  # Емайл получателя
password = input("Введите пароль и нажмите Enter: ")
message = """\
Subject: Test smtplib

It's works! Alex Kovalskiy"""


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

# Задание 5
# Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата (В первой строке заголовки
# колонок)
# Посчитайте сколько отделов на фирме
# Определите максимальную зарплату
# Определите максимальную зарплату в каждом отделе
# Выведите «Отдел Макс_Зарплата Фамилия_человека_с_такой_зарплатой» в
# новый файл
# Подсказка: используйте словари!!!
file = 'files/test.csv'
with open(file, 'r', encoding="utf-8") as new_file:
    first_line = new_file.readline()
    keys = first_line.split(";")[:-1]
    emps = []  # <- создаем пустй список
    for line in new_file:
        values = line.split(';')[:-1]
        d = {}
        for i in range(len(keys)):
            d[keys[i]] = values[i]
        emps.append(d)  # <- заполняем его
deps = [emp["Department"] for emp in emps]
print(len(list(set(deps))))
deps = max([emp["salary"] for emp in emps]) # Максимальная ЗП с генератором списка

max_level = 0 # Перебор в ручную, максимальной ЗП
for d in emps:
    if int(d['salary']) > int(max_level):
        max_level = d['salary']

department = [emp['Department'] for emp in emps]
unigue_department = list(set(department))

max_salary_in_department = dict.fromkeys(unigue_department, 0) # создается словарь с значением 0
print(max_salary_in_department)
# max_salary_in_department = {} ## Создаем словарь с нулевыми значениями в ручную
# for item in unigue_department:
#     max_salary_in_department[item] = 0
# print(max_salary_in_department)

for dep in emps: #
    if int(dep['salary']) > int(max_salary_in_department[dep['Department']]):
        max_salary_in_department[dep['Department']] = int(dep['salary'])
print(max_salary_in_department)

