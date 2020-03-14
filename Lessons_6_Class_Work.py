from Lessons_4_Home_Work import strings
import requests
import json
# 1) Записать в текстовый файл и вашу песню “la-la-la”.
with open("text.txt", 'w') as new_file:
    new_file.write(strings())


# 2) Прочитать и вывести на экран код файла, в котором вы создавали класс Person
with open("text.txt", 'r') as new_file:
    print(new_file.read())


with open("text.txt", 'r') as new_file:
    for text in new_file:
        print(text, end='') # или text[:-1] убираем перевод строки...


with open("text.txt", 'a', encoding="utf-8") as new_file:
    print("кукушка", file=new_file)


# Get

# s = requests.get('https://google.com.ua')
# #print(s.text)
# print(s.apparent_encoding)
# print(s.content)
# print(s.cookies)
# print(s.headers)
# print(s.status_code)
# print(s.url)
# print(s.content)
# print()
data = {"new": 12}
r = requests.get('https://httpbin.org/get', data=data, headers={'User-Agent': 'Hello'})
rest_body = json.loads(r.text)
print(rest_body["headers"])

r = requests.get('https://httpbin.org/get')
resp = r.json()
print(resp["headers"])


parameters = {"q": "sometings"}
data = {"new": 12}
r = requests.post(
    'https://httpbin.org/get',
    params=parameters,
    data=data,
    headers={'User-Agent': 'Hello'})
