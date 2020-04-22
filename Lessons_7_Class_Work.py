import requests

get_url_link = "http://pulse-rest-testing.herokuapp.com/roles/"
r = requests.get(get_url_link)
roles = r.json()
print(roles) # Выводим полный список словарей

# Ищем в словаре максимальное значение ключа "level"
max_level = 0
for role in roles:
    if role["level"] > max_level:
        max_level = role["level"]
print(max_level)

# Альтернативное решение с помощью генератора словарей и функции MAX
max_level_2 = max([role["level"] for role in roles])
print(max_level_2)

# Выводим список максимального уровня каждого типа
types = [role["type"] for role in roles]
unique_types = list(set(types)) # Создаем список уникальных значений с помощью SET
max_level_in_types = dict.fromkeys(unique_types, 0) # передаем методу dict.fromkeys список "types" где 0 это значение,
# но можно и без его, тогда значение будет None

# Аналогичное решение, только с Цыклом
max_level_in_types = {}
for item in unique_types:
    max_level_in_types[item] = 0

# Перебираем полученный Джсон и сравниваем с созданным Словарем и если в нашем словере уровень ниже, добавляем
for role in roles:
    if role["level"] > max_level_in_types[role["type"]]:
        max_level_in_types[role["type"]] = role["level"]
print(max_level_in_types)

#