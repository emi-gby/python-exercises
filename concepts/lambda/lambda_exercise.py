
square = lambda x: x**2

sum_two_num = lambda x, y : x+y

even_odd = lambda x: x%2==0

temp_convert = lambda c: c*9/5 +32


#list comprehension is a better option is these cases
nums = [1, 2, 3, 4, 5]
double_nums = map(lambda x: x*2, nums)


scores = [45, 82, 60, 30, 90]
scores_filter =  filter(lambda s: s>= 50, scores)


prices = [100, 250, 400]
discount = map(lambda x: x*0.9, prices)


#Filter valid emails
emails = ["user@mail.com", "invalid.com", "admin@site.org"]
valid_emails = list(filter(lambda x: "@" in x, emails))


#--------------------------------------------------

#Sort by string length
names = ["John", "Elizabeth", "Amy"]
names_sort = sorted(names, key=lambda l: len(l))


#Sort by second value
records = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
records_sort = sorted(records, key=lambda x: x[1])
print(records_sort)


#9️Sort products by price
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 600}
]
products_sort = sorted(products, key=lambda x: x["price"])
cheapest_prod = min(products, key=lambda x: x["price"])


#Sort by score (descending)
students = [
    ("Alice", 85),
    ("Bob", 85),
    ("Charlie", 78)
]

students_sort = sorted(students, key=lambda x: x[1], reverse=True)


#Find the employee with the most projects.
employees = [
    {"name": "Alice", "projects": 3},
    {"name": "Bob", "projects": 7},
    {"name": "Charlie", "projects": 5}
]
projects_max = max(employees, key= lambda p: p["projects"])

