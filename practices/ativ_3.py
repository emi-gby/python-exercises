def simple_calculator():
    try:
        x = float(input('Number 1 : '))
        y = float(input('Number 2 : '))
        op = input('Operation (+,-,*,/): ')
        if op not in '+-*/':
            raise ValueError('Invalid operation')
        result = eval(f'{x}{op}{y}')
        print(f'Result : {result}')
    except Exception:
        print('Operation failed. Enter appropriate values.')


def grade_classification():
    try:
        grades = [float(input(f'Grade {i+1} : ')) for i in range(3)]
        if any(n < 0 or n > 10 for n in grades):
            print('Invalid grade')
            return
        average = sum(grades) / 3
        if average >= 7:
            print(f'Average = {average}, status = approved')
        elif 5 <= average < 7:
            print(f'Average = {average}, status = recovery')
        else:
            print(f'Average = {average}, status = failed')
    except ValueError:
        print('Invalid value.')


def electrical_quantities():
    print('''***********************************************************
                ELECTRICAL QUANTITIES CALCULATION
***********************************************************
1. Voltage (in Volt)
2. Resistance (in Ohm)
3. Current (in Ampere)
********************************************************''')
    quantity = input('Which quantity do you want to calculate ? ')
    try:
        if quantity == '1':
            r = float(input('resistance : '))
            c = float(input('current : '))
            print(f'voltage = {r*c} volts')
        elif quantity == '2':
            t = float(input('voltage : '))
            c = float(input('current : '))
            print(f'resistance = {t/c} ohms')
        elif quantity == '3':
            t = float(input('voltage : '))
            r = float(input('resistance : '))
            print(f'current = {t/r} amperes')
        else:
            print('Invalid option.')
    except ValueError:
        print('Invalid value.')


def triangle_exists():
    try:
        x1, y1 = float(input('x1 : ')), float(input('y1 : '))
        x2, y2 = float(input('x2 : ')), float(input('y2 : '))
        x3, y3 = float(input('x3 : ')), float(input('y3 : '))
        p1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
        p2 = ((x1-x3)**2 + (y1-y3)**2)**0.5
        p3 = ((x3-x2)**2 + (y3-y2)**2)**0.5
        sides = [p1, p2, p3]
        if all(l > 0 for l in sides) and (
            (p1+p2>p3 and abs(p1-p2)<p3) or
            (p1+p3>p2 and abs(p1-p3)<p2) or
            (p3+p2>p1 and abs(p3-p2)<p1)):
            if p1 == p2 == p3:
                status = 'equilateral'
            elif len(set(sides)) == 3:
                status = 'scalene'
            else:
                status = 'isosceles'
            print(f'side 1 = {round(p1,2)}, side 2 = {round(p2,2)}, side 3 = {round(p3,2)}, status = {status}.')
        else:
            print('No triangle formed with the given points.')
    except ValueError:
        print('Invalid value.')


def descending_height():
    try:
        height = [float(input(f'Height {i+1} : ')) for i in range(3)]
        print(sorted(height, reverse=True))
    except ValueError:
        print('Invalid value.')

def delivery_logistics():
    try:
        distance = float(input('Enter the distance (km): '))
        vehicle = input('Enter the vehicle (1 - car, 2 - motorcycle or 3 - bicycle):')
        if distance > 0 and vehicle in ('1', '2', '3'):
            if vehicle == '1':
                print(f'Total car ride price: {10 + 5*distance}')
            elif vehicle == '2':
                print(f'Total motorcycle ride price: {10 + 3.5*distance}')
            else:
                print(f'Total bicycle ride price: {10 + 2*distance}')
        else:
            print('Invalid distance or vehicle.')
    except ValueError:
        print('Invalid value.')
