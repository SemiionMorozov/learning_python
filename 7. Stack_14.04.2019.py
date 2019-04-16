# класс Работа со стеком - 14.04.2019 - semiion-morozov@mail.ru

# класс стека
class Stack :
    def __init__(self):
        self.items = []

    def push(self, item):   # загрузить в стек
        self.items.append(item)

    def pop(self):          # выгрузить из стека
        return self.items.pop()


stack = Stack()     # инициализация стека

for i in range(5):  # заполнение стека
    stack.push(i)   # через цикл for

print(stack.items)  # посмотреть содержимое стека

a = 0               # выгрузка из стека
while a <= len(stack.items): # через цикл while
    print(stack.pop())
    a =+ 1

print(stack.items)  # посмотреть содержимое стека

