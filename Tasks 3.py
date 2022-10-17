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

#
# def add_elements(n):    # Функци создает список размером n
#     elements_add = []
#
#     for _ in range(n):
#         elements_add.append(format(random.uniform(1, 20), '.2f'))
#     print(elements_add)
#     return elements_add
#
#
# def transformation_elements(transformation_elements):   # функция выводит список только двух чисел после замятой
#     for i in range(len(transformation_elements)):
#         transformation_elements[i] = int(float(transformation_elements[i]) * 100) % 100
#     print(transformation_elements)
#     return transformation_elements
#
#
# def max_min_elements(max_min_elements): # Функция находит разницу между максимальной и минимальной дробной частью
#     max = max_min_elements[0]
#     min = max_min_elements[0]
#     for i in range(len(max_min_elements)):
#         if max_min_elements[i] > max:
#             max = max_min_elements[i]
#         elif max_min_elements[i] < min:
#             min = max_min_elements[i]
#     print(f'Разница между максимальной и минимальной доробной части равна 0.{max - min}')
#
#
#
# n = int(input('Введите число: '))
# n = abs(n)
# max_min_elements(transformation_elements(add_elements(n)))
#
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
#
# def binary_elements(n): # Функция записывает в стоку остаток от деления на 2
#     elements = []
#     while n // 2 > 0:
#         elements.append(int(n % 2))
#         n = n // 2
#     elements.append(int(n % 2))
#     return elements
#
#
# def replacement_elements(elements): # Функция меняет местами элементы строки
#     i = 0
#     while i < (math.ceil(len(elements) / 2)):
#         elements[i], elements[(i + 1) * (-1)] = elements[(i + 1) * (-1)], elements[i]
#         i += 1
#     return elements
#
#
# def output_elements(elements): # Функция выводит элементы строки
#     for i in range(len(elements)):
#         print(elements[i], end='')
#
#
# n = int(input('Введите число: '))
# n = abs(n)
#
# output_elements(replacement_elements(binary_elements(n)))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.
#
# def fibonachchy(n): # Функция находит положительные числа Фибоначчи
#     f1 = 0
#     f2 = 1
#     elements = []
#     for _ in range(n):
#         elements.append(int(f2))
#         f1 = f1 + f2
#         f1, f2 = f2, f1
#     return elements
#
#
# def fibonachchy_elements(elements): # Функция составляет список для отрицательных и положительных индексов чисел Фибоначи
#     fib_elements = []
#     for i in range(len(elements)):
#         if i % 2 != 0:
#             fib_elements.append(int(elements[-(i+1)]))
#         else:
#             fib_elements.append(int(elements[-(i+1)]*(-1)))
#     fib_elements.append(int(0))
#     for i in range(len(elements)):
#         fib_elements.append(int(elements[i]))
#     return fib_elements
#
#
# n = int(input('Введите число: '))
# n = abs(n)
# print(fibonachchy_elements(fibonachchy(n)))


# Написать программу, которая группирует слова по «общим буквам»
# n = int(input('Введите число: '))


def find(elements, n): # Функция находит все слова с одинаковыми буквами и выводт доплнительный список в котором записаны на местах совпадения символо 1, на местах не совпадения символов 0
    str_mask = []
    for _ in range(len(elements)):
        str_mask.append(' ')
    while elements[n] != ' ':
        for j in range(len(elements)):
            if elements[n] == elements[j]:
                str_mask[j] = 1
            else:
                if str_mask[j] != 1 and elements[j] != ' ':
                    str_mask[j] = 0
        n += 1
        # print(n, end='')
        if n >= len(elements):
            break
    return str_mask


def proizvedenie(elements, x, y): # Функция выводит значение 1, если все символы слова совпадают, и значение 0 если хотя бы один символ не совпадает
    s = 1
    while x <= y:
        s = s * int(elements[x])
        x += 1
    return s


def zamena(elements1, elements2, x, y): # Функия сортирует элементы с одинаковыми символами
    for z in range((len(elements2) // y)):
        p1 = x + y * z
        p2 = p1 + y - 2
        elements1 = list(elements1)
        if p1+y < len(elements2):
            if proizvedenie(elements2, p1, p2) != 1 and proizvedenie(elements2, p1 + y, p2 + y) == 1:
                for q in range(y-1):
                    elements2[p1 + q], elements2[p1 + y + q] = elements2[p1 + y + q], elements2[p1 + q]
                    elements1[p1 + q], elements1[p1 + y + q] = elements1[p1 + y + q], elements1[p1 + q]
    return elements1


def poisk(elements2, y): # Функия находит первую позицию элемента, который еще не отсортирован
    position1 = 0
    for z in range((len(elements2) // y)):
        p1 = y * z
        p2 = p1 + y - 2
        if p1 < len(elements2):
            if proizvedenie(elements2, p1, p2) == 1 and proizvedenie(elements2, p1 + y, p2 + y) != 1:
                if position1 == 0:
                    position1 = p1 + y # Следующая позиция знака
    return position1


str1 = input("Введите слова через пробел : ")
str2 = []
i = 0
k = i # Позиция символа
while i + k < len(str1):
    str2 = find(str1, i)
    k = i
    j = 0
    while str1[i] != ' ': # Проходим первое слово до пробела и определяем его длинну
        i += 1
        j += 1
        if i >= len(str1):
            break
    j += 1 # длинна слова
    i = poisk(str2, j)
    str1 = zamena(str1, str2, i, j)
print(str1)



