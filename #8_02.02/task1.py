# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

# Выбрал реализацию поиска подстроки алгоритмом Рабина—Карпа

def rabin_karp(src: str, query: str):
    n = len(src)
    m = len(query)
    hquery = hash(query)
    hsrc = hash(src[1:m])
    indexes = []
    for i in range(n-m+1):
        if hquery == hsrc:
            if src[i:i+m] == query:
                indexes.append(i)
        hsrc = hash(src[i+1:i+m+1])
    return indexes if len(indexes) > 0 else -1


src = 'abcdefghijklmdefnopqrstuvwxwzdef'

print(rabin_karp(src, 'def'))
print(rabin_karp(src, 'zzz'))
