# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

x = int(input('Введите число:'))
print('Ответ:',bin(x).replace('0b',''))