'''4. Программа принимает действительное положительное число x
и целое отрицательное число y.
Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения
числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
'''

if __name__ != '__main__':
    print(f'\nThis file is not for import!!!')

def exponentiation(base: float, exponent: int)-> float:
    exponent = abs(exponent) - 1
    step = base
    while exponent > 0:
        base = base * step
        exponent -= 1

    return 1 / (base)

def negative_int_only(input_txt: str, error_txt: str)-> int:
    while True:
        user_input = input(f'\n{input_txt}')
        try:
            user_input = int(user_input)
            if user_input < 0:
                return user_input
            else:
                print(f'\n{error_txt}')

        except ValueError:
            print(f'\n{error_txt}')


def any_positive_number(input_txt: str, error_txt: str)-> float:
    while True:
        user_input = input(f'\n{input_txt}')
        try:
            user_input = float(user_input)
            if user_input > 0:
                return user_input
            else:
                print(f'\n{error_txt}')

        except ValueError:
            print(f'\n{error_txt}')

if __name__ == '__main__':

    us_base = any_positive_number(
        'Please enter value of base, it should be any positive number: ',
        'You are entered something wrong, please try again'
        )

    us_exponent = negative_int_only(
        'Please enter value of exponent, it should be negative integer number: ',
        'You are entered something wrong, please try again'
        )

    power = exponentiation(us_base, us_exponent)

    print(f'\nThe result of exponentiation is \n{power}')
