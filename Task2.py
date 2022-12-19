# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите первое число '))
y = int(input('Введите второе число '))
z = int(input('Введите третье число '))

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if not (x and y and z) == (not x) or (not y) or (not z):
                result = 'Утверждение истино'
            else:
                result = 'Утверждение ложно'
print(result)