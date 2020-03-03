# конструктор класса __init__(self):

class Person:
    def __init__(self, name = '', surname = '', age = None, position = None):
        self.name = name
        self.surname = surname
        self.age = age
        self.position = position

    def full_name(self):
        return self.name + ' ' + self.surname
#        return f"{self.name} {self.surname}"  пример № 2

    def get_older(self, years):
        self.age += years

a = Person('Sasha', 'Kov')

print(a.full_name())

# Наследование

class Employee(Person):
    def __init__(self, name = '', surname = '', age = None, position = None, salary = 0):
        super.__init__(name, surname, age, position) # Вписываем свойства конструктора "Родительского класса"
        self.salary = salary # добавляем новое свойство конструктора в дочерний класс


    def get_older(self, years=1):
        self.age += years

# ITEmployee принимает
class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.skills = []

if __name__ == "__main__":
    e1 = ITEmployee("Olya", 25, "QA")
    print(e1.name)

# -----
class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self, x, y):
        return self.x * self.y

q = Room()
print(area(3, 3))

# ----

