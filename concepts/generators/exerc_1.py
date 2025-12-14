#yields numbers from 1 to n.
def counter(s):
    n = 0
    for i in range(s):
        yield n
        n+=1


#yields even numbers up to n.
def even_num(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


#counts down from n to 0.
def countdown(n):
    for i in range(n+1):
        yield n
        n -= 1


#yields the first n Fibonacci numbers.
def fibonacci(n):
    if n <= 0:
        return

    a, b = 0, 1

    count = 0

    while count < n:
        yield a
        a, b = b, b + a
        count += 1


#yields squares from 0 to n
def squares(n):
    for i in range(n):
        yield i**2


#yield the length of each word one by one.
def count_length(setence):
    words = setence.split()
    for word in words:
        yield len(word)



#yields natural numbers forever.
def natural_numbers():
    n = 0
    while True:
        yield n
        n += 1



def search_error(file):
    try:
        with open(file, "r") as f:
            for line in f:
                if "error" in line.lower():
                    yield line

    except FileNotFoundError:
        print("Error: The file was not found")
    except Exception as e:
        print("An error occurred")



#-----------Pipeline----------

#yields numbers 1–n
def gen_numbers(n):
    for i in range(1,n+1):
        yield i

#filters multiples of 3
def filter_numbers(gen_numbers):
    for n in gen_numbers:
        if n % 3 == 0:
            yield n

#squares the numbers
def squares_numbers(filter_numbers):
    for n in filter_numbers:
        yield n**2


source_gen = gen_numbers(10)

filter_gen = filter_numbers(source_gen)

transformer_gen = squares_numbers(filter_gen)

for n in transformer_gen:
    print(n)
