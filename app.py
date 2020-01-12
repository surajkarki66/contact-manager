import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import time
import sqlite3


from contact.contactcreate import ContactCreate
from db.database import DB


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.db=DB()
        self.title("Contact-Book")
        self.geometry("700x700")
        self.resizable(False,False)
        self.label_0 =tk.Label(self, text='!!!!WELCOME TO THE CONTACT MANAGER!!!!', width=50, font=("bold", 20))
        self.label_0.place(x=-80, y=43)

        self.label_1 =tk.Label(self, text='Your Conatact List', width=50, font=("bold", 20))
        self.label_1.place(x=-80, y=103)
       
        menubar = Menu(self)
        contacts = Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='Contacts', menu = contacts) 
        contacts.add_command(label ='New Contact', command = self.contact_create )
       
    
        contacts.add_separator() 
        contacts.add_command(label ='Exit', command = self.destroy) 

        self.config(menu = menubar) 
        self.contact_list()

        
    def contact_create(self, event=None):       
        ContactCreate()


    


    def contact_list(self):
        self.contact = self.db.list_contact()
        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = tk.Listbox(self, height=20, width=80)
        self.listbox.place(x=20, y=153)
        self.listbox.insert(END, "Id")
        for c in self.contact:
            self.listbox.insert(END, c['id'])
            self.listbox.insert(2, c['name'])
        
        
       
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)



        


            


if __name__ == "__main__":
    mainwindow = MainWindow()
    mainwindow.mainloop()