# Задана натуральная степень n. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени 
# пример записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0




from random import randint, random


n = int(input('Введите n:'))

i = 0

list = [str(randint(0, 100)) + 'x^' + str(n) + ' + ' for n in range(n, -1, -1)]

print(list)