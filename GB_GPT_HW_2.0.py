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

    pass




test_string = '4 + 3 * 2 - 5 + 20 * 22 / 5 ** 2 - 2 ** 0.5'

test_list = test_string.split()

''' ['4', '+', '3 * 2', '-', '5', '+', '20', '*', '22', '/', '5', '**', '2', '-', '2', '**', '0.5'] '''

print(test_list)

operators_list = ['**', '*', '/', '+', '-']

for oper_symb in operators_list:
    while True:  # For / operation!

        if test_list.count(oper_symb) > 0:
            ind_n1 = test_list.index(oper_symb) - 1
            ind_op = test_list.index(oper_symb)
            ind_n2 = test_list.index(oper_symb) + 1

            n1 = float(test_list[ind_n1])
            op = test_list[ind_op]
            n2 = float(test_list[ind_n2])

            result_numb = operations(n1, op, n2)

            test_list.pop(ind_n1)
            test_list.pop(ind_n1)
            test_list.pop(ind_n1)

            test_list.insert(ind_n1, result_numb)

            continue

        else:
            print(test_list)
            break


