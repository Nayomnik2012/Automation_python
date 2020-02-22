a = ['wqwq', '21', '1234', 'd']
b = 0
for i in a:
    if len(i) % 2 != 0:
        b += 1
print(b)

a = {"VALUE" : 1212, "DEAD": 32323, "dsad": "32321"}

for i, value in a.items():
    print(i, type(value))

for key in a:
    print(key, ':', a[key]) # Альтернативное решение


print(10)
raise ValueError
print('Dead')
