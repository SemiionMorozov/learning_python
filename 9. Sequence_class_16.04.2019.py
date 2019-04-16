# Sequence class - Класс выдающий последовательности, начиная с числа, переданного в конструктор v1.0
# 16.04.2019 - semiion-morozov@mail.ru

# # вариант без использования yield
# class Sequence:
#     def __init__(self, value):
#         self.value = value
#
#     def now_var(self):
#         print(self.value)
#         self.value += 1
#
#
# s = Sequence(100)
#
# s.now_var()
# s.now_var()
# s.now_var()
# s.now_var()
# s.now_var()


# Вариант с использованием yield
class Sequence:
    def __init__(self, value):
        self.value = value

    def now_var(self):
        yield self.value
        self.value += 1

    def show(self):
        for i in self.now_var():
            print(i)


s = Sequence(100)

s.show()
s.show()
s.show()
s.show()
s.show()