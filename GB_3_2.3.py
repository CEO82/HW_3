'''2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой.
'''
from typing import Optional, Callable
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
import re


def print_identity(
        surname: Optional[str] = None,
        name: Optional[str] = None,
        birth_date: Optional[str] = None,
        place_of_living: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None
        ) -> None:
    return (
        f'\nThe person name is {name} '
        f'\nand his surname is {surname}, '
        f'\nhe/she was born in {birth_date}, '
        f'\nfor now hi/she is living in {place_of_living}, '
        f'\nhere is his/her contact information, '
        f'\nphone number is {phone_number} '
        f'\nand email is {email}'
        )

def input_output_for_validators(
        input_prompt: Optional[str],
        error_prompt: Optional[str],
        validator_func: Callable[[str],bool]
        ):
    while True:
        user_input = input(f'\n{input_prompt}')
        if validator_func(user_input):
            return user_input
        print(f'\n{error_prompt}')


def is_alpha(value: str) -> bool:
   return value.isalpha()

def check_date(value: str)-> bool:
    while True:
        try:
            datetime.strptime(value, '%d.%m.%Y')
            return True
        except (ValueError, TypeError):
            return False

def check_email(value: str)-> bool:
    try:
        validate_email(value, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False

def check_phone_number(value: str)-> bool:
    if re.fullmatch(r'\+?\d{7,15}', value) != None:
        return True
    else:
        return False


enter_name = input_output_for_validators(
    'Enter the first name: ',
    'You are entered not letters, try to enter first name again',
    is_alpha
    )

enter_surname = input_output_for_validators(
    'Please enter customer surname: ',
    'You are entered not letters, try to enter surname again',
    is_alpha
    )

enter_place_of_living = input_output_for_validators(
    'Please enter customer place of living: ',
    'You are entered not letters, try to enter place of living again',
    is_alpha
    )


birth_date = input_output_for_validators(
    'Please enter customer birth_date in following format - dd.mm.yyyy: ',
    'You are entered not date, please enter date in following format - dd.mm.yyyy: ',
    check_date
    )


customer_email = input_output_for_validators(
    'Please enter customer email: ',
    'you are entered not email, please enter email: ',
    check_email
    )

customer_phone_number = input_output_for_validators(
    'Please enter phone number in following format - +xxxxxxxxxx\n(+, country code, phone number with no dash, dots, spaces, slash): ',
    'You are entered not phone number, please enter phone number in following format - +xxxxxxxxxx: ',
    check_phone_number
    )

print(print_identity(
    surname = enter_surname,
    name = enter_name,
    birth_date = birth_date,
    place_of_living = enter_place_of_living,
    phone_number = customer_phone_number,
    email = customer_email
    ))
