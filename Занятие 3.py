import cmath
import math

"""Задание 1"""
pozition = [0, 0]
print("Выберите направление движения: вниз, вверх, влево, вправо")
orientation = input("Направление=")
print("Какое количество шагов?")
steps = int(input("Шаги="))
if orientation == "вниз":
    pozition[1] -= steps
elif orientation == "вверх":
    pozition[1] += steps
elif orientation == "влево":
    pozition[0] -= steps
elif orientation == "вправо":
    pozition[0] += steps
else:
    print("Направление или колиство шагов введены неверно")
print("Текущая позиция - ", pozition)
"""Задание 2"""
pozition = [0, 0]
while True:
    print("Выберите направление движения: вниз, вверх, влево, вправо. Для прекращения движения напишите \"стой\"")
    orientation = input("Направление=")
    if orientation == "стой":
        print("Вы остановились")
        break
    print("Какое количество шагов?")
    steps = int(input("Шаги="))
    if orientation == "вниз":
        pozition[1] -= steps
    elif orientation == "вверх":
        pozition[1] += steps
    elif orientation == "влево":
        pozition[0] -= steps
    elif orientation == "вправо": 
     pozition[0] += steps
    else:
        print("Направление или колиство шагов введены неверно")
    print("Текущая позиция - ", pozition)
"""Задание * и ** одновременно"""
print("Введите коэфициенты квадратного уравнения: ax^2+bx+c=0")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
D = b**2 - 4*a*c
if D < 0:
    print("Дискриминант отрицательный")
    D = complex(D)
    print(D)
    x1 = (-b + cmath.sqrt(D))/(2*a)
    x2 = (-b - cmath.sqrt(D))/(2*a)
    print("Корни квадратного уравнения с отрицательным дискриминантом:", x1, x2)
else:
    print("Дискриминант неотрицательный")
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print ("Корни квадратного уравнения:", x1, x2)