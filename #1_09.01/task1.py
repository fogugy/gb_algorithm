# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

from functools import reduce

input_str = input('Введите целое 3х значное число: ')
x = int(input_str)

if 99 < x <= 999:
    digits = []

    for i in range(3):
        digit = x % 10
        x //= 10
        digits.append(digit)

    x_sum = sum(digits)
    x_mult = reduce(lambda x, y: x*y, digits)

    print(f'Произведение цифр числа {input_str} равно {x_mult}')
    print(f'Сумма цифр числа {input_str} равно {x_sum}')

else:
    print('Число должно быть трехзначным')
