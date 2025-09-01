# print('Начало работы программы...')
# print(a)
# print('Конец работы программы.')

#NameError: name 'a' is not defined

#ZeroDivisionError - ошибка при делении на ноль
#FileNotFoundError - ошибка при попытке открыть несуществующий файл:
#RecursionError - ошибка рекурсии:
#def recursion():return recursion()

#TypeError — ошибка типа: 2 + '2'
#OverflowError - ошибка переполнения:
#math.exp(1000)

#AssertionError - ошибка утверждения

#AttributeError - ошибка атрибута, т. е. попытка сослаться на несуществующий атрибут.

try:
    file = open('file.txt')
except FileNotFoundError:
    print("Файл не найден.")
print('Продолжение работы программы...')

# Файл не найден.
# Продолжение работы программы...

try:
    a, b = map(int, input().split())
    result = a/b
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

#В Python ошибки являются объектами.

#1 0
#division by zero

#a b
#invalid literal for int() with base 10: 'a'

#Таким образом, мы можем обрабатывать разные типы ошибок и продолжать работу программы, даже если возникают исключения.

#В Python существует иерархия классов исключений, в которой базовым является класс BaseException

try:
    a, b = map(int, input().split())
    result = a / b
except ArithmeticError as e:
    print(e)
except ValueError as e:
    print(e)

#Если вместо ZeroDivisionError прописать класс Exception
# — общий для классов ZeroDivisionError и ValueError,
#то первым блоком except будут отлавливаться все типовые исключения, а блок с ValueError
#не будет выполнен:

try:
    a, b = map(int, input().split())
    result = a / b
except Exception:
    print("Общая ошибка")
except ValueError:
    print("Ошибка типа данных")

#2 e
#Общая ошибка

#При последовательности нескольких блоков except используйте
#следующее правило: сначала прописывайте блоки со
# специализированными классами исключений,
# а затем — с более общими.

# try:
#     print('Основной код.')
# except:
#     print('Код, если возникло исключение.')
# else:
#     print('Код, если не возникло исключений.')
# finally:
#     print('Код, который выполняется всегда.')

try:
    a, b = map(int, input().split())
    result = a / b
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print('Код, который выполняется, когда не возникло исключений.')
finally:
    print('Код, который выполняется всегда.')
