# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

"""

fruits = ['яблоко', 'банан', 'киви', 'арбуз']
print('Было:')
print(fruits)
print()
print('Стало:')
for i in range(0, len(fruits)):
    print('{} {: >10}'.format(str(i+1) + '.', fruits[i]))

"""

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

"""

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'конь', 'телескоп']
list2 = [7, 74, 535, 5, 67, 8, 74, 'конь', 733, 3, 9, 65, 5, 353, 1, 4688, 0]

print('Список №1:')
print(list1)
print()
print('Список №2:')
print(list2)
print()

for i in range(0, len(list2)):
    j = 0
    while j < len(list1):
        if list1[j] == list2[i]:
            list1.pop(j)
        j += 1

print('Список №1 после удаления элементов, присутствующие в списке №2:')
print(list1)

"""

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4,
# если не кратен, то умножить на два.

"""

numbers = [43, 534, 88, 386, 46, 775, 979, 742, 115, 87]
newnumbers = []

print('Список из целых чисел:')
print(numbers)
print()

for i in range(0, len(numbers)):
    if numbers[i]%2 == 0:
        numbers[i] = numbers[i] / 4
        newnumbers.append(numbers[i])
    else:
        numbers[i] = numbers[i] * 2
        newnumbers.append(numbers[i])

print('Новый список чисел:')
print(newnumbers)

"""