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
        self.geometry("950x650")
        self.resizable(False,False)
        self.label_0 =tk.Label(self, text='!!!!WELCOME TO THE CONTACT MANAGER!!!!', width=50, font=("bold", 20))
        self.label_0.place(x=40, y=43)

        self.label_1 =tk.Label(self, text='Your Contact List', width=50, font=("bold", 20))
        self.label_1.place(x=36, y=103)
       
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
        self.cols = ('ID','Name', 'Gender', 'Email', 'Phone', 'Type', 'Address')
        self.listbox = ttk.Treeview(self, columns=self.cols, show="headings")
        self.listbox.place(x=20, y=153)
        self.listbox.column(self.cols[0], width=35)
        self.listbox.column(self.cols[1], width=150)
        self.listbox.column(self.cols[2], width=60)
        self.listbox.column(self.cols[3], width=220)
        self.listbox.column(self.cols[4], width=150)
        self.listbox.column(self.cols[5], width=70)
        self.listbox.column(self.cols[6], width=220)
        
        
        
        for col in self.cols:
            self.listbox.heading(col, text=col)

        for c in self.contact:
            self.listbox.insert("","end", values=(c['id'],c['name'],c['gender'],c['email'],c['phone'],c['Type'],c['address']))


        
        
        
       
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.config(command=self.listbox.xview)





        


            


if __name__ == "__main__":
    mainwindow = MainWindow()
    mainwindow.mainloop()