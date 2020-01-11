import tkinter as tk
import tkinter.ttk as ttk

import database

class ContactList(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title('Contact List')
        self.geometry('700x500')
        self.load_contacts()


    def load_contacts(self):
        contacts = database.list_contact()
        for c in contacts:
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

            self.user_id = ttk.Label(id_label_frame, text=c['Id'])
            self.user_id.pack(fill=tk.BOTH)

            id_label_frame.pack(fill=tk.BOTH, expand=0)
            id_frame.pack(fill=tk.BOTH)
        

            self.name = ttk.Label(name_label_frame, text=c['name'])
            self.name.pack(fill=tk.BOTH)
            

            name_label_frame.pack(fill=tk.BOTH, expand=0)
            name_frame.pack(fill=tk.BOTH)

            self.phone = ttk.Label(phone_label_frame, text=c['phone'])
            self.phone.pack(fill=tk.BOTH)

            phone_label_frame.pack(fill=tk.BOTH, expand=0)
            phone_frame.pack(fill=tk.BOTH)     

            self.address =ttk.Label(address_label_frame, text=c['address'])
            self.address.pack(fill=tk.BOTH)

            address_label_frame.pack(fill=tk.BOTH, expand=0)
            address_frame.pack(fill=tk.BOTH) 
            
            self.label = ttk.Label(self, text="<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>")
            self.label.pack()
       
        


       
       