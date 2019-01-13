# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import re

input_str = input('Введите число, а я посчитаю: ')

odd_re = re.compile(r'[13579]')
even_re = re.compile(r'[02468]')

odd_res = re.findall(odd_re, input_str)
even_res = re.findall(even_re, input_str)

print('Четных чисел %d:' % len(even_res), ', '.join(even_res))
print('Нечетных чисел %d:' % len(odd_res), ', '.join(odd_res))
