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

# import random
# import math
#
#
# def add_elements():
#     for _ in range(n):
#         elements.append(random.randint(1, 20))
#     print(elements)
#
#
# def product_elements(elements) -> list:
#     elements_product = []
#     i = 0
#     while i < (math.ceil(len(elements) / 2)):
#         elements_product.append(elements[i] * elements[(i + 1) * (-1)])
#         i += 1
#     return elements_product
#
#
# n = int(input('Введите число: '))
# n = abs(n)
# elements = []
# add_elements()
# print(product_elements(elements))
#
# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import math


def add_elements(n):    # Функци создает список размером n
    elements_add = []

    for _ in range(n):
        elements_add.append(format(random.uniform(1, 20), '.2f'))
    print(elements_add)
    return elements_add


def transformation_elements(transformation_elements):   # функция выводит список только двух чисел после замятой
    for i in range(len(transformation_elements)):
        transformation_elements[i] = int(float(transformation_elements[i]) * 100) % 100
    print(transformation_elements)
    return transformation_elements


def max_min_elements(max_min_elements): # Функция находит разницу между максимальной и минимальной дробной частью
    max = max_min_elements[0]
    min = max_min_elements[0]
    for i in range(len(max_min_elements)):
        if max_min_elements[i] > max:
            max = max_min_elements[i]
        elif max_min_elements[i] < min:
            min = max_min_elements[i]
    print(f'Разница между максимальной и минимальной доробной части равна 0.{max - min}')



n = int(input('Введите число: '))
n = abs(n)
max_min_elements(transformation_elements(add_elements(n)))
