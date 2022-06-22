# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'Результат эксперименабвта: работает лабви натуралабвьное средсабвтво от комаров из траабвв, ванили и эфирного масла?'

def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_words(text)
print(text)
