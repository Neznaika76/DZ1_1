# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# lines = 'пример абв слова абв которое нужно удалить абв'
# print(lines)
# lines = lines.replace('абв', '')
# print(lines)

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
import random


def rnd_turn():  # Функция определения первого хода
    print(f'Выбор очередности ходов: ')
    print(f'Введите 0, если ходить первым будет Вы')
    print(f'Введите 1, если ходить первым будет компьютер')
    print(f'Введите 2, чтобы выбрать очередность ходов случайным образом')
    while True:
        n = input('> ')
        if n.isdigit():
            n = int(n)
            if n > 2 or n < 0:
                print(f'Введите число 0, 1 или 2')
            else:
                if n == 2:
                    n = random.randint(0, 1)
                if n == 0:
                    print(f'Первым будет ходить игрок!')
                else:
                    print(f'Первым будет ходить компьютер!')
                break
        else:
            print(f'Вы ввели недопустимый символ. Введите число 0, 1 или 2')
            continue
    return n


def turn_player(matches):
    n = 29
    while n > 28 or n < 1:
        n = input('Сколько вы возьмете конфет? ')
        if n.isdigit():
            # n = int(n)
            if int(n) > 28 or int(n) < 1:
                print(f'Вы вязли недопустимое количество конфет! Возьмите от 1 до 28-и')
                continue
            # проверка на остаток
            if int(n) > matches:
                print(f'Вы взяли больше чем осталось конфет!')
                # n = 28
                continue
        else:
            print(f'Вы ввели недопустимые символы. Введите число от 1 до 28-и')
            # n = 28
            continue
        n = int(n)
    return n


def turn_ai(matches):  # Ход компьютера
    n = matches % 28
if n == 0:
        n = random.randint(1, 28)
    return n


matches = 2021
count = 1
turn = rnd_turn()
while True:
    print(f'\n******** Ход номер: {count} ********')
    if turn % 2 == 0:
        print(f'Ход игрока! Всего конфет: {matches}')
        n = turn_player(matches)
        print(f'Игрок взял {n} конфет.')
    elif turn % 2 == 1:
        print(f'Ход компьютера! Всего конфет: {matches}')
        n = turn_ai(matches)
        print(f'Компьютер взял {n} конфет')
    matches -= n
    if matches == 0:
        if turn % 2 == 0:
            print(f'Победил игрок!')
        else:
            print(f'Победил компьютер!')
        break
    turn += 1
    count += 1
# Создайте программу для игры в ""Крестики-нолики"".
#
# board = list(range(1, 10))
# wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
#
#
# def draw_board():
#     print('-------------')
#     for i in range(3):
#         print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
#     print('-------------')
#
#
# def take_input(playar_token):
#     while True:
#         value = input('Куда поставить: ' + playar_token + '?  ')
#         if not (value in '123456789'):
#             print('Неверный ввод. Попробуйте еще раз.')
#             continue
#         value = int(value)
#         if str(board[value - 1]) in 'XO':
#             print('Позиция уже занята')
#             continue
#         board[value - 1] = playar_token
#         break
#
#
# def check_win():
#     for each in wins_coord:
#         if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
#             return board[each[1] - 1]
#     else:
#         return False
#
#
# def main():
#     counter = 0
#     while True:
#         draw_board()
#         if counter % 2 == 0:
#             take_input('X')
#         else:
#             take_input('O')
#         if counter > 3:
#             winner = check_win()
#             if winner:
#                 draw_board()
#                 print(winner, "выйграл!")
#                 break
#         counter += 1
#         if counter > 8:
#             draw_board()
#             print('Ничья!')
#             break
#
#
# main()

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# src = 'пример следующий пример абв слова абв которое абв повторяются сжимаем пример'
# print('Строка :' + src)
#
# pack = ''
# i = 0
# while i < len(src):
#     ln = 9
#     found = False
#     while not found and ln > 3:
#         j = i - ln
#         while j >= 0 and (i-j) < 100:
#             if src[i:i+ln] == src[j:j+ln]:
#                 pack += '#%1d%2d' % (ln, (i - j))
#                 i += ln
#                 found = True
#                 break
#             j -= 1
#         ln -= 1
#     if not found:
#         pack += src[i]
#         i += 1
#
# print('Сжатая строка: ' + pack)
#
# unpack = ''
# i = 0
# while i < len(pack):
#     if pack[i] != '#':
#         unpack += pack[i]
#         i += 1
#         continue
#     ln = int(pack[i + 1: i + 2])
#     dist = int(pack[i + 2: i + 4])
#     unpack += unpack[-dist: -dist+ln]
#     i += 4
#
# print('Распакованная сторока: ' + unpack)
# if src != unpack:
#     print('Ошибка!')
