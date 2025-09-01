#В Python мы можем принудительно вызвать исключение
# с помощью специальной инструкции raise

# raise ZeroDivisionError('division by zero')
#ZeroDivisionError: division by zero

# raise ZeroDivisionError
#ZeroDivisionError

e = ZeroDivisionError('division by zero')
# raise e
# ZeroDivisionError: division by zero

#Инструкция raise ожидает, что после нее будет объект
# класса исключения, поэтому мы можем создать свой класс
# исключений, унаследовавшись от класса Exception

# Шелл-скрипт — сценарий командной строки, или командной
# оболочки. Программа, выполняемая командной оболочкой
# операционной системы.

# Шебанг (shebang) — последовательность символов
# #!
# , которая указывает операционной системе, какую программу использовать для анализа остальной части файла.

# Пример шебанга:
#  #!/bin/bash

class ShellScriptError(Exception):
    """Общий класс исключения для скриптов"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка скрипта.'

    def __str__(self):
        return self.message


class ShellScriptEmpty(ShellScriptError):
    """Класс исключения при отсутствии кода скрипта"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл пустой.'

class ShellScriptShebag(ShellScriptError):
    """Класс исключения при отсутствии shebang"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'В файле отсутствует shebang.'

# Используем написанные исключения в классе ShellScript

class ShellScript:
    """Класс для работы с шелл-скриптами."""

    def __init__(self, script: str):
        if not script:
            raise ShellScriptEmpty
        elif script[0:2] != '#!': # Если отсутствует shebang
            raise ShellScriptShebag
        else:
            self.script = script

    def evaluate(self):
        # Код исполнения скрипта
        pass

content = ('')

try:
    script = ShellScript(content)
except ShellScriptEmpty:
    print('Отсутствует текст скрипта.')
except ShellScriptShebag:
    print('Добавьте шебанг в скрипт.')
except ShellScriptError:
    print('Ошибка при работе скрипта.')

#Отсутствует текст скрипта.

content = ('!/bin/bash')

try:
    script = ShellScript(content)
except ShellScriptEmpty:
    print('Отсутствует текст скрипта.')
except ShellScriptShebag:
    print('Добавьте шебанг в скрипт.')
except ShellScriptError:
    print('Ошибка при работе скрипта.')

#Добавьте шебанг в скрипт.

