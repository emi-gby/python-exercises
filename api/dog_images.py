import requests
import customtkinter as ctk
from PIL import Image
from io import BytesIO

url = "https://dog.ceo/api/breeds/image/random"



def get_image():

    response = requests.get(url)

    data = response.json()

    dog_url = data["message"]

    img_bytes = requests.get(dog_url).content

    dog_image = Image.open(BytesIO(img_bytes))


    ctk_image = ctk.CTkImage(dog_image, size = (500,350))

    label.configure(image=ctk_image)




window = ctk.CTk(fg_color="white")
window.geometry("600x450")

button = ctk.CTkButton(window,text="Get Image",width = 350, height=80,
                       font=("consolas",30), command=get_image)
button.pack(side="bottom", pady=10)


label = ctk.CTkLabel(window,text="")
label.pack(pady=20)



window.mainloop()