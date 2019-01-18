# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

import random as rnd

h, w = 5, 4
mtrx = [[0 for x in range(w)] for y in range(h)]

values = input(f'Введите значения для матрицы {h}x{w}: \n').split()

next_idx = 0
for i in range(h):
    for j in range(w-1):
        # autofill
        mtrx[i][j] = float(values[next_idx])
        next_idx += 1

for i in range(h):
    mtrx[i][w-1] = sum(mtrx[i])

for x in mtrx:
    print(*x, sep='\t')
