# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

import sys

user_num = int(input('Введите номер координатной плоскости '))
if user_num < 1 or user_num > 4:
    sys.exit('Такой плоскости нет')

if user_num == 1:
    print('Диапазон от [0,0] до [∞,∞]')
if user_num == 2:
    print('Диапазон от [0,0] до [-∞,∞]')
if user_num == 3:
    print('Диапазон от [0,0] до [-∞,-∞]')
if user_num == 4:
    print('Диапазон от [0,0] до [∞,-∞]')