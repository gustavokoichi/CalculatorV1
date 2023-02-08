from util import read_float

def sum(x=0, y=0):
    x = read_float('First number: ')
    y = read_float('Second number: ')
    print()
    total = x + y
    return print(f'{x} + {y} = {total}')

def subtraction(x=0, y=0):
    x = read_float('First number: ')
    y = read_float('Second number: ')
    print()
    total = x - y
    return print(f'{x} - {y} = {total}')

def multiply(x=0, y=0):
    x = read_float('First number: ')
    y = read_float('Second number: ')
    print()
    total = x * y
    return print(f'{x} x {y} = {total}')

def division(x=0, y=0):
    x = read_float('Numerator: ')
    y = read_float('Denominator: ')
    print()
    total = x / y
    return print(f'{x} / {y} = {total}')

def power(x=0, y=0):
    x = read_float('Base: ')
    y = read_float('Exponent: ')
    print()
    total = x ** y
    return print(f'{x} ** {y} = {total}')

def factorial(x):
    f = 1
    for x in range(2, x + 1):
        f *= x
    return print(f)

