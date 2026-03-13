def convert_time(n) : print(f'{n//60} hours and {n%60} minutes')

def weighted_average():
    try:
        grades_weights = [(float(input(f'Grade {i+1}: ')), float(input(f'Weight {i+1}: '))) for i in range(3)]
        total_grade = sum(n * p for n, p in grades_weights)
        total_weight = sum(p for _, p in grades_weights)
        print(f'Weighted average : {total_grade/total_weight}')
    except ValueError:
        print('Invalid value.')


def swap_variables(a,b):
    a = a + b
    b = a - b
    a = a - b
    print(f'A = {a}, B = {b}')

def bhaskara_root(a,b,c):
    delta = b**2 - 4 * a * c
    if delta > 0:
        root = delta ** 0.5
        print(f'Root 1 : {(-b+root)/(2*a)}, Root 2 : {(-b-root)/(2*a)}')
    elif delta == 0:
        print(f'Root : {-b/(2*a)}')
    else:
        print('Imaginary root')


def convert_units(m) : print(f'{m}m = {m*100}cm, {m*1000}mm, {m/1000}km')


def invert_number(n):
    u = n // 100
    d = (n % 100) // 10
    c = n % 10
    print(f'New number : {c}{d}{u}')

def simple_interest():
    try:
        c = float(input('Capital : '))
        i = float(input('Interest : '))
        t = float(input('Time(months) : '))
        print(f'Amount : {c + (c*i*t)}')
    except ValueError:
        print('Invalid value.')
