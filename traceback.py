#Разобраться, где в коде ошибка и почему возникло
# исключение, помогает дополнительная информация —
# traceback.

#Traceback (трассировка, трэйс) — отчет, который
# показывает стек вызовов, где появилась ошибка.
# Каждое исключение содержит краткую информацию и
# полный путь до места ошибки.

#Стек — тип данных, представляющий собой список элементов,
# организованных по принципу LIFO (англ. last in — first out,
# «последним пришел — первым вышел»). То есть добавление
# новых элементов и удаление существующих производится с
# одного конца, называемого вершиной стека. Первым из стека
# удаляется элемент, который был помещен туда последним.

class Exp:

    def func1(self):
        self.func2()
        print('Штатное завершение func1()')

    def func2(self):
        self.func3()
        print('Штатное завершение func2()')

    def func3(self):
        print(100 / 0)
        print('Штатное завершение func3()')

# ob = Exp()
# ob.func1()
#
# print("Выход.")

# Traceback (most recent call last):
#   File "C:\Users\alexa\PycharmProjects\inheritance\traceback.py", line 32, in <module>
#     ob.func1()
#   File "C:\Users\alexa\PycharmProjects\inheritance\traceback.py", line 20, in func1
#     self.func2()
#   File "C:\Users\alexa\PycharmProjects\inheritance\traceback.py", line 24, in func2
#     self.func3()
#   File "C:\Users\alexa\PycharmProjects\inheritance\traceback.py", line 28, in func3
#     print(100 / 0)
# ZeroDivisionError: division by zero

#Обработать (перехватывать) исключение можно на любом уровне стека.

#Например, на уровне модуля, если поместить вызов метода func1()
#  в блок try/except:

ob = Exp()
try:
    ob.func1()
except ZeroDivisionError:
    print('Ошибка где-то в цепочке вызовов func1().')

print('Exit')

# Ошибка где-то в цепочке вызовов func1().
# Exit

# Обрабатывать исключения можно и на более глубоких уровнях. Например, непосредственно в методе
# func1() или в func3() при выполнении деления на ноль:


class ExpTr:

    def func1(self):
        try:
            self.func2()
        except ZeroDivisionError:
            print('Ошибка в func1()')
        print('Штатное завершение func1()')

    def func2(self):
        try:
            self.func3()
        except ZeroDivisionError:
            print('Ошибка в func2()')
        print('Штатное завершение func2()')

    def func3(self):
        try:
            print(100 / 0)
        except ZeroDivisionError:
            print('Ошибка в func3()')
        print('Штатное завершение func3()')


ob = ExpTr()

try:
    ob.func1()
except ZeroDivisionError:
    print('Ошибка где-то в классе Exp.')

print('Exit')

# Ошибка в func3()
# Штатное завершение func3()
# Штатное завершение func2()
# Штатное завершение func1()
# Exit

