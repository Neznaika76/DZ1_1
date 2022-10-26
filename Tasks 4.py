
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# def transformation_elements(x, y):
#     m = int(x)
#     z = int(float(x) * (10**y)) % (10**y)
#     z = m + z/(10**y)
#     return z
#
#
# n = float(input('Введите число: '))
# d = int(input('Введите точность d: '))
# if n > 0:
#     print(transformation_elements(n, d))
# else:
#     n = abs(n)
#     print(transformation_elements(n, d)*(-1))
#
#
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def multipliers(n):
   i = 2
   multiplier = []
   while i * i <= n:
       while n % i == 0:
           multiplier.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       multiplier.append(n)
   return multiplier

n = int(input('Введите число: '))
print(multipliers(n))

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# import random
#
#
# def add_elements(x):
#     for _ in range(x):
#         elements.append(random.randint(1, 20))
#     print(elements)
#
#
# n = int(input('Введите число: '))
# elements = []
# add_elements(n)
# new_elements = [elements[0]]
# for i in range(len(elements)):
#     coincidence = 0
#     for j in range(len(new_elements)):
#         if elements[i] == new_elements[j]:
#             coincidence = 1
#     if coincidence == 0:
#         new_elements.append(elements[i])
# print(new_elements)
#
#
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
#
#
# def add_elements(x):
#     for _ in range(x):
#         elements.append(random.randint(0, 20))
#     print(elements)
#
#
# n = int(input('Введите число: '))
# elements = []
# add_elements(n)
#
# path = 'file.txt'
# data = open(path, 'w')
# for i in range(n):
#     if i == n-1 and elements[i] != 0:
#         # print(f'{elements[i]}')
#         data.writelines(f'{elements[i]}')
#     elif elements[i] != 0:
#         data.writelines(f'{elements[i]}x{n-1-i} + ')
#         # print(f'{elements[i]}x{n-1-i} +')
#     i+= 1
#
# data.close()
#
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# import random
# import re
#
#
# def add_elements(elements, x):
#     for _ in range(x):
#         elements.append(random.randint(0, 20))
#     # print(elements)
#
#
# n = int(input('Введите число: '))
# elements1 = []
# elements2 = []
# add_elements(elements1, n)
# add_elements(elements2, n)
#
# path = 'file1.txt'
# data = open(path, 'w')
# for i in range(n):
#     if i == n-1 and elements1[i] != 0:
#         data.writelines(f'{elements1[i]}')
#     elif elements1[i] != 0:
#         data.writelines(f'{elements1[i]}x{n-1-i}+')
#     i+= 1
# data.close()
#
# path = 'file2.txt'
# data = open(path, 'w')
# for i in range(n):
#     if i == n-1 and elements2[i] != 0:
#         data.writelines(f'{elements2[i]}')
#     elif elements2[i] != 0:
#         data.writelines(f'{elements2[i]}x{n-1-i}+')
#     i+= 1
# data.close()
#
# elements_new1 = []
# path = 'file1.txt'
# data = open(path, 'r')
# elements_new1 = data.read()
# # print(elements_new1)
# data.close()
# elements_new1 = re.findall('\d+', elements_new1)
#
# elements_new2 = []
# path = 'file2.txt'
# data = open(path, 'r')
# elements_new2 = data.read()
# # print(elements_new2)
# data.close()
# elements_new2 = re.findall('\d+', elements_new2)
#
# print("Полученный многочлен записан в файл 'file3.txt'")
#
# path = 'file3.txt'
# data = open(path, 'w')
# j = 0
# for i in range(0, len(elements_new1), 2):
#     if i == len(elements_new1)-1 and elements_new1[i] != 0:
#         data.writelines(f'{elements_new1[i]}')
#     elif elements_new1[i] != 0:
#         data.writelines(f'{int(elements_new1[i])+int(elements_new2[i])}x{len(elements_new1)//2-j} + ')
#         j += 1
# data.close()
