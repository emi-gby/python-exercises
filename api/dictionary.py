import requests


word = input("Enter a word: ").strip()

try:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    response = requests.get(url)

    data = response.json()

    print(f"word : {word}\n")


    for mean in data[0]["meanings"]:
        print(f"definition: {mean["definitions"][0]["definition"]}")

        try:
            print(f"example: {mean["definitions"][0]["example"]}\n")
        except:
            print("example: Not found\n")

        
except Exception as e:
    print("Word not Found.")

