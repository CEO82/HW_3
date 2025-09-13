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

test_string = '4 + 3 * 2 - 5 + 20 * 22 / 5 ** 2 - 2 ** 0.5'
test_list = test_string.split()

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