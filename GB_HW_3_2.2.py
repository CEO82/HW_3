'''2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой.
'''


def print_identity(surname=None, name=None, birth_date=None, place_of_living=None, phone_number=None, email=None):
    print(
        f'\nThe person name is {name} \nand his surname is {surname}, \nhe/she was born in {birth_date}, \nfor now hi/she is living in {place_of_living}, \nhere is his/her contact information, \nphone number is {phone_number} \nand email is {email}')
    pass


print_identity(name='Vova', surname='Petrov', birth_date='01.10.1987', phone_number='+4423459854',
               place_of_living='London', email='tut@gmail.com')

def check_for_letters():
    pass


while True:
    enter_name = str(input(f'\nPlease enter customer first name: '))
    if enter_name.isalpha() == True:
        break
    else:
        print(f'\nYou are entered not letters, try to enter first name again: ')
        continue

while True:
    enter_surname = str(input(f'\nPlease enter customer first surname: '))
    if enter_surname.isalpha() == True:
        break
    else:
        print(f'\nYou are entered not letters, try to enter surname again: ')
        continue

from datetime import datetime

while True:
    enter_birth_date = str(input(f'\nPlease enter customer birth_date in folowing format - dd.mm.yyyy: '))
    try:
        datetime.strptime(enter_birth_date, '%d.%m.%Y')
        break
    except ValueError:
        print(f'\nYou are entered not date, please enter date in folowing format - dd.mm.yyyy: ')

import re

while True:
    enter_phone_number = input(f'\nPlease enter phone number in folowing format - +xxxxxxxxxx\n(+, country code, phone number with no dash, dots, spaces, slash): ')
    if re.fullmatch(r'\+?\d{7,15}', enter_phone_number) != None:
        break
    else:
        print(f'\nYou are entered not phone number, please enter phone number in folowing format - +xxxxxxxxxx: ')
        continue

while True:
    enter_place_of_living = str(input(f'\nPlease enter customer place_of_living: '))
    if enter_place_of_living.isalpha() == True:
        break
    else:
        print(f'\nYou are entered not letters, try to enter place of living again: ')
        continue


from email_validator import validate_email, EmailNotValidError

while True:
    enter_email = str(input(f'\nPlease enter customer email: '))
    try:
        email_check = validate_email(enter_email, check_deliverability=False)
        break
    except EmailNotValidError:
        print(f'\nYou are entered not email, please enter email: ')

print_identity(name=enter_name, surname=enter_surname, birth_date=enter_birth_date, phone_number=enter_phone_number,
               place_of_living=enter_place_of_living, email=enter_email)