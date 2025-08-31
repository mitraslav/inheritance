#Множественное наследование — это такое наследование, когда один дочерний класс
# образуется сразу от нескольких базовых.

#Миксины (от англ. mixins — примеси) — это классы, которые используются в качестве дополнительного
# функционала в других классах. Миксины применяются, когда требуется добавить в класс какой-то функционал
# без изменения его основной структуры.

class Employee:

    def __init__(self, name, surname):
        super().__init__()
        self.name = name
        self.surname = surname

class MixinLog:
    ID = 1

    def __init__(self):
        self.id = self.ID
        MixinLog.ID += 1

    def order_log(self):
        print(f"{self.id}-й сотрудник")

class Developer(Employee, MixinLog):
    pass

dev1 = Developer('Ivan', 'Ivanov')
dev1.order_log()
#AttributeError: 'Developer' object has no attribute 'id'. Did you mean: 'ID'?
#после исправления

#1-й сотрудник

#MRO (от англ. Method Resolution Order — порядок разрешения методов) — это алгоритм,
# который определяет порядок обхода классов при поиске методов и атрибутов в иерархии наследования.

print(Developer.__mro__)
#(<class '__main__.Developer'>, <class '__main__.Employee'>, <class '__main__.MixinLog'>, <class 'object'>)

#При другой иерархии наследования цепочка может быть другой, но всегда неизменно то, что первый базовый класс,
# указанный при наследовании, выбирается первым.



