#расширение и переопределение базового класса

#Расширение базового класса — это добавление новых атрибутов
# в дочерних классах, не затрагивая при этом реализацию базового класса.

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return print(f'{self.first} {self.last}')

class Developer(Employee):
    def code(self):
        print("I'm coding now!")

dev_1 = Developer('Ivan', 'Ivanov', 60000)
dev_1.fullname() #Ivan Ivanov
dev_1.code() #I'm coding now!

#Переопределение базового класса — это изменение в дочерних классах
# поведения функционала родительского класса.

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return print(f'{self.first} {self.last}')

    def code(self):
        print("I'm coding as an employee.")

class Developer(Employee):
    def code(self):
        print("I'm coding as a developer now!")

dev_1 = Developer('Ivan', 'Ivanov', 60000)
dev_1.fullname() #Ivan Ivanov
dev_1.code() #I'm coding as a developer now!

#Функция super() возвращает объект-посредник, который делегирует
# вызовы метода родительскому или родственному классу.
# Позволяет получать доступ из класса-наследника к методам класса-родителя
# в том случае, если наследник переопределил эти методы.

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Developer('Ivan', 'Ivanov', 60000, 'Python')
dev_2 = Developer('Petr', 'Petrov', 70000, 'Java')

# class НазваниеКласса(БазовыйКласс):
#
#     def метод_от_родителя(self):
#         super().метод_от_родителя()

class Employee:
    def work(self):
        print('Do some work')

class Developer(Employee):
    def work(self):
        super().work()
        print('Write code')

class JavaDeveloper(Developer):
    def work(self):
        super().work()
        print('Write tests for code')

jv = JavaDeveloper()
jv.work()
# Do some work
# Write code
# Write tests for code



