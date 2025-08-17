'''5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
'''

if __name__ != '__main__':
    print(f'\nThis file is not for import!!!')

def sum_func(lst_for_sum: str)-> float:
    return sum(lst_for_sum)

def make_list_of_floats(user_list: list)-> list:
    '''This function should check that list contain any number/s if it does not make aalert and reqest another list. '''
    for n in user_list:
        if n
    pass

def go_stop_check(check_lst: list)-> str:
    '''Function checking rights to continue program'''
    if check_lst == '~':
        return 'hard_stop'
    elif check_lst[-1] == '~':
        return 'sum_and_stop'
    else:
        return 'continue'

def get_string()-> list:
    '''Function that ask user to input numbers separated by spaces, checking this string for numbers or special symbol ~, if no numbers or symbol ~ than function will ask to enter input again, if input valid return list with numbers and symbol ~ if present '''
    user_str = input(f''
                     f'\nPlease enter only numbers separated by spaces,'
                     f'\nIf you want finish the program please enter only symbol ~ '
                     f'\nIf you will input numbers and at the end you will put symbol ~ , program will do last calculation and be finished after it')
    return user_str.split()




