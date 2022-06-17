# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


list1 = []
for i in range(0, 10):
    list1.append(randint(0, 10))
print(list1)

list2 = []
print(len(list1))

e = 0
print(list1.count(e))
for f in list1:
    if list1.count(e) >= 2:
        list1.pop(e)
    else:
        list2.append(list1[e])
        



print(list2)
