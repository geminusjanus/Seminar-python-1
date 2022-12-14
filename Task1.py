# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

user_num = int(input('Введите номер дня недели и программа проверит выходной это или нет '))
if user_num == 1:
    print(f'{user_num} -> нет')
if user_num == 2:
    print(f'{user_num} -> нет')
if user_num == 3:
    print(f'{user_num} -> нет')
if user_num == 4:
    print(f'{user_num} -> нет')
if user_num == 5:
    print(f'{user_num} -> нет')
if user_num == 6:
    print(f'{user_num} -> да')
if user_num == 7:
    print(f'{user_num} -> да')
if user_num > 7:
    print('Такого дня нет')