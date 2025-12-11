import requests


name = input("Enter pokemon name: ")

try:
    resp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    data = resp.json()

    print("Name:", data["name"])
    print("Height:", data["height"])
    print("Weight:", data["weight"])
    print("Types:", [t["type"]["name"] for t in data["types"]])


    print("Abilities:", [ability["ability"]["name"] for ability in data["abilities"]])
    print("Stats:", {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]})
    

except:
    print("Pokemon not found.")

