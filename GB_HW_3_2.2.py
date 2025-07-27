'''2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой.
'''
from typing import Optional


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



print(print_identity(
        name='Vova',
        surname='Petrov',
        birth_date='01.10.1987',
        phone_number='+4423459854',
        place_of_living='London',
        email='tut@gmail.com'
        ))


def check_for_letters(
        input_question: Optional[str] = None,
        repeat_question: Optional[str] = None
        ) -> str:
    while True:
        user_input = str(input(f'\n{input_question}'))
        if user_input.isalpha():
            return user_input
        else:
            print(f'\n{repeat_question}')
            continue


enter_name = check_for_letters(
    input_question = 'Enter the first name: ',
    repeat_question = 'You are entered not letters, try to enter first name again'
    )

enter_surname = check_for_letters(
    input_question = 'Please enter customer surname: ',
    repeat_question = 'You are entered not letters, try to enter surname again')

enter_place_of_living = check_for_letters(
    input_question = 'Please enter customer place of living: ',
    repeat_question = 'You are entered not letters, try to enter place of living again')

from datetime import datetime


def check_date(
        input_question: Optional[str] = None,
        repeat_question: Optional[str] = None
        ) -> str:
    while True:
        birth_date = str(input(f'\n{input_question}'))
        try:
            datetime.strptime(birth_date, '%d.%m.%Y')
            return birth_date
        except (ValueError, TypeError):
            print(f'\n{repeat_question}')
            continue


birth_date = check_date(
    input_question = 'Please enter customer birth_date in following format - dd.mm.yyyy: ',
    repeat_question = 'You are entered not date, please enter date in following format - dd.mm.yyyy: ')

from email_validator import validate_email, EmailNotValidError


def check_email(
        input_question: Optional[str] = None,
        repeat_question: Optional[str] = None
        ) -> str:
    while True:
        customer_email = input(f'\n{input_question}')
        try:
            email_check = validate_email(customer_email, check_deliverability=False)
            return customer_email
        except EmailNotValidError:
            print(f'\n{repeat_question}')


customer_email = check_email(
    input_question = 'Please enter customer email: ',
    repeat_question = 'you are entered not email, please enter email: ')

import re


def check_phone_number(
        input_question: Optional[str] = None,
        repeat_question: Optional[str] = None
        ) -> str:
    while True:
        enter_phone_number = input(f'\n{input_question}')
        if re.fullmatch(r'\+?\d{7,15}', enter_phone_number) != None:
            return enter_phone_number
        else:
            print(f'\n{repeat_question}')
            continue


customer_phone_number = check_phone_number(
    input_question = 'Please enter phone number in following format - +xxxxxxxxxx\n(+, country code, phone number with no dash, dots, spaces, slash): ',
    repeat_question = 'You are entered not phone number, please enter phone number in following format - +xxxxxxxxxx: ')

print(print_identity(
    surname = enter_surname,
    name = enter_name,
    birth_date = birth_date,
    place_of_living = enter_place_of_living,
    phone_number = customer_phone_number,
    email = customer_email
    ))
