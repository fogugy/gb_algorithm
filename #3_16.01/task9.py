# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random as rnd

h, w = 5, 3
mtrx = [[0 for j in range(w)] for i in range(h)]

for i in range(h):
    for j in range(w):
        mtrx[i][j] = rnd.randint(0, 5)

mins = [min([mtrx[i][j] for i in range(h)]) for j in range(w)]

print('матрица: ')
for x in mtrx:
    print(*x, sep='\t')

print('минимумы по столбцам: ')
print(*mins, sep='\t')

print(f'максимум из них: {max(mins)}')