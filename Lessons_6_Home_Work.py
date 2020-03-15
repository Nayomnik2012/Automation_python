# ЗАДАНИЕ 1 (Обязательное всем, кроме части со звёздочкой!!!!)
# Тестовое приложение с REST API http://pulse-rest-testing.herokuapp.com/
# Создаём один скрипт:
# Создаём книгу POST /books/, вы запоминаете его id.
import requests

base_url = "http://pulse-rest-testing.herokuapp.com/"
data_params = {
    "title": "Изучения Python Automation",
    "author": "Александр Ковальский"
}
post_api = requests.post(base_url + "books/", data=data_params)
reg_dict_post = post_api.json()
id_post = str(reg_dict_post['id'])
print(type(id_post))

# Проверяете, что она создалась и доступна по ссылке GET/books/[id]
get_api = requests.get(base_url + "books/" + id_post)
reg_dict_get = get_api.json()
assert reg_dict_post == reg_dict_get

# Проверяете, что она есть в списке книг по запросу GET /books/
get_all_books = requests.get(base_url + "books/")
reg_dict_get = get_all_books.json()
for i in reg_dict_get:
    for a, k in i.items():
        if k == int(id_post):
            assert k == int(id_post)
