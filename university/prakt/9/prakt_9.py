import os, fnmatch
from pdf2docx import parse
from docx2pdf import convert
from PIL import Image

def menu():
    global catalog
    print(f'\nТекущий каталог: {catalog}')
    number = input(f'\nВыберите действие:\n\n0 - Сменить рабочий каталог\n1 - Преобразовать PDF в Docx\n2 - Преобразовать Doc, Docx в PDF\n3 - Сжать изображение\n4 - Удалить группу файлов\n5 - Выход\n\nВаш выбор: ')
    if int(number) >= 0 and int(number) <= 5:
        return choise(number)
    else:
        print('Не верный ввод')
        return menu()

def choise(number):
    global catalog
    if number == '0':
        catalog = change_kat()
        return menu()
    elif number == '1':
        return convert_pdf_dock(0)
    elif number =='5':
        print('\nБлагодарю за использование')
        return
    elif number == '2':
        return convert_pdf_dock(1)
    elif number == '3':
        return  convert_pdf_dock(2)
    elif number == '4':
        return del_menu()
    else:
        print('Не верный ввод')
        return choise()

def change_kat():
    global catalog
    change = input('Укажите путь к каталогу: ')
    try:
        os.chdir(change)
    except:
        print('Неверный путь')
        return change_kat()
    return os.getcwd()

def quality():
    correct = input('Укажите параметры сжатия в %: ')
    if correct.isdigit():
        if int(correct)<= 100 and int(correct) >= 0:
            return (int(correct))
        else:
            print('Указали не верный параметр.\nВведите в диапазоне 0 - 100')
            return quality()


def convert_pdf_dock(number : int):
    global catalog
    print(f'Список файлов в данном каталоге:')
    listOfFiles = os.listdir('.')
    if number == 0:
        pattern = "*.pdf"
    elif number == 1:
        pattern = "*.docx"
    elif number == 2:
        pattern = "*.jpg"
    list_file = list()
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            list_file.append(entry)
    for i in range(len(list_file)):
        print(f'{i+1}. {list_file[i]}')
    choise = input('Введите номер файла, при нажатии 0 выберутся все файлы ')
    try:
        if choise == '0':
            for i in range(len(list_file)):
                if number == 0:
                    parse(list_file[i])
                elif number == 1:
                    convert(list_file[i])
        else:
            choise = int(choise) - 1
            if number == 0:
                parse(list_file[choise])
            elif number == 1:
                try:
                    new_file = list_file[choise] + '.pdf'
                    convert(list_file[choise], new_file)
                except:
                    print(f'\nНе удалось конвертировать файл {list_file[choise]} в формат pdf\n')
                    return menu()
            elif number == 2:
                file = list_file[choise]
                image_path = file
                image_file = Image.open(image_path)
                image_file.save(file, quality=quality())
    except:
        print('Выберите из предложенных')
        return convert_pdf_dock(number)
    return menu()

def del_menu():
    inp = input('\nВыберите действие:\n\n1 - Удалить все файлы начинающиеся с подстроки\n2 - Удалить все файлы заканчивающиеся на подстроку\n'
                '3 - Удалить все файлы содержащие подстроку\n4 - Удалить все файлы по расширению ' )
    try:
        if int(inp) >= 1 and int(inp) <= 4:
            return remove(int(inp))
        else:
            print('Не верный ввод')
            return del_menu()
    except:
        print('Не верный ввод')
        return del_menu()
def answer (file):
    answer = input(f'{file}\nДействительно ли вы хотите удалить данный файл\n1 - Да \n2 - Нет ')
    if answer == '1':
        os.remove(file)
    elif answer != '1' and answer != '2':
        print('Неверный ввод\n')
        return answer(file)
    else:
        return

def remove(inp):
    global catalog
    print(f'Список файлов в данном каталоге: ')
    files = []
    for file in os.listdir(catalog):
        if os.path.isfile(file):
            files.append(file)
    for i in range(len(files)):
        print(f'{i+1}. {files[i]}')
    remove = input('Введите подстроку: ')
    if inp == 1:
        for file in files:
            if file [0:len(remove)] == remove:
                answer(file)
    elif inp == 2:
        for file in files:
            if file [-len(remove):] == remove:
                answer(file)
    elif inp == 3:
        for file in files:
            name = file.split('.')[0]
            if name.__contains__(remove):
                answer(file)
    elif inp == 4:
        for file in files:
            name = file.split('.')[1]
            if name.__contains__(remove):
                answer(file)
    return menu()

catalog = os.getcwd()
menu()
