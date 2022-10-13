# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# def sum(n, s):
#     if int(n/10) == 0:
#         s = s + n
#         print(s)
#         return
#     else:
#         s = s + n % 10
#         sum(int(n/10), s)
#
# x=float(input("Введите число: "))
# if x < 0:
#     x = x * (-1)
# while x % 10 != 0:
#     x = x*10
# else:
#     x = int(x / 10)
# sum(x, 0)

# Напишите программу, которая принимает на вход число N и выдает набор произведений
# чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# x = int(input("Введите число: "))
# x = abs(x)
# k = 1
# print("[",  end = ' ')
# for i in range(x-1):
#     k = (i+1) * k
#     print(k,  end = ',')
# k = k * x
# print(k,  end = ' ]')

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и
# выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# x = int(input("Введите число: "))
# elements = list()
# s = 0
# for i in range(abs(x)):
#     elements.append((1+1/(i+1))**(i+1))
#     s = s + elements[i]
# print("Сумма:",  end = ' ')
# print(s)

# Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

# import random
#
# x = int(input("Введите число больше 10: "))
# x = abs(x)
# elements = list()
# s = 1
# for i in range(x):
#     elements.append(random.randint((x*-1), x))
#     print(elements[i], end=' ')
# path = 'file.txt'
# data = open(path, 'r')
# text = data.read()
# data.close()
# data = open(path, 'r')
# print(len(text))
# for i in range(len(text)-1):
#     y = int(data.read(1))
#     s = s * elements[y]
# data.close()
# print("Сумма:",  end = ' ')
# print(s)

# Реализуйте алгоритм перемешивания списка.

# import random
#
# x = int(input("Введите число размера массива: "))
# x = abs(x)
# elements = list()
# for i in range(x):
#     elements.append(i)
#     print(elements[i], end=' ')
# i = len(elements)
# while i > 1:
#     i = i - 1
#     j = random.randrange(i)
#     elements[j], elements[i] = elements[i], elements[j]
# print()
# print("Перемешанный массив")
# for i in range(x):
#     print(elements[i], end=' ')

# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

elements1 = [1, 2, 3, 2, 0]
elements2 = [5, 1, 2, 7, 3, 2]
elements3 = list()
s = 0
for j in range(len(elements1)):
    for i in range(len(elements2)):
        if elements2[i]==elements1[j]:
            for k in range(j):
                if elements2[i]==elements3[k]:
                    s = 1
            if s != 1:
                elements3.append(elements2[i])
            else:
                s = 0
for j in range(len(elements3)):
    print(elements3[j], end=' ')



