from words import world_find
from words import records

def complexity():
    complexity = int(input('Выберите сложность: 1 - 3 жизни, 2 - 5 жизней, 3 - 7 жизней '))
    if complexity == 1:
        lives = 3
    elif complexity == 2:
        lives = 5
    elif complexity == 3:
        lives = 7
    else:
        print('Не верно указана сложность')
    return lives

def begin():
    lives = complexity()
    global score
    score = 0
    game(lives)
    return




def end (score, lives):
    if lives > 0:
        global check
        check = int(input('Если хотите продолжить нажмите 1, закончить игру 2 '))
        if check == 1:
            print(f'Осталось жизней: {lives}\n')
            return game(lives)
        elif check == 2:
            check = input('Спасибо за игру\nВведите ваше имя ')
            end = check + ' = ' + str(score)
            print(end)
            return records(end)
    else:
        check = str(input('Спасибо за игру\nВведите ваше имя '))
        end = check + ' = ' + str(score)
        records(end)
        check = input(f'{end}\nЧтобы начать новую игру нажмите 1\nЕсли хотите закончить 2 ')
        if check == '1':
            return begin()
        else:
            print('\nПока получается')

        return



def game(lives):
    global score
    a = world_find()
    world = []
    show_world = []
    symvol = '\u25A0'
    for i in range(len(a)):
        world.append(a[i])
        show_world.append(symvol)
    while lives != 0:
        if world != show_world:
            symvol = input('Введите букву или слово ')
            if len(symvol) == 1:
                right = 0
                for i in range(len(a)):
                    if world[i] == symvol and show_world[i] != symvol:
                        show_world[i] = symvol
                        right = right + 1
                        score = score + 1
            else:
                if symvol == a:
                    score = score + show_world.count('\u25A0')
                    end(score, lives)
            print(show_world)
            print(world)
            if right == 0:
                lives = lives - 1
            if lives == 0:
                end(score, lives)
        else:
            end(score, lives)