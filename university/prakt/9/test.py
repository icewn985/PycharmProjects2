import os
from PIL import Image

def compression():
    correct = input('Укажите параметры сжатия в %: ')
    if correct.isdigit():
        if int(correct)<= 100 and int(correct) >= 0:
            return (correct)
        else:
            print('Указали не верный параметр.\nВведите в диапазоне 0 - 100')
            return compression()

#quality = compression()

try:
    file = 'test.jpg'
    image_path = 'test.jpg'

    #Image.save(file, quality=50)
    image_file = Image.open(image_path)
    image_file.save(file, quality=50)
except:
    print(f'Невозможно сжать изображение')