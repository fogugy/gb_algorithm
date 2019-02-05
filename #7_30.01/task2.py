# Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


import random as rn


def sort_merge(ls: list) -> list:
    if len(ls) > 1:
        mid = len(ls)//2
        lefthalf = ls[:mid]
        righthalf = ls[mid:]

        sort_merge(lefthalf)
        sort_merge(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                ls[k] = lefthalf[i]
                i = i+1
            else:
                ls[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            ls[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            ls[k] = righthalf[j]
            j = j+1
            k = k+1

    return ls


ls = [rn.random()*50 for x in range(6)]
print(ls, '->')
print(sort_merge(ls))
