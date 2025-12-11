import customtkinter as ctk

class Button(ctk.CTkButton):
    def __init__(self,master, width, height, fg_color, text,font, func, side,color):
        super().__init__(master, width=width, height=height,font=font,
                         fg_color=fg_color,text=text, command=func, 
                         text_color=color)
        
        self.pack(side=side)


class Label(ctk.CTkLabel):
    def __init__(self,master,text,font, wrap):
        super().__init__(master, text=text,font=font, wraplength=wrap)

        self.pack()


class Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.pack() 

class Window(ctk.CTk):
    def __init__(self,size):
        super().__init__()

        self.geometry(f"{size[0]}x{size[1]}")

    