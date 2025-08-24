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
    '''Function will take input from user and check it for "~". if input does not have ~ or numbers it will ask another input, if input does not have ~ but have numbers -> create list of numbers (float) and send signal to continue program, if it has no numbers but have ~ any where in input it send signal to finish program, if input have, if input has numbers and ~ any where it will create list of numbers and signal do summ and finish program '''
    while True:

        user_str = input(f'\nPlease enter numbers separated by space'
                         f'\nIf you wont to finish program plese enter "~": ')
        signal = 'continue'
        user_lst = user_str.split()
        number_lst = []

        for s in user_lst:
            try:
                float(s)
                number_lst.append(float(s))

            except ValueError:

                pass
            if s == '~':
                number_lst.insert(0, '~')

        if len(number_lst) > 0:
            return number_lst
        else:
            print(f"\nYou are entered wrong value, please repeat enter prepper value")
            continue


if __name__ == '__main__':
    print(take_input())

