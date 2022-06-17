# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N

number = int(input('Введите число:'))
list = []
i = 2

for e in range(i, number):
    if number % i == 0:
        list.append(i)
        number = number / i
    else:
        i+=1
print(list)