import operator
import re
def operations(n1, op, n2):
    ''' This function receives three arguments firs number - n1, operation - op, second number - n2. And will return result of operation. If any errors appear it will show message with original string and message that user entered something wrong and send user to repeat input '''
    print(f'{n1} {op} {n2}')
    operator_list = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow, }

    return operator_list[op](n1, n2)
    pass

def user_input():

    ''' This function take input from user, check it for correct format and for stop word "exit". If user string format correct, then return user string, if not check for stop word if user string contain only stop word in any register program will stop, if not it wil ask to repeat input again  '''

    while True:
        user_string = input(f'\nPlease enter expression in format:'
                            f'\nnumber space operator space number,'
                            f'\nbut without brackets'
                            f'\nas example'
                            f'\n5 + 3 * 4 -2 ** 2 / 3: ')
        user_list = re.findall()
        if re.fullmatch(r'-?\d+\.?\d* (\+|-|/|\*{0,2}) -?\d+\.?\d*', user_string):
            return user_string
        elif user_string.lower() == 'exit':
            return 'exit'

        else:
            print(f'\nYou are entered something wrong, please try again')




test_string = '4 + 3 * 2 - 5 + 20 * 22 / 5 ** 2 - 2 ** 0.5'
test_list = test_string.split()

print(user_input())

print(test_string)

''' ['4', '+', '3 * 2', '-', '5', '+', '20', '*', '22', '/', '5', '**', '2', '-', '2', '**', '0.5'] '''
print(test_list)
operators_list = ['**', '*', '/', '+', '-']
for oper_symb in operators_list:
    while True:
        #print(test_list)
        if test_list.count(oper_symb) > 0:
            ind_n1 = test_list.index(oper_symb) - 1
            ind_op = test_list.index(oper_symb)
            ind_n2 = test_list.index(oper_symb) + 1

            n1 = float(test_list[ind_n1])
            op = test_list[ind_op]
            n2 = float(test_list[ind_n2])

            result_numb = operations(n1, op, n2)

            test_list.pop(ind_n1)
            test_list.pop(ind_n1)
            test_list.pop(ind_n1)

            test_list.insert(ind_n1, result_numb)

            continue

        else:
            print(test_list)
            break