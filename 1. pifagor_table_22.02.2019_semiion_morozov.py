# Таблица Пифагора - двумерный массив (матрица)
# 22.02.2019 - Semion Morozov - semiion-morozov@mail.ru

#x = 1
#y = 1

# 1 вариант - сложная неудобная инициализация массива с возможными ошибками,
# например, в данном случае
#pif_xy = [['']*10]*10 # не работает

#pif_xy = [['']*10,['']*10,['']*10,['']*10,['']*10,['']*10,['']*10,['']*10,['']*10,['']*10] # инициализация массива

#while y<=10:
    #while x<=10:
        #pif_xy[y-1][x-1] = x * y
        #x += 1
        
    #y += 1
    #x = 1


# 2 вариант - простая инициализация массива с последующим добавлением элементов (вложенных массивов)
#a = 10 # кол-во строк
#b = 10 # кол-во элементов в строке
#pif_xy = [] # инициализация массива
#for i in range(a):
    #pif_xy.append([])
    #for j in range(b):
        #pif_xy[i].append(x*y)
        #x += 1
    #y += 1
    #x = 1

# просто вывод массива
#print (pif_xy)

# красивый вывод двумерного массива
#for row in pif_xy:
    #print(*row)


# Алгоритм поиска НОК и НОД двух чисел
def nok_nod (a,b):
    p = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    nod = a + b
    nok = int (p / nod)
    nok_nod = [nod,nok]
    return nok_nod

#a = int(input("Введите число a="))
#b = int(input("Введите число b="))
#nok_nod = nok_nod (a,b)
#nod = nok_nod[0]
#nok = nok_nod[1]
#print("НОК:" + str(nok) + ", НОД:" + str(nod))


# Таблица Пифагора на НОК и НОД:
#x = 1
#y = 1
#while y <= 10:
    #while x <= 10:
        #a = nok_nod (x,y)[0] * nok_nod (x,y)[1]
        #x += 1
        #print(str(a) + " ", end = '')
    #print('')
    #x = 1
    #y += 1


# Таблица Пифагора на простом умножении с выравниванием при выводе
#x = 1
#y = 1
#while y <= 10:
    #while x <= 10:
        #a = x * y
        #x += 1
        #if len(str(a)) == 1:
            #print(str(a) + "   ", end = '')
        #elif len(str(a)) == 2:
            #print(str(a) + "  ", end = '')
        #elif len(str(a)) == 3:
            #print(str(a) + " ", end = '')
    #print('') # для новой строки
    #x = 1
    #y += 1


# Таблица Пифагора - упрощенный код v1.023.02.2019
#x = 1
#y = 1
#s = ''  # одна строка чисел
#while y <= 10:
    #while x <= 10:
        #a = str(x * y)
        #if len(a) == 1:
            #a += "   "
        #elif len(a) == 2:
            #a += "  "
        #else:
            #a += " "
        #s += a
        #x += 1
    #print(s)
    #s = ''
    #x = 1
    #y += 1


# Таблица Пифагора - упрощенный код v1.1 25.02.2019
for y in range(1, 11):
    s = ''
    for x in range(1, 11):
        s += str(x * y).rjust(4)
    print(s)

