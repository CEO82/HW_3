'''6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
'''

if __name__ != '__main__':
    print(f'\nThis file is not for import!!!')

import re

def int_func():
    '''This function request string from take_input() function and make this string title'''
    new_str = take_input()
    return new_str.title()



def take_input():
    '''This function ask user to input some word in latin letters, checking than all symbols are Latin letters if not it will repeat input'''
    while True:
        user_input = input(f'\nPlease enter any word by Latin letters, '
                           f'\nwith no spaces or any other symbols: ')
        if re.fullmatch(r'[A-Za-z]+', user_input):
            return user_input
        else:
            print(f'\nYou are entered wrong value, please repeat enter ')
            continue

if __name__ == "__main__":
    print(f'\nThe word in title is -> {int_func()}')
