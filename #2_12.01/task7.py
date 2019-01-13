# Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.


def rec_sum(counter: int, nmb: float = 1, sum: float = 0) -> float:
    if(counter > 0):
        next_nmb = nmb + 1
        return rec_sum(counter - 1, next_nmb, sum+nmb)
    else:
        return sum


n = int(input('Введите n: '))

rec_res = rec_sum(n)
eq_res = n * (n+1)/2

print(f'Сумма ряда для n={n} равняется {rec_res}')
print(f'n(n+1)/2 для n={n} равняется {eq_res}')
print('Теорема доказана' if rec_res == eq_res else 'Теорема опровергнута')