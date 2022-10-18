# k = int(input())
# some_list = [0] * (k * 2 + 1)
# some_list[k + 1] = 1
# for idx in range(k + 2, k * 2 + 1):
#     some_list[idx] = some_list[idx - 1] + some_list[idx - 2]
# for idx in range(k, -1, -1):
#     some_list[idx] = some_list[idx + 2] - some_list[idx + 1]
# print(some_list)
# ________________________________________________________________

# from cmath import sqrt


# def find_solution(a, b, c):
#     d = b * b - 4 * a * c
#     if d < 0:
#         print('No solutions')
#     elif d == 0:
#         print(-b / (2 * a))
#     else:
#         list_ = []
#         list_.append((-b - d**0.5) / (2 * a))
#         list_.append((-b + d**0.5) / (2 * a))
#         print(list_)


# print('Input A, B, C for Ax^2 + Bx + C')
# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))

# find_solution(a, b, c)

# 1. Задайте строку из набора чисел.Напишите программу, которая покажет
# большее и меньшее число.В качестве символа - разделителя используйте пробел.

# some_str = input()
# some_str = some_str.split()
# maxx = int(some_str[0])
# minn = int(some_str[0])
# for i in some_str:
#     if int(i) > maxx:
#         maxx = int(i)
#     elif int(i) < minn:
#         minn = int(i)
# print(minn, maxx)

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#
# 1) с помощью математических формул нахождения корней квадратного уравнения

# a = float(input())
# b = float(input())
# c = float(input())
# d = b ** 2 - 4 * a * c
# if d < 0:
#     print('Действительных корней нет')
# elif d == 0:
#     print(-b / (2 * a))
# else:
#     print((-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a))

# 2) с помощью дополнительных библиотек Python

# import sympy as sm
# a = int(input())
# b = int(input())
# c = int(input())
# x = sm.Symbol('x')
# print(sm.solveset(a * x ** 2 + b * x + c, x))

# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

import sympy as sm
print(sm.lcm(int(input()), int(input())))