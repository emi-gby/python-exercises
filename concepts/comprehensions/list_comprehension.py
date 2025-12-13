squares = [x**2 for x in range(1,11)]


even_num = [x for x in range(1,21) if x%2 != 0]


words = ["python", "java", "c++", "go"]
upper_words = [word.upper() for word in words]



#Filter positive numbers
nums = [-5, 3, -1, 10, 0, 7]
pos_num = [x for x in nums if x >= 0]



#Remove empty stringsc
data = ["apple", "", "banana", "", "cherry"]
data_not_empty = [text for text in data if len(text) != 0]


#Flatten a list
matrix = [[1, 2], [3, 4], [5, 6]]
single_matrix = [x for line in matrix for x in line ]



#"Fizz" if divisible by 3 | "Buzz" if divisible by 5 | "FizzBuzz" if divisible by both
fizz_buzz = ["FizzBuzz" if(x%3==0 and x%5==0) else "Fizz" if(x%3==0) else "Buzz" if(x%5==0) else x for x in range(1,21)]



#List of user ages and only adults (18+).
ages = [12, 25, 17, 30, 16, 40]
older_18 = [a for a in ages if a>=18]


#Remove empty values before processing data.
form_inputs = ["John", False, None, "Alice", " ", "Bob"]
cleaned_inputs = [
    item.strip() for item in form_inputs
    if isinstance(item, str) and item.strip()
]


#Convert product prices from USD to EUR.
prices_usd = [10, 20, 35, 50]
exchange_rate = 0.92
prices_eur = [round(p * exchange_rate,1) for p in prices_usd]



#Normalize email addresses
emails = ["Admin@Mail.com", "USER@domain.COM", "test@Example.org"]
emails_norm = [email.lower() for email in emails]


#Extract error logs
logs = [
    "INFO Server started",
    "ERROR Database connection failed",
    "WARNING Disk usage high",
    "ERROR Timeout occurred"
]
error_logs = [error for error in logs if error.startswith("ERROR")]



#Login status labeling
login_attempts = [True, False, True, False]
login_status = ["Success" if login == True else "Failure" for login in login_attempts]



#Inventory status
stocks = [10, 0, 5, 0, 3]
invent_status = ["In stock" if stock > 0 else "Out of stock" for stock in stocks]


#Student pass/fail
scores = [45, 82, 60, 30, 90]
passing_score = 50
student_status = ["Pass" if score>=passing_score else "Fail" for score in scores]



#Extract all words longer than 5 characters.
feedback = [
    "Great product and fast delivery",
    "Customer support was helpful",
    "Bad experience"
]
feed_words = [word for sentence in feedback for word in sentence.split() if len(word)>5]
print(feed_words)


#Generators

#Large square generatorc
squares_gen = (x**2 for x in range(30000))

#Sum of even numbers
sum_even_gen = sum(x for x in range(1,100) if x % 2 == 0)


