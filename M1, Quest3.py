digit1 = float(input('Введите число для оценки: '))
digit2 = float(input('Введите число для оценки: '))
if digit1 > digit2:
    print('Это самое большое число:', digit1)
elif digit2 > digit1:
    print('Это самое большое число:', digit2)
else:
    print('Данные числа ровны!')  # Первый вариант


digit3 = float(input('Введите число для оценки:'))
digit4 = float(input('Введите число для оценки:'))
Max = (digit3 >= digit4) * digit3 or (digit4 >= digit3) * digit4
print(Max)  # Второй вариант


