'''

*
Мини-калькулятор со встроенными проверками
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
*
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
*
'''

if __name__ != '__main__':
    print(f'\nThis file not for import!!!')

if __name__ == '__main__':

    import operator
    import re


    def operations(n1, op, n2):
        ''' This function receives  three arguments firs number - n1, operation - op, second number - n2. And will return result of operation. If any errors appear it will show message with original string and message that user entered something wrong and send user to repeat input '''

        print(f'{n1}  {op}  {n2}')
        operator_list = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow,
        }

        return operator_list[op](n1, n2)

    def user_input():

        ''' This function take input from user, check it for correct format and for stop word "exit". If user string format correct, then return user string, if not check for stop word if user string contain only stop word in any register program will stop, if not it wil ask to repeat input again  '''

        while True:
            user_string = input(f'\nPlease enter expression in format:'
                                f'\nnumber space operator space number,'
                                f'\nbut without brackets'
                                f'\nas example'
                                f'\n5 + 3 * 4 -2 ** 2 / 3: ')

            if re.fullmatch(r'-?\d+\.?\d* (\+|-|/|\*{0,2}) -?\d+\.?\d*', user_string):
                return user_string
            elif user_string.lower() == 'exit':
                return 'exit'

            else:
                print(f'\nYou are entered something wrong, please try again')

    def make_list(user_string: str)-> list:
        ''' This function receives string (supposed from user_input() function) in following format: number space operator symbol space number and make from it list of three position. Next it will check that positions 1 and 3 are numbers, if not call back  user_input() function, if there are numbers it wil create list in format [float, operator symbol, float] and return it'''
        user_list = user_string.split()
        try:
            n1 = float(user_list[0])
            n2 = float(user_list[2])
            return [n1, user_list[1], n2]
        except ValueError:
            print(f'\nYou are entered something wrong, please try again')
            return 'false_list'


    test_string = '4 + 3 * 2 - 5 + 20 * 22 / 5 ** 2 - 2 ** 0.5'

    test_list = test_string.split()

    ''' ['4', '+', '3 * 2', '-', '5', '+', '20', '*', '22', '/', '5', '**', '2', '-', '2', '**', '0.5'] '''

    print(test_list)


    def operation_sequence(user_list: list):
        ''' This function receives prepaired list of floats and operators and step by step make operations by function 'operations()' in user expression in order according to operation rang which is given by operators_list'''

        operators_list = ['**', '*', '/', '+', '-']

        for oper_symb in operators_list:
            while True:  # For / operation!

                if user_list.count(oper_symb) > 0:
                    ind_n1 = user_list.index(oper_symb) - 1
                    ind_op = user_list.index(oper_symb)
                    ind_n2 = user_list.index(oper_symb) + 1

                    n1 = float(user_list[ind_n1])
                    op = user_list[ind_op]
                    n2 = float(user_list[ind_n2])

                    result_numb = operations(n1, op, n2)

                    user_list.pop(ind_n1)
                    user_list.pop(ind_n1)
                    user_list.pop(ind_n1)

                    user_list.insert(ind_n1, result_numb)

                    continue

                else:
                    print(user_list)
                    break


