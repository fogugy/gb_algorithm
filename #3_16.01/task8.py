# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

import random as rnd

w, h = 5, 4
mtrx = [[0 for x in range(w)] for y in range(h)]

values = input(f'Введите значения для матрицы {w}x{h}: \n').split()

for i in range(h):
    for j in range(w-1):
        # autofill
        # mtrx[i][j] = rnd.randint(0, 5)
        mtrx[i][j] = float(values[i+j])


for i in range(h):
    mtrx[i][w-1] = sum(mtrx[i])


for x in mtrx:
    for y in x:
        print(f'{y}\t', end='')
    print()
