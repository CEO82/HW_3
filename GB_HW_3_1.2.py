'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
'''


def func_get_number_float(prompt):
    while True:
        try:
            float_number = float(input(prompt))
            return float_number
        except ValueError:
            print("You are entered wrong value, please enter number.")


def func_division(n1, n2):
    try:
        result = n1 / n2
        return result
    except ZeroDivisionError:
        print(
            f'\nYou are trying divide by zero ({n1} / {n2}) it is prohibited, \nplease re start the program and enter correct numbers')
        return 'zero_division'



while True:
    user_number1 = func_get_number_float('Enter the first number for equation: ')
    user_number2 = func_get_number_float('Enter the second number for equation: ')

    n = func_division(user_number1, user_number2)
    if n != 'zero_division':
        print(f'\nResult of division is {n:.2f}')
        break
    else:
        choise = input(f'\nIf you want to re enter numbers enter Y, \nIf not enter N: ').lower()
        if choise == 'y':
            continue
        else:
            break


