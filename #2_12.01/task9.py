# Среди натуральных чисел, которые были введены, найти
# наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

numbers = input('Введите натуральные числе через пробел: ').split(' ')

max_sum = 0
nmb_res = 0

for nmb in numbers:
    dig_sum = sum(map(int, nmb.replace('.', '')))

    if dig_sum > max_sum:
        max_sum = dig_sum
        nmb_res = float(nmb)

print(f'Наибольшая сумма цифр у числа {nmb_res}')
