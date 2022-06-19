# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

list1 = []
for i in range(0, 10):
    list1.append(randint(0, 10))
print(list1)

list2 = []
[list2.append(i) for i in list1 if i not in list2]
print(list2)
