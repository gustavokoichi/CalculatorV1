def sum(x=0, y=0):
    x = float(input('First number: '))
    y = float(input('Second number: '))
    print()
    total = x + y
    return print(f'{x} + {y} = {total}')

def subtraction(x=0, y=0):
    x = float(input('First number: '))
    y = float(input('Second number: '))
    print()
    total = x - y
    return print(f'{x} - {y} = {total}')

def multiply(x=0, y=0):
    x = float(input('First number: '))
    y = float(input('Second number: '))
    print()
    total = x * y
    return print(f'{x} x {y} = {total}')

def division(x=0, y=0):
    x = float(input('Numerator: '))
    y = float(input('Denominator: '))
    print()
    total = x / y
    return print(f'{x} / {y} = {total}')

def power(x=0, y=0):
    x = float(input('Base: '))
    y = float(input('Exponent: '))
    print()
    total = x ** y
    return print(f'{x} ** {y} = {total}')

def factorial(x):
    f = 1
    for x in range(2, x + 1):
        f *= x
    return print(f)

