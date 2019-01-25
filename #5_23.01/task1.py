# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа
# должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple as ntuple

Record = ntuple('Record', ['name', 'income'])

# Префабы компаний
c1 = Record("П. Шуйлер и сыновья", [15, 13, 10, 16])
c2 = Record("Umbrella", [16, 20, 4, 1])
c3 = Record("Камино", [4, 4, 4, 31])
sheet = [c1, c2, c3]

# comp_count = int(input('Введите кол-во предприятий: '))
# sheet = []

# for i in range(comp_count):
#     input_str = input('Введите название предприятия и доход за 4 квартала: ').split()
#     comp_name = ' '.join(input_str[:-4])
#     comp_income = list(map(float, input_str[-4:]))
#     sheet.append(Record(comp_name, comp_income))

medial = sum([sum(x.income) for x in sheet])/len(sheet)

print('Средняя прибыль за год для всех предприятий:', medial)
print('Выше/равна среднего прибыль у компаний:')
for x in filter(lambda x: sum(x.income) >= medial, sheet):
    print('\t', x.name)
print('Ниже среднего прибыль у компаний:')
for x in filter(lambda x: sum(x.income) < medial, sheet):
    print('\t', x.name)