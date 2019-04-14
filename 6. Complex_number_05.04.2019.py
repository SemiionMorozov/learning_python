# класс Комплексные числа - 05.04.2019 - semiion-morozov@mail.ru

class ComlexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "{} + j{}".format(self.a, self.b)

    def __add__(self, other):
        return ComlexNumber(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return ComlexNumber(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return ComlexNumber(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)


z1 = ComlexNumber(1, 4) # z = a + bi
z2 = ComlexNumber(2, 1)

print("z1 = {}".format(z1))
print("z2 = {}".format(z2))
print("z1 + z2 = {}".format(z1+z2))
print("z1 * z2 = {}".format(z1*z2))


