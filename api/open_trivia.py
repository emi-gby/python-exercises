import requests
import customtkinter as ctk


url = "https://opentdb.com/api.php?amount=1&category=27&type=boolean"



def get_question():
    global answer

    response = requests.get(url)

    response.encoding = "utf-8"

    data = response.json()

    question = data["results"][0]["question"]

    answer = data["results"][0]["correct_answer"]

    label.configure(text=question,font=("consolas",30),text_color="black")

    button.pack_forget()

    frame.pack(side="bottom", pady=10)
    true_button.pack(side="left", pady=10, padx=8)
    false_button.pack(side="left", pady=10, padx=8)


def correct_question(user_answer):

    if answer == user_answer:
        label.configure(text="CORRECT!",font=("consolas",100),text_color="green")

    else:
        label.configure(text="INCORRECT!",font=("consolas",80),text_color="red")
    
    frame.pack_forget()
    button.pack(side="bottom", pady=10)


answer = ""

window = ctk.CTk(fg_color="white")
window.geometry("600x450")

button = ctk.CTkButton(window,text="Get Question",width = 350, height=80,
                       font=("consolas",30), command=get_question)
button.pack(side="bottom", pady=10)


frame = ctk.CTkFrame(window, width=600)


true_button = ctk.CTkButton(frame,text="True",width = 250, height=80,
                       font=("consolas",30), command= lambda: correct_question("True"))


false_button = ctk.CTkButton(frame,text="False",width = 250, height=80, fg_color="red",
                       font=("consolas",30), hover_color="#D65F80",
                       command= lambda: correct_question("False"))


label = ctk.CTkLabel(window,text="", font=("consolas",30),
                     wraplength=500, text_color="black")
label.pack(pady=20)



window.mainloop()

