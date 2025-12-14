from time import time


#Simple decorator that prints a message before the function
def print_message(func):
    def wrapper():
        print("Executing function...")
        func()
        print("Function completed.")

    return wrapper
    

@print_message
def greet1():
    print("Hello")

#greet1

#-------------------------------------------------------------------

#Function call counter


def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        func()
        print(f"Funcion Called {count} time(s).")


    return wrapper


@count_calls
def greet2():
    print("Hello")

#greet2()
#greet2()
#greet2()


#-------------------------------------------------------------------

#Timing decorator
def timer(func):
    def wrapper(*args, **kwargs):
        initial_time = time()
        func()
        final_time = time()
        print(f"This function took {final_time-initial_time} seconds")

    return wrapper

@timer
def math_calc():
    print(sum(range(1000000)))

#math_calc()

#-------------------------------------------------------------------

