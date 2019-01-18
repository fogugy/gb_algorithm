# Во втором массиве сохранить индексы четных элементов первого массива.

import random as rnd

list_src = [rnd.randint(0, 100) for x in range(10)]
list_evens_idx = []

for idx, nmb in enumerate(list_src):
    if nmb % 2 == 0:
        list_evens_idx.append(idx)

print('В массиве', list_src, 'четные элементы имеют индексы',
      list_evens_idx, sep="\n")
