# Задана натуральная степень n. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени 
# пример записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0


from dataclasses import replace
from functools import reduce
from random import randint, random


n = int(input('Введите n:'))



def get_res(n):
    list = [str(randint(0, 100)) + 'x^' + str(n) + ' + ' for n in range(n, -1, -1)]
    list_str = reduce(lambda x, y: x + y, list)
    list_str = list_str.replace("x^0", "")
    return list_str[: -3] + ' = 0'

print(get_res(n))
result = get_res(n)

with open('get_res2.txt', 'w') as data:
    data.write(result)