import csv

with open('D:\GeekBrains\Python\Homework\parents.csv', encoding='UTF=8') as r_file:
    file = csv.DictReader(r_file, delimiter=';')
    count = 0

    for row in file:
        if count == 0:
            print(f'Файл содержит столбцы: {", ".join(row)}')
        print(row)
        count += 1
    print(f'Всего в файле {count + 1} строк.')