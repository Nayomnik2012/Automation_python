
# ЗАДАНИЕ 1 (на создание классов)
# Переделываем (а что-то повторяем и закрепляем) наши классы таким образом:
# 1) Person (два свойства: 1. теперь full_name пусть будет свойством, а не функцией (одно
# поле, мы ожидаем - тип строка и состоит из двух слов «имя фамилия»), а свойств name и
# surname нету, 2. год рождения).

# Реализовать методы, которые:
# 1. выделяет только имя из full_name
# 2. выделяет только фамилию из full_name;
# 3. вычисляет сколько лет было/есть/исполнится в году, который передаётся
# параметром (obj.age_in(year)); если не передавать параметр, по умолчанию,
# сколько лет в этом году;
# ** (только для продвинутых) Можете в конструкторе проверить, что в full_name
# передаётся строка, состоящая из двух слов, если нет, вызывайте исключение ��
# ** (только для продвинутых) Можете в конструкторе проверить, что год рождения
# меньше 2019, но больше 1900, если нет вызывайте исключение
from Lessons_4_Home_Work import liters

class Person:
    def __init__(self, full_name, age = 1900):
        self.full_name = full_name
        assert type(self.full_name) is str, ("данные не STR")
        if len(self.full_name.split()) is not 2:
            raise NameError('Invalid name!')
        self.age = age
        if self.age < 1900 or self.age > 2019:
            raise ValueError("Полученный возраст " + str(self.age) + " не поддерживается")

    def __str__(self):
        return f"Полное имя: {self.full_name}, Возраст: {self.age}"

    def name(self):
        a = self.full_name.split()
        return a[0]

    def last_name(self):
        a = self.full_name.split()
        return a[1]

    def today_data(self, year2 = 2020):
        a = year2 - self.age
        if a < 0:
            return "полученное число не может быть меньше даты рождения"
        return year2 - self.age

a = Person("Саша Ковальский", 2019)
print(a.last_name())

# ЗАДАНИЕ 2
# 1) Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы,
# зарплата)
# ** (только для продвинутых) Можете в конструкторе проверить, что в опыт работы и
# зарплата не отрицательные ��
# Реализовать новые методы:
# 2. возвращает должность с приставкой, которая зависит от опыта работы: Junior —
# менее 3 лет, Middle — от 3 до 6 лет, Senior — больше 6 лет.
# Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior &lt;position&gt;.
# Если, например у вас объект имел должность “programmer” с опытом 2 года, метод
# должен вернуть “Junior programmer”
# 3. метод, который увеличивает зарплату на сумму, которую вы передаёте
# аргументом.

class Enployee(Person):
    def __init__(self, full_name, age=1900, position=None, experience=None, salary=None):
        super().__init__(full_name, age)
        self.position = position
        self.experience = experience
        if self.experience < 0:
            raise ValueError("Число не может быть отрецательным!")
        self.salary = salary
        if self.salary < 0:
            raise ValueError("Число не может быть отрецательным!")

    def __str__(self):
        return f"Должность: {self.position}, Опит: {self.experience}, Зарплата: {self.salary}"

    def work(self, experience, position):
        if experience <= 3:
            return "Junior " + position
        elif 3 < experience <= 6:
            return "Middle " + position
        else:
            return "Senior " + position

    def money(self, cash):
        return cash + self.salary

a = Enployee("Alex Kovalskiy", 1900, "programmer", 6, 300)
print(a.work(2, "programmer"))
print(a.money(300))

# ЗАДАНИЕ 3
# ITEmployee (наследуемся от Employee)
# 1. Реализовать метод добавления одного навыка в новое свойство skills (список) новым
# методом add_skill (см. презентацию).
# 2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список)
# новым методом add_skills.
# Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы
# расширяете список-свойство skill, или вы принимаете неопределённое количество
# аргументов, и все их добавляете в список-свойство skill

class ITEmployee(Enployee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skill = []

    def __str__(self):
        return f"Новые умения: {self.skill}"

    def add_skills(self, new_skill):
        return self.skill.append(new_skill)

a = ITEmployee("Alex Kovalskiy", 1900, "programmer", 6, 300)
a.add_skills(1)


# ЗАДАНИЕ 4
# Для всех классов сделайте __str__, чтоб объекты красиво выводились на экран!

# --- реализован метод __str__ во всех классах


# Задание 8
# (на генераторы списков и словарей – тема на самостоятельное изучение)
# 8.1 Создайте список 2 в степени N, где N от 0 до 20.
s = [2**n for n in range(0, 20)]
print(s)

# 8.2 У вас есть список целых чисел. Создайте новый список остатков от деления на 3 чисел из
# исходного списка.
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = [i % 3 for i in d]
print(f)

# 8.3 У вас есть список, в котором могут быть разные типы данных. Создайте новый список
# только чисел из этого списка.
a = ['dsds', 1, 2, 3, 'dsds', 4, 'dsaad']
s = [x for x in a if type(x) == int]
print(s)

# 8.4 У вас есть список, в котором могут быть разные типы данных. Создайте новый список
# только строк, при этом удалите усе небуквенные символы из них. Воспользуйтесь
# функцией из предыдущего задания (импортируйте её из другого своего файла)


a = ['sa8sa', 1, 'e...w8e77777777w', True, 1.7]

s = [x for x in a if type(x) == str]

b = [liters(x) for x in s if not x == str]
print(b)

# 8.5 У вас есть словарь – характеристик человека. Ключи например: “name”, “surname”, “age”,
# “position”, “address”, “skills”.
# - Сгенерируйте новый словарь с такими же ключами, а в значениях типы значений.
a = {"name": "Alex", "surname": "Kovalskiy", "age": 33, "position": "QA", "address": "Kiev", "skills": "Super boy"}

b = {k: type(v) for k, v in a.items()}
print(b)

# - Сгенерируйте новый словарь с только парами ключ-значение, если значение исходного
# словаря было строкой. Значения нового словаря должны быть переведены в нижний
# регистр и удалены всё небуквенные символы из них.


a = {"name": "Al8e.x", "surname": "Kovals*kiy", "age": 33, "position": "QA", "address": "Kiev", "skills": "Super boy"}

b = {k: v for k, v in a.items() if type(v) == str}
c = {k: liters(v) for k, v in b.items()}
print(c)