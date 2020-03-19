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
id_post = reg_dict_post['id']
print(type(id_post))

# Проверяете, что она создалась и доступна по ссылке GET/books/[id]
get_api = requests.get(base_url + "books/" + str(id_post))
reg_dict_get = get_api.json()
assert reg_dict_post == reg_dict_get

# Проверяете, что она есть в списке книг по запросу GET /books/
get_all_books = requests.get(base_url + "books/")
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
put_api = requests.put(base_url + "books/" + str(id_post), data=data_params)



# Проверьте, что она изменилась и доступна по ссылке /books/[id]/
get_api = requests.get(base_url + "books/" + str(id_post))
reg_dict_get = get_api.json()
reg_dict_get.pop('id')
assert data_params == reg_dict_get, "Измененныи данные не совпадают с полученными!"

# Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
get_api = requests.get(base_url + "books/")
reg_dict_get = get_api.json()
get_dict = fun1(reg_dict_get)
get_dict.pop('id')
assert get_dict == data_params, "при проверке списка книг, не найдена книга с изменениями"


# Удаляете эту книгу методом DELETE /books/[id].
delete_api = requests.delete(base_url + "books/" + str(id_post))

# Второй скрипт:
# тоже самое с ролями. Здесь немного поинтересней, т.к. есть связка с
# книгой, которая уже должна существовать. Создайте книгу заранее в
# этом же скрипте, не надейтесь на книги, которые вы видите, их кто-то
# другой может удалить.
url_roles = "http://pulse-rest-testing.herokuapp.com/roles"


