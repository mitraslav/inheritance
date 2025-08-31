#__dict__ - это магический атрибут в Python, представляющий собой словарь,
# в котором хранятся атрибуты объекта (экземпляра класса). Он позволяет добавлять,
# изменять и удалять атрибуты объекта во время выполнения программы.
import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_del(self):
        self.x += 1
        del self.y
        self.y = 0

pt = Point(10, 20)

#Мы можем создавать новые свойства экземпляров класса:
pt.z = 100

print(pt.__dict__)
#{'x': 10, 'y': 20, 'z': 100}

#__slots__ - это способ оптимизации использования памяти в Python,
# который позволяет заранее определить, какие атрибуты могут присутствовать
# в экземпляре класса.

class MyClass:
    __slots__ = ('attr1', 'attr2', 'attr3')

class PointSlots:
    MAX_VALUE = 1000

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_del(self):
        self.x += 1
        del self.y
        self.y = 0
#Экземпляры класса со __slots__ будут занимать меньше памяти,
# доступ к их атрибутам будет быстрее. Но у экземпляров такого
# класса нельзя будет создавать новые свойства.

pts = PointSlots(10, 20)

#pts.z = 100
#AttributeError: 'PointSlots' object has no attribute 'z' and no
# __dict__ for setting new attributes

print(pts.__slots__)
#('x', 'y')

#pts.__dict__
#AttributeError: 'PointSlots' object has no attribute '__dict__'. Did you mean: '__dir__'?

#Тест на скорость

pt = Point(10, 20)
pts = PointSlots(10, 20)

t1 = timeit.timeit(pt.get_set_del)
t2 = timeit.timeit(pts.get_set_del)

print(t1, t2)
print((t1-t2)/t1*100)

# 0.10558590001892298 0.12288359995000064
# -16.38258510651288

#Если дочерний класс не имеет своего атрибута __slots__, то у
# экземпляра дочернего класса можно создавать любые атрибуты:

class Parent:
    __slots__ = ['a', 'b']

class Child(Parent):
    pass

child = Child()
child.a = 1
child.b = 2
child.c = 3 # Нет ошибки,
# так как в дочернем классе не определена коллекция __slots__

#Если родительский класс имеет свой атрибут __slots__ и дочерний
# класс имеет свой атрибут __slots__, то у экземпляра дочернего класса
# можно создавать только те атрибуты, которые есть в родительской и дочерней коллекции __slots__

class Parent:
    __slots__ = ['a', 'b']

class Child(Parent):
    __slots__ = ['c', 'd']

child = Child()
child.a = 1
child.b = 2
child.c = 3
child.d = 4
#child.e = 5 # Ошибка,
# так как атрибут 'e' не определен ни в __slots__ родительского,
# ни в __slots__ дочернего класса



