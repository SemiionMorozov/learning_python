# 4 задание - класс: уравнение прямой
# 26.02.2019 - Semion Morozov - semiion-morozov@mail.ru


### Класс линейного уравнения v1.0
##
### Tochka пока не используется - не могу понять как подгружать property во внутреннюю функцию другого класса
##class Tochka:
##    @property
##    def x(self):
##        return self.__dict__['x']
##    @property
##    def y(self):
##        return self.__dict__['y']
##    @x.setter
##    def x(self, value):
##        self.__dict__['x'] = value
##    @y.setter
##    def y(self, value):
##        self.__dict__['y'] = value
##
##
##class LineEquation():
##    def __init__(self, a, b):
##        self.a = a
##        self.b = b
##    def check(self, c):
##        self.c = c
##        x1 = self.a[0]
##        y1 = self.a[1]
##        x2 = self.b[0]
##        y2 = self.b[1]
##        x3 = self.c[0]
##        y3 = self.c[1]
##        
##        # поиск коэффициентов k и b
##        k = (y2-y1)/(x2-x1)
##        b = y1-k*x1
##        bz = '+' if b >= 0 else ''
##        # отображение уравнения
##        print("Уравнение: y={0}*x{1}{2}".format(k,bz,b))
##    
##        # проверка третьей точки
##        if y3 == k*x3+b:
##            print ("точка с координатами [{0}, {1}] лежит на прямой".format(x3,y3))
##        else:
##            print("точка с координатами [{0}, {1}] не лежит на прямой".format(x3,y3))
##
##
##lineEqu = LineEquation([0,0],[1,1])
##print(lineEqu.a)
##print(lineEqu.b)
##lineEqu.check([2,2])
##lineEqu.check([2,3])


### Класс линейного уравнения v1.1
##
##class Point:
##    def __init__(self, a):
##        self.a = a
##    @property
##    def x(self):
##        return self.a[0]
##    @property
##    def y(self):
##        return self.a[1]
##    @x.setter
##    def x(self, value):
##        self.a[0] = value
##    @y.setter
##    def y(self, value):
##        self.a[1] = value
##
##class LineEquation():
##    def __init__(self, A, B):
##        self.A = A
##        self.B = B
##    def koef(self):
##        A = Point(self.A)
##        B = Point(self.B)
##        x1 = A.x
##        y1 = A.y
##        x2 = B.x
##        y2 = B.y
##        # поиск коэффициентов k и b
##        k = (y2-y1)/(x2-x1)
##        b = y1-k*x1
##        return [k, b]
##    def show(self):
##        k = self.koef()[0]
##        b = self.koef()[1]
##        # отображение уравнения
##        bz = '+' if b >= 0 else ''
##        print("Уравнение: y={0}*x{1}{2}".format(k,bz,b))
##    def check(self, C):
##        C = Point(C)
##        x3 = C.x
##        y3 = C.y
##        k = self.koef()[0]
##        b = self.koef()[1]
##        # проверка третьей точки
##        if y3 == k*x3+b:
##            print ("Точка с координатами [{0}, {1}] лежит на прямой".format(x3,y3))
##        else:
##            print("Точка с координатами [{0}, {1}] не лежит на прямой".format(x3,y3))
##
##
##lineEqu = LineEquation([0,0],[1,1])
##print("Точка A: {0}".format(lineEqu.A))
##print("Точка B: {0}".format(lineEqu.B))
##lineEqu.show()
##lineEqu.check([2,2])
##lineEqu.check([2,3])


### Класс линейного уравнения v1.2 - убрал 6 лишних связей по типу x1 = A.x
##
##class Point:
##    def __init__(self, a):
##        self.a = a
##    @property
##    def x(self):
##        return self.a[0]
##    @property
##    def y(self):
##        return self.a[1]
##    @x.setter
##    def x(self, value):
##        self.a[0] = value
##    @y.setter
##    def y(self, value):
##        self.a[1] = value
##
##class LineEquation():
##    def __init__(self, A, B):
##        self.A = A
##        self.B = B
##    def koef(self):
##        A = Point(self.A)
##        B = Point(self.B)
##        # поиск коэффициентов k и b
##        k = (B.y-A.y)/(B.x-A.x)
##        b = A.y-k*A.x
##        return [k, b]
##    def show(self):
##        k = self.koef()[0]
##        b = self.koef()[1]
##        # отображение уравнения
##        bz = '+' if b >= 0 else ''
##        print("Уравнение: y={0}*x{1}{2}".format(k,bz,b))
##    def check(self, C):
##        C = Point(C)
##        k = self.koef()[0]
##        b = self.koef()[1]
##        # проверка третьей точки
##        if C.y == k*C.x+b:
##            print("Точка с координатами [{0}, {1}] лежит на прямой".format(C.x,C.y))
##        else:
##            print("Точка с координатами [{0}, {1}] не лежит на прямой".format(C.x,C.y))
##
##
##lineEqu = LineEquation([0,0],[1,1])
##print("Точка A: {0}".format(lineEqu.A))
##print("Точка B: {0}".format(lineEqu.B))
##lineEqu.show()
##lineEqu.check([2,2])
##lineEqu.check([2,3])


