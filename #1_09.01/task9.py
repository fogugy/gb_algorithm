# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

input_str = input('Введите 3 целых через пробел: ')

numbers = tuple(map(int, input_str.split(' ')))

set_d = set(numbers)

if len(set_d) == 3:
    set_d.remove(max(set_d))
    set_d.remove(min(set_d))
    print("среднее значение это %s" % set_d.pop())
else:
    print("слишком мало уникальных значений")
