import requests

name = input("Enter a name: ")

url_age = f"https://api.agify.io?name={name}"
url_genderize = f"https://api.genderize.io?name={name}"
url_nationalize = f"https://api.nationalize.io?name={name}"

response_age = requests.get(url_age)
data_age = response_age.json()

response_genderize = requests.get(url_genderize)
data_genderize = response_genderize.json()

response_nationalize = requests.get(url_nationalize)
data_nationalize = response_nationalize.json()


age = data_age["age"]
gender = data_genderize["gender"]

if(age==None and gender == None):
    print(f"{name} Not Found.")

else:
    country = data_nationalize["country"][0]["country_id"]
    probability = data_nationalize["country"][0]["probability"]

    print(f'Age : {age}')
    print(f'Gender : {gender}')
    print(f'Country: {country} | Certainty : {round(probability*100,1)}%')