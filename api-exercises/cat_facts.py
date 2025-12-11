import requests
import customtkinter as ctk

url = "https://catfact.ninja/fact"


def get_fact():

    response = requests.get(url)

    data = response.json()

    label.configure(text=data["fact"])



window = ctk.CTk()
window.geometry("600x450")

button = ctk.CTkButton(window,text="Get fact",width = 350, height=80,
                       font=("consolas",30), command=get_fact)
button.pack(side="bottom", pady=10)

label = ctk.CTkLabel(window,text="", font=("consolas",25),
                     wraplength=500)
label.pack(pady=30)


window.mainloop()