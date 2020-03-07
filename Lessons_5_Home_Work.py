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

class Person:
    def __init__(self, full_name, age = 1900):
        self.full_name = full_name
        assert type(self.full_name) is str, ("данные не STR")
        if len(self.full_name.split()) is not 2:
            raise NameError('Invalid name!')
        self.age = age
        if self.age < 1900 or self.age > 2019:
            raise ValueError("Полученный возраст " + str(self.age) + " не поддерживается")

    def name(self):
        a = self.full_name.split()
        return a[0]

    def last_name(self):
        a = self.full_name.split()
        return a[1]

    def today_data(self, year2 = 2020):
        a = year2 - self.year
        if a < 0:
            return "полученное число не может быть меньше даты рождения"
        return year2 - self.year

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
    def __init__(self, full_name, age = 1900, position = None, experience = None, salary = None):
        super.__init__(full_name, age)
        self.position = position
        self.experience = experience
        if self.experience < 0:
            raise ValueError("Число не может быть отрецательным!")
        self.salary = salary
        if self.salary < 0:
            raise ValueError("Число не может быть отрецательным!")

    def position(self, ):
        if self.experience < 3:
            return ''