'''7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
написанную ранее функцию int_func().
'''


if __name__ != '__main__':
    print(f'\nThis file is not for import!!!')

import re

def int_func(user_str):
    '''This function request string from take_input() function and make this string title'''
    new_str = user_str
    return new_str.title()



def take_input():
    '''This function ask user to input some word in latin letters, checking than all symbols are Latin letters if not it will repeat input'''
    while True:
        user_input = input(f'\nPlease enter several words using by Latin letters'
                           f'\n separated by spaces, but no other symbols: ')
        if re.fullmatch(r'[A-Za-z]+( [A-Za-z]+)*', user_input):
            return user_input
        else:
            print(f'\nYou are entered wrong value, please repeat enter ')
            continue

if __name__ == "__main__":
    print(f'\nThe words in title wil be -> {int_func(take_input())}')