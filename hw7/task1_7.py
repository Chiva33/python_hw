name = input('Введите имя:')
surname = input('Введите фамилию:')
tel = input('Введите телефон:')
about = input('Введите оисание:')
with open('bd1.txt', 'a+', encoding='utf-8') as file:
    file.write(', '.join([name, surname, tel, about]) + '\n')