import re



f = open('list.txt', 'r',encoding='utf-8')
text = f.readlines()
f.close()
selective = []
for i in text:
    inf = 0
    inf = re.match(r'^Рейс\s\d{3}\s(?:прибыл|отправился)\s(?:из|в)\s\w{4,6}\sв\s\d{2}:\d{2}:\d{2}', i)
#^ - начало строки \s - соответствует пробелам, табуляции и тд
#\d - соответствует цифрам а в скобках их количество (?: ищет )
#\w - соответствует буквам
    if inf != None:
        selective.append(inf[0])
text.clear()
for i in selective:
    town = re.search(r'(?:из|в)\s\w{4,6}', i)
    number = re.search(r'\d{3}', i)
    time = re.search(r'\d{2}:\d{2}:\d{2}', i)
    text.append(f'[{time[0]}] - Поезд №{number[0]} {town[0]}\n')
f = open('result.txt', 'a',encoding='utf-8')
f.writelines(text)
f.close()