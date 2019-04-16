# doubly linked list - двунаправленный список v1.0 - 15.04.2019 - semiion-morozov@mail.ru
# код сделан по материалам:
# http://py-algorithm.blogspot.com/2011/08/blog-post.html
# https://www.ibm.com/developerworks/ru/library/l-data_structures_01/
# https://www.ibm.com/developerworks/ru/library/l-data_structures_02/
# https://www.ibm.com/developerworks/ru/library/l-data_structures_03/
# http://www.cyberforum.ru/python-beginners/thread1454239.html

# внесена доработка и корректировки, в процессе тестирования совместимости компонентов
# удаления / вставки были выявлены и исправлены некоторые ошибки. Появилось понимание работы с классами
# в частности - двухсвязных списков и структур данных.

# P.S. При обнаружении (пока еще не выявленных) ошибок (нарушения связей в двунаправленном списке),
# просьба сообщить на почту semiion-morozov@mail.ru
# P.P.S.# Очень приветствуются все пожелания, рекомендации, корректировки, оптимизация читабельности и улучшения кода.


class Node:

    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:

    def __init__(self):
        self.head = None  # головной узел (первый)
        self.tail = None  # хвостовой узел (последний)

    def add(self, value):  # добавить в конец списка
        new_node = Node(value, None, None)  # Объявляем объект узла
        if self.head is None:  # Если головной узел пустой, то
            self.head = self.tail = new_node  # Головной равен хвостовому и равен узлу,
        else:  # вставка ноды в самый конец
            new_node.prev = self.tail  # ссылка на предыдущий узел
            new_node.next = None  # следующий узел None
            self.tail.next = self.tail = new_node  # поместить узел в хвост и привязать

    def insert(self, num, value):
        new_node = Node(value, None, None)  # Объявляем объект узла
        count = 0
        current_node = self.head
        while True:  # бесконечный цикл до прерывания break
            if count == num:
                if current_node is None:  # вставка последней ноды
                    new_node.prev = self.tail
                    new_node.next = None
                    self.tail.next = self.tail = new_node
                elif current_node.prev is None:  # вставка головной ноды
                    new_node.prev = None
                    new_node.next = current_node
                    current_node.prev = self.head = new_node
                elif current_node.next is None:  # вставка предпоследней ноды
                    new_node.prev = current_node.prev
                    new_node.next = current_node = self.tail
                    current_node.prev.next = self.tail.prev = new_node
                    current_node.next = None
                else:  # вставка промежуточной ноды
                    new_node.prev = current_node.prev
                    new_node.next = current_node
                    current_node.prev.next = current_node.prev = new_node
                break
            count += 1
            current_node = current_node.next  # переход к следующей ноде

    def del_node(self, num):
        count = 0
        current_node = self.head
        while True:  # бесконечный цикл до прерывания break
            if count == num:
                if current_node.prev is None:  # удаление головной ноды
                    self.head = current_node.next
                    current_node.next.prev = None
                elif current_node.next is None:  # удаление хвостовой ноды
                    self.tail = current_node.prev
                    current_node.prev.next = None
                else:  # удаление любой дргой ноды, кроме головной и хвостовой
                    current_node.prev.next = current_node.next  # сохранение линковки при
                    current_node.next.prev = current_node.prev  # образовавшемся разрыве
                break
            count += 1
            current_node = current_node.next  # переход к следующей ноде

    def show(self):
        if self.head is None:
            print(None)
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.next is None:
                    print(current_node.value, end=" ")
                    break
                else:
                    print(current_node.value, end=" <--> ")
                    current_node = current_node.next


L = DoublyLinkedList()
for i in range(0, 5):
    L.add(i)

L.insert(4, 12)

#L.del_node(4)

L.show()
