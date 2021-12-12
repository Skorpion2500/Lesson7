"""Задание 1"""
def code(a):
    for i in range(len(a)):
        a[i] = a[i].encode('utf-8')
    return a

def decode(a):
    for i in range(len(a)):
        a[i] = a[i].decode('utf-8')
    return a

test = ["hello", "world", "!"]
x = code(test)
print("Закодированный текст:", x)
x = decode(x)
print("Декодированный текст:", x)

"""Задание 2"""

file = open('D:/Programs/Python/input.txt')
"""Чтение файла по одной строке"""
c = int(file.readline())
h = int(file.readline())
o = int(file.readline())
"""Узнаем сколько молекул можно "собрать" из каждого атома и находим среди них наименьшее"""
molecules = int(min(c/2, h/6, o))
file.close()
f = open('D:/Programs/Python/output.txt', 'w')
print(f.write("Количество молекул=" + str(molecules)))
f.close()
