import requests


url_general = "https://official-joke-api.appspot.com/jokes/general/random"
url_programming = "https://official-joke-api.appspot.com/jokes/programming/random"



while True:

    user_input = input("You wanna a programming(p) or general(g) joke. (q) to quit: ").lower()

    if user_input == "p":
        response_programming = requests.get(url_programming)
        data = response_programming.json()[0]
        

    elif user_input == "g":
        response_general = requests.get(url_general)
        data = response_general.json()[0]

    elif user_input == "q":
        break
    
    else:
        print("Not a valid option. Try again.")
        continue


    print("Joke: ")
    print(data["setup"])
    print(data["punchline"])
    print()