# # Класс линейного уравнения v1.3
#
# class Point:
#     @property
#     def x(self):
#         return self.x_val
#
#     @property
#     def y(self):
#         return self.y_val
#
#     @x.setter
#     def x(self, value):
#         self.x_val = value
#
#     @y.setter
#     def y(self, value):
#         self.y_val = value
#
#
# class LineEquation:
#     def __init__(self, A_in, B_in):
#         self.A = Point()
#         self.A.x = A_in[0]
#         self.A.y = A_in[1]
#         self.B = Point()
#         self.B.x = B_in[0]
#         self.B.y = B_in[1]
#
#     def show(self):
#         Ax = self.A.x
#         Ay = self.A.y
#         Bx = self.B.x
#         By = self.B.y
#         # поиск коэффициентов k и b
#         k = (By-Ay)/(Bx-Ax)
#         b = Ay-k*Ax
#         self.k = k
#         self.b = b
#         # отображение уравнения
#         bz = '+' if b >= 0 else ''
#         print("Уравнение: y={0}*x{1}{2}".format(k, bz, b))
#
#     def check(self, C_in):
#         C = Point()
#         C.x = C_in[0]
#         C.y = C_in[1]
#         k = self.k
#         b = self.b
#         # проверка третьей точки
#         if C.y == k*C.x+b:
#             print("Точка с координатами [{0}, {1}] лежит на прямой".format(C.x, C.y))
#         else:
#             print("Точка с координатами [{0}, {1}] не лежит на прямой".format(C.x, C.y))
#
#
# lineEqu = LineEquation([0, 0], [1, 1])
#
# print("Изначальные данные:")
# print("Точка A: [{0}, {1}]".format(lineEqu.A.x, lineEqu.A.y))
# print("Точка B: [{0}, {1}]".format(lineEqu.B.x, lineEqu.B.y))
# lineEqu.show()
# lineEqu.check([2, 2])
# lineEqu.check([3, 5])
#
# print('')
#
# lineEqu.A.x = 2
# lineEqu.A.y = 3
# print("Изменили точку A:")
# print("Точка A: [{0}, {1}]".format(lineEqu.A.x, lineEqu.A.y))
# print("Точка B: [{0}, {1}]".format(lineEqu.B.x, lineEqu.B.y))
# lineEqu.show()
# lineEqu.check([2, 2])
# lineEqu.check([3, 5])


# Класс линейного уравнения v1.4

class Point: # объявление класса Point
    def __init__(self, x, y): # конструктор класса с атрибутами x и y
        self.x = x # создание внутриклассовых переменных x и y
        self.y = y # с присвоением им значений атрибутов

    @property # декоратор @property (геттер)
    def x(self): # метод x
        return self._x # возвращение значения переменной _x (_ - инкапсуляция)
        # имя переменной _x должно отличаться от имени метода x, иначе возникнет ошибка
        # RecursionError: - превышена рекурсия

    @property # тоже самое для y
    def y(self):
        return self._y

    @x.setter # декоратор @x.setter (сеттер)
    def x(self, value): # метод x с атрибутом value
        self._x = value # присвоение переменной _x значение атрибута value

    @y.setter # тоже самое для y
    def y(self, value):
        self._y = value


class LineEquation: # объявление класса LineEquation
    def __init__(self, A, B): # конструктор класса с атрибутами A и B
        self.A = A # создание внутриклассовых переменных A и B
        self.B = B # с присвоением им значений атрибутов

        self._calc() # вызов метода _calc() при инициализации объекта класса LineEquation

    def _calc(self): # объявление метода _calc - расчёт
        if self.A and self.B: # если переменные A и B существуют - корректны (True)
            self.k = (self.B.y - self.A.y) / (self.B.x - self.A.x) # формула рассчета коэффициента k
            self.b = self.A.y - self.k * self.A.x # формула расчета коэффициента b
        else: # если переменные отсутствуют - не корректны (False)
            self.k = None # присвоение коэффициентам значения None
            self.b = None

    def show(self): # объявление метода show - показать
        # отображение уравнения
        bz = '+' if self.b >= 0 else '' # объявление переменной знака ("+" если коэф. b >= 0, "-" в остальных случаях)
        print("Уравнение: y={0}*x{1}{2}".format(self.k, bz, self.b)) # вывод уравнения на экран в заданном формате

    def check(self, C): # объявление метода check (проверить) с аргументом C
        # проверка третьей точки
        if C.y == self.k * C.x + self.b: # если данное уравнение верно
            print("Точка с координатами [{0}, {1}] лежит на прямой".format(C.x, C.y)) # вывести что точка C лежит
        else: # иначе
            print("Точка с координатами [{0}, {1}] не лежит на прямой".format(C.x, C.y)) # вывести что точка C не лежит


lineEqu = LineEquation(Point(0, 0), Point(1, 1)) # создание объекта lineEqu класса линейного уравнения LineEquation,
# в качестве его аргументов - объекты класса точка Point с аргументами координат x и y для каждой из точек.
print("Точка A: [{0},{1}]".format(lineEqu.A.x, lineEqu.A.y)) # вывод координат точек на экран
print("Точка B: [{0},{1}]".format(lineEqu.B.x, lineEqu.B.y))

lineEqu.show() # обращение к методу show() - вывод уравнения

lineEqu.check(Point(2, 2)) # проверка точек на принадлежность заданной прямой линии
lineEqu.check(Point(2, 3))
