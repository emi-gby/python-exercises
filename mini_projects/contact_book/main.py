#Simple Contact Book

#Create a program that allows users to store and manage a list of contacts, including names,phone numbers, and email addresses.
import contact_data
from widgets import *


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x700')
        self.title('Phone Book')
        self.resizable(False,True)
        self.item_height = 100
        contact_data.create_table()

        #contacts number var
        self.num_var = tk.StringVar(value=f'{len(contact_data.get_items())} contacts')

        #widgets
        Label(self,'Phone Book','center',font=('arial',30),bg=None)
        num_label = tk.Label(self,anchor='center',font=('fila code',18),textvariable=self.num_var)
        num_label.pack(fill='x')
        self.add_button = tk.Button(self,text='+',font=('consolas',20))    
        self.add_button.pack(anchor='e',padx=10)
        Label(self,text='',anchor='center',font=('consolas',1),bg='black')

        #contact_frame / canvas
        self.contact_frame = ContactsFrame(self,contact_data.get_items(),self.item_height,self.add_button,self.update_frame)

        #bind window close / close connection
        self.protocol("WM_DELETE_WINDOW", self.close_conn)

    def close_conn(self):
        contact_data.close_conn()
        self.destroy()

    def update_frame(self):
        self.contact_frame.destroy()
        self.num_var.set(value=f'{len(contact_data.new_items_list[0])} contacts')
        self.contact_frame = ContactsFrame(self,contact_data.new_items_list[0],self.item_height,self.add_button,self.update_frame)


class ContactsFrame(tk.Frame):
    def __init__(self,master,ctt,item_height,add_but,upd_func):
        super().__init__(master)
        self.pack(expand=True, fill='both')
        self.contacts = ctt
        self.master = master
        self.item_number = len(self.contacts)
        self.list_height = (self.item_number * item_height) + 80
        self.count_press = 0
        self.add_button = add_but
        self.update_func = upd_func


        #config add buton
        self.add_button.configure(command=lambda:self.modify_data('+','id'))       
        
        #canvas
        self.canvas = tk.Canvas(self,scrollregion=(0,0,400,self.list_height))
        self.canvas.pack(expand=True, fill='both')
    
        #display frame
        self.display_frame = tk.Frame(self)
        

        #create display window
        
        self.canvas.create_window((0,0),window=self.display_frame,
                                  anchor='nw',width=400,              
                                  height=self.list_height)



        #scrollbar
        self.scrollbar = tk.Scrollbar(self,command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=1,rely=0,anchor='ne',relheight=1)

        #bind (Linux)
        self.canvas.bind_all("<Button-4>", lambda event: self.canvas.yview_scroll(-2, "units"))
        self.canvas.bind_all("<Button-5>", lambda event: self.canvas.yview_scroll(2, "units"))

        #buttons
        storage = []
        self.frame_id = {}
        for contacts in self.contacts:
            self.button_frame = tk.Frame(self.display_frame)
            storage.append(contacts[1][0])
            if len(storage) < 2:
                Label(self.button_frame,text=contacts[1][0],anchor='w',font=('arial',20),bg=None)
            elif len(storage) == 2:
                if storage[0] == storage[1]:
                    pass
                else:
                    Label(self.button_frame,text=contacts[1][0],anchor='w',font=('arial',20),bg=None)
                storage.remove(storage[0])

            self.button =ContactButton(self.button_frame,text=contacts[1],fill='x',
                   relief='ridge',font=('consolas',30),anchor='w',
                   cmd=self.button_press,id=contacts[0])   # flat, groove, raised, ridge, solid, or sunken
            
            self.button_frame.pack(fill='both',expand=True)

            self.frame_id[contacts[0]] = [self.button_frame, self.button]    #access each frame with the respective id

    def button_press(self,id): 
        frame_select = self.frame_id[id][0]
        if self.count_press == 0:                                   #add if to frame selected = frame select
            self.info_frame = tk.Frame(frame_select)
            self.button_frame = tk.Frame(frame_select)

            self.info_frame.pack(fill='both',expand=True)
            self.button_frame.pack(fill='both',expand=True)
            self.count_press += 1
        
        else:
            self.info_frame.destroy()
            self.button_frame.destroy()

            self.info_frame = tk.Frame(frame_select)
            self.button_frame = tk.Frame(frame_select)

            self.info_frame.pack(fill='both',expand=True)
            self.button_frame.pack(fill='both',expand=True)


        #button frame layout
        self.button_frame.columnconfigure((0,1),weight=1,uniform='a')

        #find id at tuple's list
        for item in self.contacts: 
            if item[0] == id:  
                self.data = item


        #info labels
        Label(self.info_frame,text=f' Name: {self.data[1]} {self.data[2]}',font=('consolas',10),anchor='w',bg=None)
        Label(self.info_frame,text=f' Phone: {self.data[3]}',font=('consolas',10),anchor='w',bg=None)
        
        #more button
        self.see_more_but = FunctionButton(self.info_frame,text='v',row=None,col=None,
                           font=('consolas',10),cmd=self.modify_data,id=id)
        
        #edit/delete button
        text_list = ['edit','delete']
        for col in range(2):
            FunctionButton(self.button_frame,text=text_list[col],row=0,col=col,
                           font=('consolas',10),cmd=self.modify_data,id=id)

    def modify_data(self,text,id):
        if text == '+':
            TopLevel(self.master,self.submit_edit_data,text,'contacts','id')

        elif text == 'edit':
            TopLevel(self,self.submit_edit_data,text,self.data,id)

        elif text == 'delete':
            contact_data.delete_data(id)
            self.update_func()
            
        else: 
            #email/addres labels
            if self.count_press == 1:
                Label(self.info_frame,text=f' Email: {self.data[4]}',font=('consolas',10),anchor='w',bg=None)
                Label(self.info_frame,text=f' Address: {self.data[5]}',font=('consolas',10),anchor='w',bg=None)
                self.count_press += 1
            elif self.count_press == 2:
                self.info_frame.destroy()
                self.button_frame.destroy()

                self.count_press -= 1


    def submit_edit_data(self,entry_dict,text,id):
        data = []
        for key,value in entry_dict.items():
            data.append(value.get())
            value.delete(0,tk.END)
        
        count = 0
        for i in range(len(data)):
            if len(data[i]) == 0:
                print('invalid output')
                count += 1

        if count == 0:
            format_data = (data[0].capitalize(),data[1].capitalize(),
                           data[2],data[3],data[4])  
            if text == '+':
                contact_data.add_data(format_data)
            elif text == 'edit':
                contact_data.edit_data(format_data,id)

            self.update_func() 
        


if __name__ == '__main__':
    window = Window()
    window.mainloop()