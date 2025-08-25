'''5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
'''

'''special symbol will be ~'''

if __name__ != '__main__':
    print(f'\nThis file is not for import!!!')

def take_input():
    '''Function will take input from user if user string contain numbers or/and symbol "~" it will create list of float numbers where "~" is the first symbol, if i contain numbers with out ~ it will create lift of float numbers, if it does not contain numbers or/and "~" it will ask input again '''
    while True:

        user_str = input(f'\nPlease enter numbers separated by space'
                         f'\nIf you want to finish program please enter "~": ')
        signal = 'continue'
        user_lst = user_str.split()
        number_lst = []

        if user_str.count('~') >= 1:
            number_lst.insert(0, '~')

        for s in user_lst:

            try:
                float(s)
                number_lst.append(float(s))

            except ValueError:
                pass
            '''if s == '~':
                number_lst.insert(0, '~')'''

        if len(number_lst) > 0:
            return number_lst
        else:
            print(f"\nYou are entered wrong value, please repeat input"
                  f"\nand enter proper value"
                  f"\nor for finish program enter ~ ")
            continue

def check_and_summ():
    '''Function take input from take_input() function and check it for rights to do summ, do summ and finish program or just finish program'''

    num_summ = 0.0

    while True:
        lst_fr_chk_sum = take_input()
        if lst_fr_chk_sum[0] == '~' and len(lst_fr_chk_sum) == 1:
            return print(f'\nProgram finished'
                         f'\nsumm of numbers = {num_summ}')
        elif lst_fr_chk_sum[0] == '~' and len(lst_fr_chk_sum) > 1:
            num_summ = num_summ + sum(lst_fr_chk_sum[1:])
            return print(f'\nProgram finished'
                         f'\nsumm of numbers = {num_summ}')
        else:
            num_summ = num_summ + sum(lst_fr_chk_sum)
            print(f'\nCurrent summ = {num_summ}')
            continue





if __name__ == '__main__':

    check_and_summ()

