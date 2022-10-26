# # 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# text = input('Введите текст: ')
# text = text.split()  # разделяет текст по пробелам
# new_text = ''
# for i in text:
#     if 'абв' not in i:
#         new_text += i + ' '
# print(new_text)
#
# # 2. Создайте программу для игры с конфетами человек против человека.
# # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# # Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# # Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# # чтобы забрать все конфеты у своего конкурента?
# print('Взял решение из интернета, после разбора полета понял, что все не так уж сложно оказалось')
# from random import randint
#
#
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
#
#
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
#
#
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")
#
# # а
# print('Просто добавил боту рандом')
#
#
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
#
#
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
#
#
# player1 = input("Введите имя первого игрока: ")
# player2 = 'BOT'
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = randint(1, 29)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")
#

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt) - 1):
#         if txt[i] == txt[i + 1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt) - 2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res
#
#
# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res
#
#
# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")

def Compression(text):  # алгоритм сжатия
    compresdata = ''

    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        compresdata += str(count) + text[i]
        i += 1

    return compresdata


def Recovery(text):  # алгоритм восстановления
    datarecovery = ''

    i = 0
    while i < len(text):
        datarecovery += str(text[i + 1]) * int(text[i])
        i += 2

    return datarecovery


with open('Input.txt', 'r') as t1:
    t1 = t1.read()

with open('Output.txt', 'w+') as t2:
    t2.write(Compression(t1))
    t2.seek(0)  # возврат курсора на начало строки
    t2 = t2.read()

with open('Recovery.txt', 'w') as t3:
    t3.write(Recovery(t2))
