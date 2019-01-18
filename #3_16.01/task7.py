# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random as rnd

ls = [rnd.randint(0, 10) for x in range(10)]

min1 = float('inf')
min2 = float('inf')

for x in ls:
    if x < min1:
        min1 = x
        continue
    elif x < min2:
        min2 = x

print(ls)
print([min1, min2])