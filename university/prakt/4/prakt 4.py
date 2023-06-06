import re

def read_file (name: str):
    f = open(name, 'r',encoding='utf-8')
    text = f.read()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    words = text.split()
    words = list(set(words))
    words.sort()
    f.close()
    return words



def save_file():
    f = open('count.txt','a',encoding='utf-8')
    f.writelines(f'Всего уникальных слов: {len(words)}\n=========================')
    for i in range(len(words)):
        f.writelines(f'{words[i]}\n')
    f.close()
    return
words = read_file('data.txt')
save_file()
