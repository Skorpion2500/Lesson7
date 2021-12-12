"""Задание 1"""
def password(pas):
    flag = False
    x=str(1234567890)        
    for i in x:
        if i in pas:
            """Если в пароле встречается цифра, то мы продолжаем проверку"""
            flag = True
    if flag == False:
        print("Пароль должен содержать хотя бы 1 цифру")
        return flag
    if len(pas) < 6:
        flag = False
        print("В пароле должно быть не менее 6 символов")
        return flag
    if pas.isdigit():
        flag = False
        print("Пароль не может состоять только из цифр")
        return flag
    if 'password' in pas or 'PASSWORD' in pas:
        flag = False
        print("Пароль не должен содержать слово \'password\'")
        return flag
    return flag

pas=input("Введите пароль: ")
x = password(pas)
print(x)
"""Задание 2"""
def summ(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

l = []
while True:
    print("Введите число. Ввод остановится, если будет введено что-то другое")
    b = input()
    if b.isdigit():
        b = float(b)
        l.append(b)
    else:
        break
print(l)
x = summ(*l)
print(x)
"""Задание *"""
def fibo(n):
    if n==1 or n==2:
        return 1
    return fibo(n-1) + fibo(n-2)

print("Введите номер числа фибоначи. Номер должен превышать 2.")
number = int(input())
if number >= 3:
    x = fibo(number)
    print("Число Фибоначчи с номером", number, "=", x)
else:
    print("Неверно введен номер")