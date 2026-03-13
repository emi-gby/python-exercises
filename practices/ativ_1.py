def even_odd(n):
    print('even' if n % 2 == 0 else 'odd')

def division_remainder(x,y) : print(x % y)

def positive_negative_zero(n):
    print('positive' if n > 0 else 'negative' if n < 0 else 'zero')

def multiple(x,y):
    print('multiple' if x % y == 0 else 'not a multiple')

def greater_of_two(x,y):
    if x == y:
        print(f'{x} is equal to {y}')
    else:
        greater = max(x, y)
        smaller = min(x, y)
        print(f'{greater} is greater than {smaller}')

def double_triple(n):
    print(f'double of {n} = {n * 2}')
    print(f'triple of {n} = {n * 3}')

def predecessor_successor(n):
    print(f'predecessor = {n-1}')
    print(f'successor = {n+1}')

def triangle_area():
    try:
        h = float(input('Height : '))
        l = float(input('Width : '))
        print(f'Area : {h * l / 2}')
    except ValueError:
        print('Invalid values.')

def convert_temp():
    try:
        celsius = float(input('Temperature in celsius : '))
        print(f'Temperature in fahrenheit : {((celsius*9)/5)+32}')
    except ValueError:
        print('Invalid value.')

def simple_average():
    try:
        grades = [float(input(f'Grade {i + 1} : ')) for i in range(4)]
        print(f'Average : {sum(grades)/4}')
    except ValueError:
        print('Invalid value.')
