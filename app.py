import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import sqlite3


from contact.contact import Contact
from db.database import DB


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.db=DB()
        self.title("Contact-Book")
        self.geometry("950x600")
        self.resizable(False,False)
        self.label_0 =tk.Label(self, text='!!!!WELCOME TO THE CONTACT MANAGER!!!!', width=50, font=("bold", 20))
        self.label_0.place(x=40, y=43)

        self.label_1 =tk.Label(self, text='Your Contact List', width=50, font=("bold", 20))
        self.label_1.place(x=36, y=103)
       
        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.cols = ('ID','Name', 'Gender', 'Email', 'Phone', 'Type', 'Address')
        self.listbox = ttk.Treeview(self, columns=self.cols, show="headings")

        for col in self.cols:
            self.listbox.heading(col, text=col)

        self.listbox.place(x=10, y=163)
        self.listbox.column(self.cols[0], width=35)
        self.listbox.column(self.cols[1], width=150)
        self.listbox.column(self.cols[2], width=60)
        self.listbox.column(self.cols[3], width=220)
        self.listbox.column(self.cols[4], width=150)
        self.listbox.column(self.cols[5], width=70)
        self.listbox.column(self.cols[6], width=220)

        
       
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.config(command=self.listbox.xview)

        self.search_label =tk.Label(self, text='Search By Name', width=20, font=("bold", 10))
        self.search_label.place(x=36, y=420)

        self.search_entry = ttk.Entry(self)
        self.search_entry.place(x=200, y=420)

       

        sort_list = ['A', 'Name', 'Id', 'Address']
        self.sort_type = tk.StringVar()
        droplist = ttk.OptionMenu(self, self.sort_type, *sort_list)
        droplist.config(width=7)
        self.sort_type.set('Sort By')
        droplist.place(x=810, y=383)
       


        tk.Button(self, text='Create Contact', command=self.contact_create, width=15, bg='green', fg='white',font=("bold", 10)).place(x=50, y=500)
        tk.Button(self, text='Show Contact List', command=self.contact_list, width=15, bg='blue', fg='white', font=("bold", 10)).place(x=270, y=500)
        tk.Button(self, text='Update Contact ', command=self.contact_update, width=15, bg='orange', fg='white', font=("bold", 10)).place(x=490, y=500)
        tk.Button(self, text='Delete Contact', command=self.contact_delete, width=15, bg='red', fg='white', font=("bold", 10)).place(x=710, y=500)
        tk.Button(self, text='Search', command=self.search_contact, width=10, bg='yellow', fg='white', font=("bold", 10)).place(x=400, y=415)

        
    def contact_create(self):       
       self.create = Contact(self)
       self.create.contact_create_form()

    def contact_list(self):
        sort_type = self.sort_type.get()
        if sort_type == 'Name':
            self.sort_by_name()

        elif sort_type == 'Address':
            self.sort_by_address()

        elif sort_type == 'Id':
            self.sort_by_id()

        else:
            self.contact = self.db.list_contact()
            for i in self.listbox.get_children():
                self.listbox.delete(i)
        
            for c in self.contact:
                self.listbox.insert("","end", values=(c['id'],c['name'],c['gender'],
                                        c['email'],c['phone'],c['Type'],c['address']))


    def contact_update(self):
       
       try:
          
           self.selected_item = self.listbox.selection()[0]
           values = tuple(self.listbox.item(self.selected_item)['values'])
           self.update = Contact()
           self.update.contact_update_form(values[0])
          


          
       except IndexError:
            msgbox.showerror("error", "First Select the Item")
            
           


        
    def contact_delete(self):
       try:
            if msgbox.askyesno("Delete Contact?", "Do you really want to delete?"):

                self.selected_item = self.listbox.selection()[0]
                values = tuple(self.listbox.item(self.selected_item)['values'])
                self.listbox.delete(self.selected_item)
                self.db.delete(values[0])
                msgbox.showinfo("deleted", "Successfully Deleted")

            else:
                pass


          
       except IndexError:
            msgbox.showerror("error", "First Select the Item")



    def on_closing(self):
        if msgbox.askokcancel("Quit", "Do you want to quit?"):
            del self.db
            self.destroy()
            
           
       

    def search_contact(self):
        self.contact_name = self.search_entry.get()
        self.result=self.db.search(self.contact_name)
       
        for i in self.listbox.get_children():
            self.listbox.delete(i)

        if self.result == []:
            msgbox.showinfo('Not Found',"Search result not found")

        

        else:
            for c in self.result:
                self.listbox.insert("","end", values=(c['id'],c['name'],c['gender'],
                                        c['email'],c['phone'],c['Type'],c['address']))

    
    def sort_by_name(self):
        self.sort_name = self.db.sort_by_name()
        for i in self.listbox.get_children():
            self.listbox.delete(i)
        for c in self.sort_name:
                self.listbox.insert("","end", values=(c['id'],c['name'],c['gender'],
                                        c['email'],c['phone'],c['Type'],c['address']))

    def sort_by_address(self):
        self.sort_address = self.db.sort_by_address()
        for i in self.listbox.get_children():
            self.listbox.delete(i)
        for c in self.sort_address:
                self.listbox.insert("","end", values=(c['id'],c['name'],c['gender'],
                                        c['email'],c['phone'],c['Type'],c['address']))


    def sort_by_id(self):
        self.sort_id = self.db.sort_by_id()
        for i in self.listbox.get_children():
            self.listbox.delete(i)
        for c in self.sort_id:
                self.listbox.insert("","end", values=(c['id'],c['name'],c['gender'],
                                        c['email'],c['phone'],c['Type'],c['address']))


        

        




    

if __name__ == "__main__":
    mainwindow = MainWindow()
    mainwindow.protocol("WM_DELETE_WINDOW", mainwindow.on_closing) 
    mainwindow.mainloop()