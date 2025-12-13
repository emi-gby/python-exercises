#set "Even" or "Odd" for numbers from 1 to 10
even_odd = {x: "even" if x%2 == 0  else "odd" for x in range(1,11) }


#Length of strings
names = ["Alice", "Bob", "Charlie"]
length_names = {name: len(name) for name in names}


#Dictionary of squares
squares_dict = {x: x**2 for x in range(1,6)}


#Word frequency
sentence = "python makes python fun and python in python is fun funny"
words = sentence.split()
word_frenq = {word : words.count(word) for word in set(words)}


#User age mapping
users = [("alice", 25), ("bob", 30), ("charlie", 22)]
user_map = {name: age for name, age in users}


#Create a dictionary assigning each product the default price.
products = ["apple", "banana", "cherry"]
default_price = 1.99
product_default = {prod: default_price for prod in products}
