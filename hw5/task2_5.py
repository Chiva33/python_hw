#  Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


import random

print('ПРАВИЛА ИГРЫ\n На столе лежат конфеты. Играют два игрока, делая ход друг после друга.\n Первый ход определяется жеребьёвкой. За один ход можно забрать не более определенного конфет.\n Игрок, который заберет последние конфеты - победил.')
def bot_first(game):
    candy = n
    while candy > 0:
        print('Ход соперника.')
        mb = candy % (e+1)
        if mb > 0:
            candy = candy - mb
        else:
            mb = random.randint(1, e)
            candy = candy - mb
        print('Соперник взял', mb, 'конфет, осталось ',candy)
        if candy == 0:
            print('Соперник победил!')
            break
        pm = int(input('Сколько конфет возьмете?\n'))
        while pm > e:
            print('Слишком много.')
            pm = int(input('Сколько конфет возьмете?\n'))
            if pm <= e:
                break
        candy = candy - pm
        print('Осталось', candy, 'конфет.')
        if candy == 0:
            print('Вы победили!')
            break

def player_first(game):
    candy = n
    while candy > 0:
        pm = int(input('Сколько конфет возьмете?\n'))
        while pm > e:
            print('Слишком много.')
            pm = int(input('Сколько конфет возьмете?\n'))
            if pm <= e:
                break
        candy = candy - pm
        print('Осталось', candy, 'конфет.')
        if candy == 0:
            print('Вы победили!')
            break
        print('Ход соперника.')
        mb = candy % (e+1)
        if mb > 0:
            candy = candy - mb
        else:
            mb = random.randint(1, e)
            candy = candy - mb
        print('Соперник взял', mb, 'конфет, осталось ',candy)
        if candy == 0:
            print('Соперник победил!')
            break
        
def player_player(game):
    candy = n
    while candy > 0:
        print('Ход первого игрока.')
        pm = int(input('Сколько конфет возьмете?\n'))
        while pm > e:
            print('Слишком много.')
            pm = int(input('Сколько конфет возьмете?\n'))
            if pm <= e:
                break
        candy = candy - pm
        print('Осталось', candy, 'конфет.')
        if candy == 0:
            print('Игрок 1 победил!')
            break
        print('Ход второго игрока.')
        pm = int(input('Сколько конфет возьмете?\n'))
        while pm > e:
            print('Слишком много.')
            pm = int(input('Сколько конфет возьмете?\n'))
            if pm <= e:
                break
        candy = candy - pm
        print('Осталось', candy, 'конфет.')
        if candy == 0:
            print('Игрок 2 победил!')
            break

versus = int(input('С кем будете играть?\n1.Бот\n2.Человек\n'))
if versus == 1:
    f = random.randint(1, 2)
    n = int(input('Введите общее количество конфет:\n'))
    e = int(input('Сколько конфет берем за один ход?\n'))
    if f == 1:
        print('Вы ходите первым.')
        player_first(n)
    elif f == 2:
        print('Соперник ходит первым.')
        bot_first(n)
else:
    n = int(input('Введите общее количество конфет:\n'))
    e = int(input('Сколько конфет берем за один ход?\n'))
    player_player(n)