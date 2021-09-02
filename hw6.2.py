from itertools import cycle

a = int(input('Введите количество повторений - '))
c = 0
for el in cycle(input('Введите список элементов - ')):
    if c > a:
        break
    print(el)
    c += 1
