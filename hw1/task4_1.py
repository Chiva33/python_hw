""" Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y). """

quarter = int(input('Введите номер четверти:'))
if (quarter == 1):
    print('х > 0; y > 0')
elif (quarter == 2):
    print('х < 0; y > 0')
elif (quarter == 3):
    print('х < 0; y < 0')
elif (quarter == 4):
    print('х > 0; y < 0')
elif (quarter < 1 or quarter > 4):
    print('Введите четверть от 1 до 4')
    