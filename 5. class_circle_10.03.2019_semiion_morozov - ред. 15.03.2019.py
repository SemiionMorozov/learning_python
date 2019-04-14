# 5 задание - класс: круг
# 10.03.2019 - Semion Morozov - semiion-morozov@mail.ru - ред. 15.03.2019

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value


class Circle(Point):
    def __init__(self, x, y, r, f): # конструктор с атрибутами x,y - центр окружности, r - радиус, f - угол
        super().__init__(x, y) # центр окружности
        self.r = r  # радиус окружности
        self.f = f  # угол f

    def coordinate(self):
        f = math.radians(self.f)  # перевод градусов в радианы
        x = round(self.r * math.cos(f) + self._x, 2) # значение x точки на окружности
        y = round(self.r * math.sin(f) + self._y, 2) # значение y точки на окружности
        print("[{0},{1}]".format(x, y))  # вывод координат x,y точки на окружности


circle = Circle(0, 0, 1, 45)  # центр (x, y), радиус, угол (в градусах)
circle.x = 5 # изменение значения x центра окружности
circle.coordinate() # вывод координат точки на окружности
