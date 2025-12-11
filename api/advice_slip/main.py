import requests
import widgets as w

url = "https://api.adviceslip.com/advice"

filePath = "advice_history.txt"


def get_advice():

    response = requests.get(url)

    data = response.json()

    label.configure(text=data["slip"]["advice"])

    with open("advice_history.txt", "a") as file:
        file.write(f"-{data["slip"]["advice"]}\n")



window = w.Window((450,200))

button = w.Button(window,width=300,height=50,fg_color="pink",
                  text="Get advice", func=get_advice,
                  font=("consolas",30), side="bottom",
                  color="black")

label = w.Label(window, text="",font=("consolas",25),wrap=400)


window.mainloop()
