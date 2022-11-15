from random import *

print('\nПравила игры: На столе лежит 2021 конфета.'
      '\nЗа один ход можно забрать не более чем 28 конфет.'
      '\nВсе конфеты оппонента достаются сделавшему последний ход.\n')


def play(candies):
    count = 0
    while candies > 0:
        if count == 0:
            motion = int(input(f'Ход "{first}": '))
            try:
                if 0 < motion <= 28:
                    candies -= motion
                    count += 1
                else:
                    print('Невернный ввод, повторите!')
            except:
                motion
            if candies > 0:
                print(f'Осталось {candies} конфет ')
            else:
                print(f'Игра оконченна победил {first}!')
                break
        if count == 1:
            motion = int(input(f'Ход "{second}": '))
            try:
                if 0 < motion <= 28:
                    candies -= motion
                    count -= 1
                else:
                    print('Невернный ввод, повторите!')
            except:
                motion
            if candies > 0:
                print(f'Осталось {candies} конфет ')
            else:
                print(f'Игра оконченна победил {second}!')
                break


def play_vs_bot(candies):
    print(f'Осталось {candies} конфет ')
    if first == player1:
        count = 0
    else:
        count = 1
    while candies > 0:
        if count == 0:
            motion1 = int(input(f'Ход "{player1}": '))
            try:
                if 0 < motion1 <= 28:
                    candies -= motion1
                    count += 1
                else:
                    print('Невернный ввод, повторите!')
            except:
                motion1
            if candies > 0:
                print(f'Осталось {candies} конфет ')
            else:
                print(f'Игра оконченна победил {player1}!')
                break
        if count == 1:
            if candies > 0 and candies > 28:
                motion2 = randint(1, 28)
                print(f'Ход {player2} {motion2}')
                try:
                    if 0 < motion2 <= 28:
                        candies -= motion2
                        count -= 1
                        print(f'Осталось {candies} конфет ')
                    else:
                        print('Невернный ввод, повторите!')
                except:
                    motion2
            elif 0 < candies <= 28:
                motion2 == candies
                print(f'Ход {player2} {motion2}')
                print(f'Игра оконченна победил {player2}!')
                break


from pick import pick

title = 'Выберите режим игры'
games = ['Player VS Player', 'Player VS COM']
candies = 2021
game, index = pick(games, title, indicator='=>', default_index=0)
if game == 'Player VS Player':
    player1 = input('Введите имя первого игрока: ')
    player2 = input('Введите имя второго игрока: ')
    first_motion = randint(0, 1)
    if first_motion == 0:
        first = player1
        second = player2
        print(f'Начинает игру "{first}"')
    else:
        first = player2
        second = player1
        print(f'Начинает игру "{first}"')
    play(candies)
if game == 'Player VS COM':
    player1 = input('Введите имя игрока: ')
    player2 = '"COM"'
    first_motion = randint(0, 1)
    if first_motion == 0:
        first = player1
        second = player2
        print(f'Начинает игру "{first}"')
    else:
        first = player2
        second = player1
        print(f'Начинает игру "{first}"')
    play_vs_bot(candies)
