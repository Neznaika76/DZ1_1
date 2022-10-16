# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
# n = int(input("Введите число: "))
# elements = []
# for _ in range(n):
#     elements.append(random.randint(0, 99))
# print(elements)
#
# s = 0
# i = 1
# while i < len(elements):
#     s += elements[i]
#     i += 2
# print(f'Сумма нечетных элементов равна {s}')
#
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
import math


def add_elements():
    for _ in range(n):
        elements.append(random.randint(1, 20))
    print(elements)


def product_elements(elements) -> list:
    elements_product = []
    i = 0
    while i < (math.ceil(len(elements) / 2)):
        elements_product.append(elements[i] * elements[(i + 1) * (-1)])
        i += 1
    return elements_product


n = int(input('Введите число: '))
n = abs(n)
elements = []
add_elements()
print(product_elements(elements))
