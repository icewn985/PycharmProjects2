import random

def birthday():
    result = 0
    n=0
    while n!=10000:
        list_day = []
        list_mounce = []
        for k in range(22):
            a = random.randrange(28)
            b = random.randrange(12)
            c = k
            list_day.append(a)
            list_mounce.append(b)
            for h in range(k):
                if h != k:
                    if list_day[k] == list_day[h]:
                        if list_mounce[k] == list_mounce[h]:
                            '''print(k,h,list_mounce[k],list_mounce[h],list_day[k],list_day[h])'''
                            result = result + 1
                            break
        n = n + 1
    result = (result*100)/10000
    return f'Процент совпадения дней рождений в группе хотя бы раз: {result}%'



