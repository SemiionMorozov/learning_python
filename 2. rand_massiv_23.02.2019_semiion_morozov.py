# 2 задание - массив случайных чисел
# 23.02.2019 - Semion Morozov - semiion-morozov@mail.ru

import random

mas = [i for i in range(1, 21)]

for i in range(10):
    rand_index = random.randint(0, 19)
    rand_count = random.randint(1, 20)
    mas[rand_index] = rand_count
    #s = str(sum(mas)) + ' = ' + str(mas)
    s = "{0} = {1}".format(sum(mas), mas)
    print(s)
    
    #print(p.__sizeof__()) # проверил память данным способом, вроде одинаково,
    #print(s.__sizeof__()) # хотя это объем значения переменной (не обработки)


