# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# lines = 'пример абв слова абв которое нужно удалить абв'
# print(lines)
# lines = lines.replace('абв', '')
# print(lines)



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
src = 'пример следующий пример абв слова абв которое абв повторяются сжимаем пример'
print('Строка :' + src)

pack = ''
i = 0
while i < len(src):
    ln = 9
    found = False
    while not found and ln > 3:
        j = i - ln
        while j >= 0 and (i-j) < 100:
            if src[i:i+ln] == src[j:j+ln]:
                pack += '#%1d%2d' % (ln, (i - j))
                i += ln
                found = True
                break
            j -= 1
        ln -= 1
    if not found:
        pack += src[i]
        i += 1

print('Сжатая строка: ' + pack)

unpack = ''
i = 0
while i < len(pack):
    if pack[i] != '#':
        unpack += pack[i]
        i += 1
        continue
    ln = int(pack[i + 1: i + 2])
    dist = int(pack[i + 2: i + 4])
    unpack += unpack[-dist: -dist+ln]
    i += 4

print('Распакованная сторока: ' + unpack)
if src != unpack:
    print('Ошибка!')