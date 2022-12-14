# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

import sys

numX = int(input('Enter X coordinate '))
if numX == 0:
    sys.exit('The coordinate must not be zero')
numY = int(input('Enter Y coordinate '))
if numY == 0:
    sys.exit('The coordinate must not be zero')

quarter = 0
if numX > 0 and numY > 0:
    quarter = 1
elif numX < 0 and numY > 0:
    quarter = 2
elif numX < 0 and numY < 0:
    quarter = 3
elif numX > 0 and numY < 0:
    quarter = 4

print(f'Точка находится в {quarter} плоскости')