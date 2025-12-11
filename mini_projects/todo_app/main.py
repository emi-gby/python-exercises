import database
import customtkinter as ctk

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x600')

        ctk.CTkLabel(self,text='Todo List',font=('consolas',30)).pack()
        
        self.add_button = ctk.CTkButton(self,text='+',font=('consolas',30),
                                        command=self.add_func,width=50)
        self.add_button.pack(anchor='e',padx=20,pady=5)

        #create dabase table
        database.create_table()

        self.tasks_completed = 0
        for item in database.get_items():
            if item[2] == 'on':
                self.tasks_completed += 1
        self.tasks_labels = ctk.CTkLabel(self,font=('consolas',20),
                    text=f'Tasks Completed : {self.tasks_completed}/{len(database.get_items())}')
        self.tasks_labels.pack(anchor='w',padx=15)

        self.main_frame = MainFrame(self,db=database.get_items(),upd=self.update_frame)


        #self.main_frame.bind("<Button-4>", lambda event: self.main_frame.yview_scroll(-1, "units"))
        #self.main_frame.bind("<Button-5>", lambda event: self.canvas.yview_scroll(1, "units"))
        

        self.protocol("WM_DELETE_WINDOW", self.close_conn)

    def close_conn(self):
        database.close_conn()
        self.destroy()

    def add_func(self):
        TopLevel(self,upd=self.update_frame)
    
    
    def update_frame(self):
        self.tasks_labels.configure(text=f'Tasks Completed : {self.tasks_completed}/{len(database.get_items())}')

        self.main_frame.pack_forget()    ## needed for scrollable frame ##
        self.main_frame.destroy()

        self.main_frame = MainFrame(self,db=database.new_items_list[0],upd=self.update_frame)

class MainFrame(ctk.CTkScrollableFrame):
    def __init__(self,master,db,upd):
        super().__init__(master,border_color='black',
                         border_width=2,corner_radius=0)
        
        
        self.pack(expand=True,fill='both')
        self.columnconfigure(0,weight=4)
        self.columnconfigure(1,weight=1)

        row=0   ############

        for i in db:
            CheckBox(self,text=i[1],row=row,value=i[2],id=i[0])
            DeleteButton(self,row=row,text='del',id=i[0],
                         font=('consolas',15),upd=upd)
            row+=1

class CheckBox(ctk.CTkCheckBox):
    def __init__(self,master,text,row,value,id):
        super().__init__(master,font=('arial',30),text=text,onvalue='on',
                         offvalue='off',command=self.checkbox_event)
        #self.select()
        self.grid(column=0,row=row,pady=20,padx=15,sticky='we')
        self.text = text 
        self.id = id

        if value == 'on':
            self.select()
            self.configure(text=self.strike(self.text),state='disabled')
        else:
            self.deselect()

    def checkbox_event(self):
        self.configure(text=self.strike(self.text),state='disabled')
        database.on_value(self.id)


    def strike(self,text):
               return ''.join([u'\u0336{}'.format(c) for c in text]) 


class DeleteButton(ctk.CTkButton):
    def __init__(self,master,row,text,font,id,upd):
        super().__init__(master,text=text,width=50,
                         font=font,command=self.delete_func)
        self.id = id
        self.upd_func = upd

        self.grid(column=1,row=row,pady=20,padx=15,sticky='e')

    def delete_func(self):
        database.delete_item(self.id)
        self.upd_func()


class TopLevel(ctk.CTkToplevel):
    def __init__(self,master,upd):
        super().__init__(master)
        self.geometry('200x100')
        self.upd_func = upd

        self.entry = ctk.CTkEntry(self,font=('consolas',15))
        self.entry.pack(expand=True,fill='x',padx=15,pady=10)

        self.submit_button = ctk.CTkButton(self,text='submit',command=self.submit_func)
        self.submit_button.pack(expand=True,fill='x',padx=30,pady=10)

    def submit_func(self):
        database.add_item(self.entry.get())
        self.destroy()
        self.upd_func()


if __name__ == '__main__':
    window = Window()
    window.mainloop()