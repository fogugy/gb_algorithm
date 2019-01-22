# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»

simples_test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197]


def is_simple(n):
    i = 2
    j = 0  # флаг

    while i**2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    return j != 1


def get_simple(n):
    """
    Эмпирические данные:
    https://pastenow.ru/2682bda90cc77b074ec4b011bc92f348
    """
    simples = []
    i = 2

    while len(simples) < n:
        if is_simple(i):
            simples.append(i)
        i += 1

    return simples[-1]

print(get_simple(60))

def test():
    method_res = get_simple(20)
    test_res = simples_test[19]

    print('Test passed' if method_res == test_res else 'Test failed')


def test_performance():
    from timeit import timeit

    def test_iteration(n):
        res = timeit(f'get_simple({n})', number=100,
                     setup='from __main__ import get_simple')
        print('N=', n, 'time=', res/100)

    for x in [2**i for i in range(4)]:
        test_iteration(x)


if __name__ == '__main__':
    test()
    test_performance()
