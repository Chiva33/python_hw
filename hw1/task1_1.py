""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет """

dayNum = int(input('Введите номер дня:'))
if(dayNum in range(1, 8)):
    if(dayNum == 6 or dayNum == 7):
        print('Сегодня выходной!')
    else:
        print('Сегодня рабочий день!')
else:
    print('В неделе 7 дней!')
