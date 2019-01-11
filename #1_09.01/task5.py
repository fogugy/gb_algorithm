# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

import string

rng = tuple(input('Введите диапазон букв через пробел: ').split(' '))

chars = string.ascii_lowercase
c1 = rng[0].lower()
c2 = rng[1].lower()
c1_idx = chars.index(c1)
c2_idx = chars.index(c2)

let_count = max(c1_idx, c2_idx) - min(c1_idx, c2_idx) - 1

print("Введенные буквы находятся на позициях %d и %d" % (c1_idx + 1, c2_idx + 1), \
      "Между ними находятся %d букв" % let_count)
