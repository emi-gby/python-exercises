import tkinter as tk


class TopLevel(tk.Toplevel):
    def __init__(self,master,func,text,contacts,id):
        super().__init__(master,height=50,width=50)
        self.title('')
        self.attributes_list = ['first_name:','last_name','phone:','email:','address:']
        self.entry_dict = {}       

        #toplevel layout
        self.rowconfigure((0,1,2,3,4,5),weight=1,uniform='a')
        self.columnconfigure((0,1,2),weight=1,uniform='a')

        for row in range(5):
            label = tk.Label(self,text=self.attributes_list[row])
            label.grid(column=0,row=row)

            self.entry = Entry(self,row)
            if text == 'edit':
                self.entry.insert(0,contacts[row + 1])

            #to store entry_box in a dict
            self.entry_dict[self.attributes_list[row]] = self.entry 

        self.submit_button = tk.Button(self,text='submit',font=('consolas',13),
                                       command=lambda:(func(self.entry_dict,text,id)))
        self.submit_button.grid(row=5,column=2)


class Entry(tk.Entry):
    def __init__(self,master,row):
        super().__init__(master)
        self.grid(column=1,row=row,columnspan=2,padx=10)

class Label(tk.Label):
    def __init__(self,master,text,anchor,font,bg):
        super().__init__(master,text=text,anchor=anchor,font=font,background=bg)
        self.pack(fill='x')

class ContactButton(tk.Button):
    def __init__(self,master,text,fill,relief,anchor,cmd,font,id):
        super().__init__(master,text=text,font=font,relief=relief,borderwidth=2,
                         anchor=anchor,
                         activebackground='light gray',command=lambda:cmd(id))
        self.pack(fill=fill,anchor='w')

class FunctionButton(tk.Button):
    def __init__(self,master,text,row,col,font,cmd,id):
        super().__init__(master,text=text,font=font,
                         command=lambda:cmd(text,id))
        if text == 'v':
            self.place(relx=0.88,rely=0)
        else:   #(submit,delete,edit)
            self.grid(row=row,column=col,sticky='nswe')
