from itertools import count

for el in count(int(input('Введите стартовое число от 0 до 99 - '))):
    if el > 100:
        break
    else:
        print(el)