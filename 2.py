# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class ZeroError(Exception):
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    inp_data = input('Введите делимое:')
    inp_data_2 = input('Введите делитель:')

    try:
        res = int(inp_data) / int(inp_data_2)
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    else:
        print(f"Все хорошо. Результат - {res}")
    finally:
        print("Программа завершена")





