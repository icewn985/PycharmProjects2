import random

def game():
    result1 = 0
    result2 = 0
    n = 0
    while n != 10000:
        a = random.randrange(3)
        list = [0,0,0]
        list[a] = 1

        choise1 = random.randrange(3)

        if list[choise1] == 1:
            result1 = result1 + 1
        list[choise1] = 2
        list.remove(2)
        list.remove(0)
        if list[0] == 1:
            result2 = result2 + 1
        n = n + 1

    result1 = (result1*100)/10000
    result2 = (result2*100)/10000
    return  f'Если не изменять выбор: {result1}%\nЕсли выбор изменить: {result2}%'