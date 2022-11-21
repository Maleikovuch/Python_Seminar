# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


print('Введите номер четверти: ')
x = int(input())


if x == 1 and (0 < x < 5):
    print(f'Диапазон возможных координат точек в этой четверти:( X;Y)')
elif x == 2:
    print(f'Диапазон возможных координат точек в этой четверти:(-X;Y)')
elif x == 3:
    print(f'Диапазон возможных координат точек в этой четверти:(-X;-Y)')
elif x == 4:
    print(f'Диапазон возможных координат точек в этой четверти:(X;-Y)')
else:
    print(f'Такой четверти нет')