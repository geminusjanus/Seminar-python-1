# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

numX_A = int(input('Enter the X coordinate of point A '))
numY_A = int(input('enter the Y coordinate of point A '))
numX_B = int(input('enter the X coordinate of point B '))
numY_B = int(input('enter the Y coordinate of point B '))

distance = 0

distance = ((numX_B - numX_A) ** 2 + (numY_B - numY_A) ** 2) ** (0.5)
print(round(distance, 2))