# Определить, какое число в массиве встречается чаще всего.

import random as rnd

ls = [rnd.randint(0, 10) for x in range(10)]
dct = dict()

for nmb in ls:
    dct[nmb] = dct.get(nmb, 0) + 1

print(ls)

print('число кол-во')
for k, v in dct.items():
    print(k, v, sep='\t')
