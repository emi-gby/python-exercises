import customtkinter as ctk
import database
from random import choice

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('380x700')

        Label(self,font=('consolas',30),text='FlashCards')

        self.main_frame = Frame(self) 

        #buttons
        for subject in list(set(database.subjects)):
            Button(self.main_frame,text=subject[0],exp=True,ipy=0,          
                   font=('consolas',30),func=self.create_window)
            
        #bind 
        self.protocol("WM_DELETE_WINDOW", self.close_conn)

    def close_conn(self):
        database.close_conn()
        self.destroy()

    def create_window(self,text):
        toplevel = TopLevel(self,text)
        self.questions_list = database.pull_questions(text)
        self.question = choice(self.questions_list)

        self.flash_button = Button(toplevel,text=self.question[0],exp=True,ipy=0,
                                   font=('consolas',20),func=self.give_answer)
        
        Button(toplevel,text='Another',font=('consolas',20),func=self.give_answer,exp=False,ipy=10)

    def give_answer(self,text):
        if text == 'Another':
            self.question = choice(self.questions_list)
            self.flash_button.configure(text=self.question[0])
        else:
            self.flash_button.configure(text=self.question[1])


class Label(ctk.CTkLabel):
    def __init__(self,master,font,text):
        super().__init__(master,font=font,text=text)
        self.pack(fill='x')

class Button(ctk.CTkButton):
    def __init__(self,master,text,font,func,exp,ipy):
        super().__init__(master,text=text,font=font
                         ,command=lambda:func(text))
        self.pack(fill='both',expand=exp,padx=10,pady=10,ipady=ipy)

class Frame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.pack(expand=True,fill='both')

class TopLevel(ctk.CTkToplevel):
    def __init__(self,master,text):
        super().__init__(master)
        self.geometry('380x300')

        Label(self,font=('consolas',20),text=text)


if __name__ == '__main__':
    window = Window()
    window.mainloop()