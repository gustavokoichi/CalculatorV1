from util import *
from operations import *

MENU_DICT = {1: 'Sum', 2: 'Subtraction', 3: 'Multiply', 4: 'Division', 5: 'Power', 6: 'Factorial', 7: 'Leave program'}

while True:
    choice = menu(MENU_DICT)
    if choice == len(MENU_DICT):
        print()
        print('LEAVING PROGRAM')
        print()
        break
    for k, v in dict.items(MENU_DICT):
        if choice == k and choice != len(MENU_DICT):
            print(f'Your choose: {v}')
            print()
            if choice == 1:
                sum()
            if choice == 2:
                subtraction()
            if choice == 3:
                multiply()
            if choice == 4:
                division()
            if choice == 5:
                power()
            if choice == 6:
                x = read_int('Factorial of: ')
                factorial(x)
            break
