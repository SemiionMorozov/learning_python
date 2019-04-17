# doubly linked list - двунаправленный список v2.0 - 17.04.2019 - semiion-morozov@mail.ru
# код сделан по материалам:
# http://py-algorithm.blogspot.com/2011/08/blog-post.html
# https://www.ibm.com/developerworks/ru/library/l-data_structures_01/
# https://www.ibm.com/developerworks/ru/library/l-data_structures_02/
# https://www.ibm.com/developerworks/ru/library/l-data_structures_03/
# http://www.cyberforum.ru/python-beginners/thread1454239.html

# P.S. Очень приветствуются все пожелания, рекомендации, корректировки, оптимизация читабельности и улучшения кода.


class Node:

    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:

    def __init__(self):  # Инициализация
        self.head = None  # головной узел (первый)
        self.tail = None  # хвостовой узел (последний)

    def __str__(self):
        if self.head is not None:
            current = self.head
            out = 'DoublyLinkedList (' + str(self.len()) + ' pcs) [\n    ' + str(self.head.value) + ' <--> '
            while current.next is not self.tail:
                current = current.next
                out += str(current.value) + ' <--> '
            out += str(self.tail.value)
            return out + '\n]'
        return 'DoublyLinkedList []'

    def len(self): # Длина списка
        length = 0
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
                length += 1
        return length + 1

    def add(self, value):  # добавить в конец списка
        if self.head is None:  # Создание списка из одной ноды
            self.head = self.tail = Node(value, None, None)
        else:   # Добавить ноду в конец
            self.tail.next = self.tail = Node(value, self.tail, None)

    def insert(self, num, value):   # Вставка ноды в произвольное место с разбивкой пополам (для оптимизации)
        if num > self.len() or num < 0:
            print("insert_error: Вставить узел (ноду) [{0}] нельзя, у неё нет ближайших соседей!".format(num))
        elif num == 0:  # вставка головной ноды
            self.head.prev = self.head = Node(value, None, self.head)
        elif num == self.len(): # вставка хвостовой ноды
            self.tail.next = self.tail = Node(value, self.tail, None)
        elif num < self.len() / 2:  # Вставка в первую половину сначала
            current_node = self.head
            for i in range(self.len()):
                if i == num:  # вставка любой другой ноды, кроме головной и хвостовой
                    current_node.prev.next = current_node.prev = Node(value, current_node.prev, current_node)
                    break
                current_node = current_node.next
        else:  # Вставка во вторую половину с хвоста
            current_node = self.tail
            for i in range(self.len()):
                if i == self.len() - num - 1:  # вставка любой другой ноды, кроме головной и хвостовой
                    current_node.prev.next = current_node.prev = Node(value, current_node.prev, current_node)
                    break
                current_node = current_node.prev

    def delete(self, num):  # Удаление произвольной ноды с разбивкой пополам (для оптимизации)
        if num > self.len() - 1 or num < 0:
            print("Del_error: Узел (нода) с адресом [{0}] в списке отсутствует!".format(num))
        elif num == 0:  # удаление головной ноды
            self.head = self.head.next
            self.head.prev = None
        elif num == self.len() - 1:  # удаление хвостовой ноды
            self.tail = self.tail.prev
            self.tail.next = None
        elif num < self.len() / 2:  # Перебор первой половины сначала
            current_node = self.head
            for i in range(self.len()):
                if i == num:  # удаление любой другой ноды, кроме головной и хвостовой
                    current_node.prev.next = current_node.next  # сохранение линковки при
                    current_node.next.prev = current_node.prev  # образовавшемся разрыве
                    break
                current_node = current_node.next
        else:   # Перебор второй половины с конца
            current_node = self.tail
            for i in range(self.len()):
                if i == self.len() - num - 1:  # удаление любой дргой ноды, кроме головной и хвостовой
                    current_node.prev.next = current_node.next  # сохранение линковки при
                    current_node.next.prev = current_node.prev  # образовавшемся разрыве
                    break
                current_node = current_node.prev


L = DoublyLinkedList()

for i in range(0, 10):
    L.add(i)

L.insert(3, 'x')

# L.delete(5)

print(L)