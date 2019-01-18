# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random as rnd

ls = [rnd.randint(-10, 10) for x in range(10)]

max_neg = float('-inf')
max_neg_idx = -1

for idx, num in enumerate(ls):
    if num < 0 and num > max_neg:
        max_neg = num
        max_neg_idx = idx

print(ls)
print(f'Макс отрицательное: {max_neg}, с индексом: {max_neg_idx}')
