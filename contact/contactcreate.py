import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

import database

class ContactCreate(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        self.contact_form()

    def contact_form(self):
        geometry = "400x190"
        self.geometry(geometry)
        id_frame = ttk.Frame(self)
        name_frame = ttk.Frame(self)
        phone_frame = ttk.Frame(self)
        address_frame = ttk.Frame(self)
        

        id_label = ttk.Label(self, text="UserID")       
        name_label = ttk.Label(self, text="Name")
        phone_label = ttk.Label(self, text="Phone Number")
        address_label = ttk.Label(self, text="Address")

       

       
        id_label_frame = ttk.LabelFrame(id_frame, labelwidget=id_label)
        name_label_frame = ttk.LabelFrame(name_frame, labelwidget=name_label)
        phone_label_frame = ttk.LabelFrame(phone_frame, labelwidget=phone_label)
        address_label_frame = ttk.LabelFrame(address_frame, labelwidget=address_label)
       

        self.user_id = ttk.Entry(id_label_frame)
        self.user_id.grid(row=0,column=0)

        id_label_frame.pack(fill=tk.BOTH, expand=0)
        id_frame.pack(fill=tk.BOTH)
       

        self.name = ttk.Entry(name_label_frame)
        self.name.pack(fill=tk.BOTH)
        

        name_label_frame.pack(fill=tk.BOTH, expand=0)
        name_frame.pack(fill=tk.BOTH)

        self.phone = ttk.Entry(phone_label_frame)
        self.phone.pack(fill=tk.BOTH)

        phone_label_frame.pack(fill=tk.BOTH, expand=0)
        phone_frame.pack(fill=tk.BOTH)     

        self.address =ttk.Entry(address_label_frame)
        self.address.pack(fill=tk.BOTH)

        address_label_frame.pack(fill=tk.BOTH, expand=0)
        address_frame.pack(fill=tk.BOTH)     

        submit_button = ttk.Button(self, text="Submit", command=self.add_to_db)
        submit_button.pack()

    
    def add_to_db(self):
        database.create()
        user_id = self.user_id.get()
        name = self.name.get()
        address = self.address.get()
        phone = self.phone.get()
        if msgbox.askyesno("Add Contact?", "Shall we proceed?"):
            try:

                
                database.add(int(user_id),name, int(phone), address)

            except sqlite3.IntegrityError:
                msgbox.showerror("error", "User is already exist!")

        else:
            pass
