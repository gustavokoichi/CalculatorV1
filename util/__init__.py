def read_int(num_int):
    while True:
        try:
            num_int = int(input(num_int))
        except ValueError:
            print('ERROR!. Input a valid number!')
            continue
        except KeyboardInterrupt:
            print('\nERROR! Interrupted by user!')
            return 0
        else:
            return num_int

def read_float(num_float):
    while True:
        try:
            num_float = float(input(num_float))
        except ValueError:
            print('ERROR!. Input a valid number!')
            continue
        except KeyboardInterrupt:
            print('\nERROR! Interrupted by user!')
            return 0
        else:
            return num_float

def lines30():
    print('-' * 30)


def header(msg):
    lines30()
    print(msg.center(30))


def menu(dict):
    header('MENU')
    lines30()
    for k, v in dict.items():
        print(f'{k} - {v}')
    lines30()
    opt = read_int('Choose a number from menu corresponding to a operation desired: ')
    return opt
    