'''Мини-калькулятор со встроенными проверками
Напиши программу, которая:
1.	Запрашивает у пользователя строку вида:
2.	число операция число
Например:
15 + 7
10 / 0
3 ** 4
3.	Поддерживает операции: +, -, *, /, ** (возведение в степень).
4.	Использует функции для:
o	парсинга строки;
o	выполнения операции;
o	запуска основного цикла работы калькулятора.
5.	Обрабатывает ошибки через try / except:
o	деление на ноль;
o	неверный ввод (например, a + b);
o	неизвестная операция.
6.	Работает в цикле до тех пор, пока пользователь не введет exit.
Теперь калькулятор должен уметь работать не только с двумя числами, а с выражением любой длины.
📌 Пример:
Ввод:  2 + 3 * 4 - 5 / 2
Вывод:  11.5
Условия:
1.	Пользователь вводит строку выражения (2 + 3 * 4 - 5 / 2).
2.	Нужно правильно обработать приоритет операций (* и / выше, чем + и -, а ** ещё выше).
3.	Ошибки по-прежнему обрабатываются (деление на 0, неправильный ввод, лишние символы).
4.	Работает в цикле, выход по exit.
5.	Нельзя использовать eval() и exec() — нужно написать логику самому.
'''
import operator
import  re

if __name__ != '__main__':
    print(f'\nThis file not for import!!!')

if __name__ == '__main__':

    def operations(user_lst: list)-> float:
        ''' func receives list with three symbols - first symbol is first number, second is operator and third is second number. As result function return result of operation with thous numbers according to second symbol '''

        operator_list = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow,
        }

        return float(operator_list[user_lst[1]](user_lst[0], user_lst[2]))

    def user_input():
        ''' description '''

        while True:
            user_string = input(f'\nPlease enter expression in format:'
                                f'\nnumber space operator space number,'
                                f'\nas example'
                                f'\n5 + 3: ')

            if re.fullmatch(r'[0-9-]* [*+-/] [0-9-]*', user_string):
                return user_string
            elif user_string.lower() == 'exit':
                print(f'\nProgram finished.')
                break
            else:
                print(f'\nYou are entered something wrong, please try again')

    def make_list(user_string: str)-> list:
        ''' description '''
        user_list = user_string.split()
        try:
            check1 = float(user_list[0])
            check_1 = 'good'
        except ValueError:
            check_1 = 'bad'

        try:
            check2 = float(user_list[2])
            check_2 = 'good'
        except ValueError:
            check_2 = 'bad'

        if check_1 and check_2 == 'good':
            return user_list
        else:
            print(f'\nYou are entered something wrong, please try again')
            user_input()





    print(user_input())





