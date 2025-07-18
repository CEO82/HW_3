'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
'''

while True:
    try:
        user_n1 = float(input("Enter the number you want to divide: "))
        break
    except ValueError:
        print("You are entered wrong value, please enter number.")

while True:
    try:
        user_n2 = float(input("Enter the number you want to divide by: "))
        if user_n2 == 0:
            print("You are entered 0, division by 0 is prohibited, please enter another number.")
            continue
        else:
            break
    except ValueError:
        print("You are entered wrong value, please enter number.")


def func_division(a1, a2):
    return a1 / a2


print(f'\nThe result of division is:\n{func_division(user_n1, user_n2)}')
