from abc import ABC, abstractmethod

class Employee:

    def work(self):
        pass

class Developer(Employee):

    def work(self):
        print("Пишет код")

class Accountant(Employee):

    def work(self):
        print("Считает зарплату")

emp = Employee()
dev = Developer()
acc = Accountant()

emp.work()
dev.work()
acc.work()

#Абстрактный класс — класс, который содержит один или
# несколько абстрактных методов. Абстрактный класс запрещает
# пользователю создавать экземпляры этого класса.

#Абстрактный метод — метод, который имеет объявление, но не имеет реализации.
# Абстрактный метод вынуждает пользователя переопределять себя в дочернем классе.

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
     def work(self):
         print('Coding')

class Accountant(Employee):
    def work(self):
        print('Counts wages')

#emp = Employee() #TypeError: Can't instantiate abstract class Employee without an implementation for abstract method 'work'

#Если мы уберем @abstractmethod из класса Employee, то мы по-прежнему сможем создавать объекты этого класса.

# class Developer(Employee):
#     pass
# dev = Developer()
#TypeError: Can't instantiate abstract class Developer without an implementation for abstract method 'work'

dev = Developer()
acc = Accountant()

