# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


def rec_sum(counter: int, nmb: float = 1, sum: float = 0) -> float:
    if(counter > 0):
        next_nmb = -nmb / 2
        return rec_sum(counter - 1, next_nmb, sum+nmb)
    else:
        return sum


print(rec_sum(4))
