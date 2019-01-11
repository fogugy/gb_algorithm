# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

import string
import random as rnd

action = input("Введите желаемый тип данных:\
                \ni: целое\
                \nf: вещественное\
                \nl: буква\n")

if action in ['i', 'f', 'l']:

    rng = tuple(input('Введите диапазон через пробел: ').split(' '))
    result = None

    if action == 'l':
        chars = string.ascii_lowercase
        from_char = rng[0].lower()
        to_char = rng[1].lower()
        from_idx = chars.index(from_char)
        to_idx = chars.index(to_char)
        res_idx = rnd.randint(from_idx, to_idx)
        result = chars[res_idx]

    elif action == 'f':
        fr = float(rng[0])
        to = float(rng[1])
        result = rnd.uniform(fr, to)

    else:
        fr = int(rng[0])
        to = int(rng[1])
        result = rnd.randint(fr, to)

    print(result)

else:
    print("Неизвестный тип данных %s" % action)
