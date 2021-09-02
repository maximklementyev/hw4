from sys import argv
script_name, hour, rate, bonus = argv
print("Имя скрипта: ", script_name)
print("Выработка в час: ", hour)
print("Ставка в час: ", rate)
print("Премия: ", bonus)
print("Зарплата: ", int(hour) * int(rate) + int(bonus))
