# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

pos = int(input('Введите позицию в алфавите(анг): '))

chars = string.ascii_lowercase

if 1 <= pos <= len(chars):
    print("На %d позиции находится буква '%s'" % (pos, chars[pos - 1]))
else:
    print("В алфавите нет такой позиции")
