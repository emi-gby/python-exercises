def simple_count():
    for i in range(1, 21):
        print(i)

def multiplication_table():
    try:
        number = int(input('Enter an integer number : '))
        for i in range(1, 11):
            print(f'{number}*{i} = {number*i}')
    except ValueError:
        print('Please enter a valid integer number.')

def sum_numbers():
    """Calculates and prints the sum of all numbers from 1 to n, where n is given by the user."""
    try:
        n = int(input('Enter a number : '))
        if n < 1:
            print('Please enter a number greater than zero.')
            return
        print(f'Sum of all numbers = {sum(range(1, n+1))}')
    except ValueError:
        print('Please enter a valid integer number.')

def countdown():
    try:
        n = int(input('Enter a number : '))
        for i in range(n, -1, -1):
            print(i)
    except ValueError:
        print('Invalid value.')

def factorial():
    """Calculates and prints the factorial of n (n!), where n is provided by the user."""
    try:
        n = int(input('Enter a number : '))
        if n < 0:
            print('Please enter a non-negative number.')
            return
        fact = 1
        for i in range(2, n+1):
            fact *= i
        print(f'Factorial = {fact}')
    except ValueError:
        print('Please enter a valid integer number.')

def digit_count():
    try:
        n = int(input('Enter an integer number : '))
        print(f'This number has {len(str(abs(n)))} digits')
    except ValueError:
        print('Invalid value.')

def prime_number():
    try:
        n = int(input('Enter a number : '))
        if n < 2:
            print('Not prime')
            return
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                print('Not prime')
                return
        print('Prime number')
    except ValueError:
        print('Invalid value.')

def fibonacci():
    try:
        n = int(input('Enter a number : '))
        fib = [1, 1][:n]
        if n <= 0:
            print([])
            return
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        print(fib)
    except ValueError:
        print('Invalid value.')

def perfect_number():
    try:
        n = int(input('Enter a number : '))
        divisors = [i for i in range(1, n) if n % i == 0]
        if sum(divisors) == n:
            print('perfect number')
        else:
            print('number is not perfect')
    except ValueError:
        print('Invalid value.')


def average_n_numbers():
    try:
        n = int(input('Enter a Number N : '))
        if n < 1:
            print('Please enter a number greater than zero.')
            return
        numbers = []
        for i in range(n):
            while True:
                try:
                    num = float(input(f'Enter number {i+1} : '))
                    numbers.append(num)
                    break
                except ValueError:
                    print('Please enter a valid number.')
        average = sum(numbers)/n
        print(f'Arithmetic average = {average:.2f}')
    except ValueError:
        print('Please enter a valid integer number.')

def arithmetic_progression():
    try:
        first_term = float(input('Enter the first term : '))
        quantity_terms = int(input('Enter the number of terms : '))
        ratio = float(input('Enter the ratio : '))
        progression = [first_term + i * ratio for i in range(quantity_terms)]
        print(progression)
    except ValueError:
        print('Invalid value.')

def swimming_system():
    try:
        system_dict = {float(input(f'Enter time {i+1} : ')): input(f'Enter name {i+1} : ') for i in range(7)}
        time_list = list(system_dict.keys())
        print(f'a.Player with best time : {system_dict[min(time_list)]}')
        print(f'b.Player with worst time : {system_dict[max(time_list)]}')
        print(f'c.Average time : {round(sum(time_list)/ 7,2)}')
        quantity_players_1215 = sum(12 < time < 15 for time in time_list)
        print(f'd.Quantity of athletes with time between 12s and 15s : {quantity_players_1215}')
    except ValueError:
        print('Invalid value.')

def opinion_survey():
    try:
        n = int(input('Enter the number of customers : '))
        age_rating = [(int(input(f'Enter age of customer {i+1} : ')), int(input(f'Enter satisfaction rating of customer {i+1} : '))) for i in range(n)]
        age_list = [age for age, _ in age_rating]
        rating_list = [rating for _, rating in age_rating]
        satisfied_customers = [(age, rating) for age, rating in age_rating if rating >= 4]
        dissatisfied_customer = sum(rating <= 2 for rating in rating_list)
        if satisfied_customers:
            average_age_satisfied = sum(age for age, _ in satisfied_customers) / len(satisfied_customers)
        else:
            average_age_satisfied = 0
        print(f'average age of satisfied customers = {average_age_satisfied}')
        print(f'percentage of dissatisfied customers = {dissatisfied_customer/n*100}%')
        print(f'overall average rating = {sum(rating_list)/n}')
    except ValueError:
        print('Invalid value.')

opinion_survey()
