# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого
# это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import re


class Hexadec:
    def __init__(self, inp: str):
        ptrn = re.compile('[A-Fa-f0-9]+')
        if re.match(ptrn, inp) == None:
            raise ValueError(f'Недопустимое значение числа {inp}')
        self._numbers = [*inp.upper()]

    @property
    def numbers(self):
        return self._numbers

    def __add__(self, other: 'Hexadec') -> 'Hexadec':
        h1 = int(str(self), 16)
        h2 = int(str(other), 16)
        res = hex(h1 + h2)
        return Hexadec(str(res)[2:])

    def __mul__(self, other: 'Hexadec') -> 'Hexadec':
        h1 = int(str(self), 16)
        h2 = int(str(other), 16)
        res = hex(h1 * h2)
        return Hexadec(str(res)[2:])

    def __str__(self):
        return ''.join(self.numbers)


h1 = Hexadec('A2')
h2 = Hexadec('C4F')
print('Operation test for ', h1, h2)
print('+', h1+h2)
print('*', h1*h2)

ih1, ih2 = input('Введите 2 16тиричных числа: ').split()
h11 = Hexadec(ih1)
h21 = Hexadec(ih2)
print('For ', h11, h21)
print('+', h11+h21)
print('*', h11*h21)
