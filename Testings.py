# Задание 5
# Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата (В первой строке заголовки
# колонок)
# Посчитайте сколько отделов на фирме
# Определите максимальную зарплату
# Определите максимальную зарплату в каждом отделе
# Выведите «Отдел Макс_Зарплата Фамилия_человека_с_такой_зарплатой» в
# новый файл
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

info_max_salary = dict.fromkeys(keys, 0)
print(info_max_salary)
for salary in emps:
    if int(salary['salary']) > info_max_salary['salary']:

print(info_max_salary)
