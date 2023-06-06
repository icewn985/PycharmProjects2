import csv

def get_books(name:str):
    with open('books.csv') as File:
        reader = csv.reader(File, delimiter='|',
                            quoting=csv.QUOTE_MINIMAL)
        result = [[]]
        result.clear()
        for i in reader:
            a = ''.join(i).lower()
            if a.__contains__(name):
                result.append(i)
    return result

def get_totals(totals):
    result = []
    for i in range(len(totals)):
        instr = totals[i]
        summ = float(instr[4]) * int(instr[3])
        if summ < 500:
            summ += 100
        text = str(instr[0]) + ' ' + str(summ)
        text = tuple(map(str, text.split()))
        result.append(text)
    return result

print(get_totals(get_books('python')))
