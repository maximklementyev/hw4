from math import factorial
num = int(input('Введите число - '))
def fact(num):
    for i in range(num+1):
        el = factorial(i)
        print('Факториал числа', i, '= ', end = '')
        yield el

for el in fact(num):
    print(el)
