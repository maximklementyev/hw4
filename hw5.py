from functools import reduce
def func(prev_el, el):
    return prev_el * el
data = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(func, data))
