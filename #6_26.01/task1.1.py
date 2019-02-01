# Подсчитать, сколько было выделено памяти под переменные в 
# ранее разработанных программах в рамках первых трех уроков. 
# Проанализировать результат и определить программы с 
# наиболее эффективным использованием памяти.

# Для сравнения взял программу вычисления n-го простого числа

from memory_profiler import profile

def is_simple(n):
    i = 2
    j = 0  # флаг

    while i**2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    return j != 1

@profile
def get_simple(n):
    simples = []
    i = 2

    while len(simples) < n:
        if is_simple(i):
            simples.append(i)
        i += 1

    return simples[-1]

get_simple(5)

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     20     14.5 MiB     14.5 MiB   @profile
#     21                             def get_simple(n):
#     22     14.5 MiB      0.0 MiB       simples = []
#     23     14.5 MiB      0.0 MiB       i = 2
#     24
#     25     14.5 MiB      0.0 MiB       while len(simples) < n:
#     26     14.5 MiB      0.0 MiB           if is_simple(i):
#     27     14.5 MiB      0.0 MiB               simples.append(i)
#     28     14.5 MiB      0.0 MiB           i += 1
#     29
#     30     14.5 MiB      0.0 MiB       return simples[-1]