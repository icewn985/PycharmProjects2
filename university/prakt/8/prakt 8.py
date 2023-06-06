import pymorphy2
import re
from translate import Translator
import translate

translator = Translator(from_lang="ru", to_lang="en")
morph = pymorphy2.MorphAnalyzer()
f = open('dialog.txt', 'r', encoding='utf=8')
text = f.readlines()
result = " ".join(text)
text = re.sub(r'[^\w\s]','', result)
text = text.split()
result = []
for i in range(len(text)):
    h = text[i].split()
    for t in range(len(h)):
        result.append(morph.parse(h[t])[0].normal_form)
h = []

z = list(set(result))
for i in range(len(z)):
    h.append(result.count(z[i]))

dictionary = dict(zip(z, h))
sorted_dict = {}
sorted_keys = sorted(dictionary, key=dictionary.get)
sorted_keys.reverse()

for w in sorted_keys:
    sorted_dict[w] = dictionary[w]
print(sorted_dict)
f = open('result.txt', 'a',encoding='utf-8')

for key in sorted_dict:
    word = key + ' ' + translator.translate(key) + ' ' + str(sorted_dict[key]) + '\n'
    word = word.title()
    f.writelines (word)
f.close()
 