# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random as rnd

ls = [rnd.randint(0, 10) for x in range(10)]

max_nmb = ls[0]
min_nmb = ls[0]
max_idx = 0
min_idx = 0

for idx, nmb in enumerate(ls):
    if nmb >= max_nmb:
        max_nmb = nmb
        max_idx = idx
    elif nmb < min_nmb:
        min_nmb = nmb
        min_idx = idx

sublist = ls[min(min_idx, max_idx) + 1: max(min_idx, max_idx)]
print(ls)
print('->')
print(sublist)
print(sum(sublist))
