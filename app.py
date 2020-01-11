import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import database
import time
import sqlite3
from contact.contactcreate import ContactCreate
from contact.contactlist import ContactList


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact-Book")
        self.geometry("500x500")
        self.resizable(False,False)
        self.label_text = "WELCOME TO THE CONTACT BOOK"
        self.label = tk.Label(self, text=self.label_text)
        self.background_image=tk.PhotoImage(file="photos/menu.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.label.pack()
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
        ContactList()
     


        
       


if __name__ == "__main__":
    mainwindow = MainWindow()
    mainwindow.mainloop()