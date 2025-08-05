'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
'''


def biggest_sum(
        a1: float,
        a2: float,
        a3: float
        )-> float:
    return sum(sorted([a1, a2, a3], reverse=True)[:2])

def input_digit_check(
        enter_txt: str,
        error_txt: str
        )-> float:
    while True:
        try:
            value = float(input(f'\n{enter_txt}'))
            return value
        except ValueError:
            print(f'\n{error_txt}')

u_num_1 = input_digit_check(
    'Please enter first number: ',
    'You are entered wrong value, please try again '
    )

u_num_2 = input_digit_check(
    'Please enter second number: ',
    'You are entered wrong value, please try again '
    )

u_num_3 = input_digit_check(
    'Please enter third number: ',
    'You are entered wrong value, please try again '
    )

print(f'\nThe sum of two biggest number is '
      f'{biggest_sum(u_num_1, u_num_2, u_num_3)}')
