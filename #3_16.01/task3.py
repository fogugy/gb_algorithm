# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random as rnd

ls = [rnd.randint(0, 100) for x in range(10)]

max_nmb = ls[0]
min_nmb = ls[0]
max_idx = 0
min_idx = 0

print(ls)

for idx, nmb in enumerate(ls):
    if nmb > max_nmb:
        max_nmb = nmb
        max_idx = idx
    elif nmb < min_nmb:
        min_nmb = nmb
        min_idx = idx

print("max:", max_nmb, "min:", min_nmb)

ls[min_idx], ls[max_idx] = ls[max_idx], ls[min_idx]

print(ls)
