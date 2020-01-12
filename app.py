import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import time
import sqlite3


from contact.contactcreate import ContactCreate
from database import DB


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.db=DB()
        self.title("Contact-Book")
        self.geometry("700x700")
        self.resizable(False,False)
        self.label_0 =tk.Label(self, text='!!!!WELCOME TO THE CONTACT MANAGER!!!!', width=50, font=("bold", 20))
        self.label_0.place(x=-80, y=43)
       
        menubar = Menu(self)
        contacts = Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='Contacts', menu = contacts) 
        contacts.add_command(label ='New Contact', command = self.contact_create )
        contacts.add_command(label ='Contact List', command = self.contact_list )
        
        
    
        contacts.add_separator() 
        contacts.add_command(label ='Exit', command = self.destroy) 

        edit = Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='Edit', menu = edit) 
        edit.add_command(label='Edit Contact', command=None)
       
        self.config(menu = menubar) 

        
    def contact_create(self, event=None):       
        ContactCreate()


    


    def contact_list(self):
        self.contact = self.db.list_contact()
        for c in self.contact:
            print(c['id'])
            print(c['name'])
            print(c['phone'])
            print(c['address'])

        


            


if __name__ == "__main__":
    mainwindow = MainWindow()
    mainwindow.mainloop()