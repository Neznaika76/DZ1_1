# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
n = int(input("Введите число: "))
elements = []
for _ in range(n):
    elements.append(random.randint(0, 99))
print(elements)

s = 0
i = 1
while i < len(elements):
    s += elements[i]
    i += 2
print(f'Сумма нечетных элементов равна {s}')

