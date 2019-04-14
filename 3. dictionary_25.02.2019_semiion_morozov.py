# 3 задание - работа со словарем (ассоциативным массивом)
# 25.02.2019 - Semion Morozov - semiion-morozov@mail.ru

# Словарь v1.0
#keys = [i for i in range(0, 21)]
#values = [str(i) for i in range(0, 21)]
#dic = dict(zip(keys, values))
#print(dic)

#a = ''
#b = ''
#for key in dic.keys():
    #if key % 2 == 0: # чётные
        #a += (str(key)).rjust(4)

#for val in dic.values():
    #if str(val).endswith('0'): # оканчиваются на 0
        #b += (str(val)).rjust(4)

#print("Четные числа: {0}".format(a))
#print("С 0 на конце: {0}".format(b))


# Словарь v1.1
dic = {x: str(y) for x, y in zip(range(22), range(0,21))}
#print(dic)

a = [str(key) for key in dic.keys() if key % 2 == 0]
b = [val for val in dic.values() if val.endswith('0')]

print("Четные числа: {0}".format(' '.join(a)))
print("С 0 на конце: {0}".format(' '.join(b)))
