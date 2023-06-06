try:
    name = input('Введите название файла ')
    name = name+'.txt'
    f = open(name, 'r',encoding='utf-8')
    text = f.read()
    text = text.split()
    print(text[1:])
    f.close()
except:
    print('Не верно ввидено имя файла')

