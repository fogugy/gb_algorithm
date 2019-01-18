# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

counter = 0

for nmb in range(2, 99):
    for divider in range(2, 9):
        if nmb % divider == 0:
            counter += 1
            break

print('В диапазоне [2, 99] таких чисел %d' % counter)
