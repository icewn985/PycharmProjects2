import random

def world_find():
    f = open('words.txt','r',encoding='utf-8')
    text = f.readlines()
    text = str(*text).split(',')
    count = len(text)
    for i in range(count):
        world = str(text[i])
        a = world.find(' ')
        if a != '-1':
            text[i] = world.strip()

    number = random.randrange(count)
    text = str(text[number])
    return text

def records(end):
    f = open('records.txt','a',encoding='utf-8')
    f.writelines(f'{end} \n')
    f.close()
    return