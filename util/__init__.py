def lines30():
    print('-' * 30)

def header(msg):
    lines30()
    print(msg.center(30))

def menu(dict):
    header('MENU')
    for k, v in dict.items():
        print(f'{k} - {v}')
    print()

def option(n,dict):
    for k, v in dict.items():
        if n == k:
            print(f'Your choice is: {v}')
            break
