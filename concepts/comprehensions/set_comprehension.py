#Vowels only
text = "comprehension"
vowels = ("a","e","i","o","u")
vowels_text = {v for v in text if v in vowels}


#Unique squared evens
nums = [1, 2, 2, 3, 4, 4, 5]
squared_evens = {x**2 for x in nums if x%2==0}
