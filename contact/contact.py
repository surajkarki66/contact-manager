import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

from db.database import DB

class Contact(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.db = DB()
        self.master = master
    
    def contact_create_form(self):
        
        self.geometry("500x500")
        self.resizable(False,False)
        self.title('Add Contacts')

        label_0 =tk.Label(self, text='Add Contact Form', width=20, font=("bold", 20))
        label_0.place(x=90, y=43)


        label_1 = tk.Label(self, text='Full Name', width=20, font=("bold", 10))
        label_1.place(x=80, y=130)

        self.name = tk.Entry(self)
        self.name.place(x=240, y=130)

        label_2 = tk.Label(self, text='Phone Number', width=20, font=("bold", 10))
        label_2.place(x=80, y=180)

        self.phone = tk.Entry(self)
        self.phone.place(x=240, y=180)

        label_3 = tk.Label(self, text='Email', width=20, font=("bold", 10))
        label_3.place(x=80, y=230)


        self.email = tk.Entry(self)
        self.email.place(x=240, y=230)


        label_4 = tk.Label(self, text="Gender", width=20, font=("bold", 10))
        label_4.place(x=80, y=280)


        self.gender = tk.StringVar(self, "")
       
        
       
        tk.Radiobutton(self, text='Male', variable=self.gender, value='Male', bg='lightblue',fg='blue').place(x=240,y=280)
        tk.Radiobutton(self, text='Female', variable=self.gender, value='Female', bg='lightblue',fg='blue').place(x=330, y=280)
        


        label_5 = tk.Label(self, text='Address', width=20, font=('bold', 10))
        label_5.place(x=80, y=330)

        self.address = tk.Entry(self)
        self.address.place(x=240, y= 330)

        label_6 = tk.Label(self, text="Type", width=20, font=("bold", 10))
        label_6.place(x=80, y=380)

        list1 = ['Telephone', 'Mobile']
        self.type = tk.StringVar(self)
        droplist = tk.OptionMenu(self, self.type, *list1)
        droplist.config(width=15)
        self.type.set('Select number type')
        droplist.place(x=240, y=380)

       
        tk.Button(self, text='Submit', command=self.add_to_db, width=15, bg='brown', fg='white').place(x=180, y=450)


        

    def contact_update_form(self, id):
        self.geometry("500x500")
        self.resizable(False,False)
        self.id = id
        self.title(f'Update Contact')

        label_0 =tk.Label(self, text='Update Contact', width=20, font=("bold", 20))
        label_0.place(x=90, y=43)


        label_1 = tk.Label(self, text='Full Name', width=20, font=("bold", 10))
        label_1.place(x=80, y=130)

        self.name = tk.Entry(self)
        self.name.place(x=240, y=130)

        label_2 = tk.Label(self, text='Phone Number', width=20, font=("bold", 10))
        label_2.place(x=80, y=180)

        self.phone = tk.Entry(self)
        self.phone.place(x=240, y=180)

        label_3 = tk.Label(self, text='Email', width=20, font=("bold", 10))
        label_3.place(x=80, y=230)


        self.email = tk.Entry(self)
        self.email.place(x=240, y=230)


        label_4 = tk.Label(self, text="Gender", width=20, font=("bold", 10))
        label_4.place(x=80, y=280)


        self.gender = tk.StringVar(self, "")
       
        
       
        tk.Radiobutton(self, text='Male', variable=self.gender, value='Male', bg='lightblue',fg='blue').place(x=240,y=280)
        tk.Radiobutton(self, text='Female', variable=self.gender, value='Female', bg='lightblue',fg='blue').place(x=330, y=280)
        


        label_5 = tk.Label(self, text='Address', width=20, font=('bold', 10))
        label_5.place(x=80, y=330)

        self.address = tk.Entry(self)
        self.address.place(x=240, y= 330)

        label_6 = tk.Label(self, text="Type", width=20, font=("bold", 10))
        label_6.place(x=80, y=380)

        list1 = ['Telephone', 'Mobile']
        self.type = tk.StringVar(self)
        droplist = tk.OptionMenu(self, self.type, *list1)
        droplist.config(width=15)
        self.type.set('Select number type')
        droplist.place(x=240, y=380)

       
        tk.Button(self, text='Submit', command=self.update_db, width=15, bg='brown', fg='white').place(x=180, y=450)


        

       
        
    
    def add_to_db(self):
        name = self.name.get()
        gender = self.gender.get()
        email = self.email.get()
        address = self.address.get()
        Type = self.type.get()
        phone = self.phone.get()
        if msgbox.askyesno("Add Contact?", "Shall we proceed?"):
            if name== "" or address == "" or phone == "" or gender == "":
                msgbox.showerror("error", "All fields are required")

            else:

                try:

                    self.db.insert(str(name), str(gender), str(email),int(phone), str(Type) ,str(address))
                    msgbox.showinfo('success', 'Successfully Created')
                    self.destroy()

                except ValueError:
                    msgbox.showerror("field", "Fields Error")
                    msgbox.showinfo("info", f"{user_id} must me integer\n {phone} must be integer")  

        else:
            pass


    def update_db(self):
        name = self.name.get()
        gender = self.gender.get()
        email = self.email.get()
        address = self.address.get()
        Type = self.type.get()
        phone = self.phone.get()
        if msgbox.askyesno("Update Contact?", "Shall we proceed?"):
            if name== "" or address == "" or phone == "" or gender == "":
                msgbox.showerror("error", "All fields are required")
          
            else:

                try:

                    self.db.update(str(name), str(gender), int(phone), str(Type) , str(email),str(address),self.id)
                    msgbox.showinfo('success', 'Successfully Update')
                    self.destroy()

                except ValueError:
                    msgbox.showerror("field", "Fields Error")
                    msgbox.showinfo("info", f"{user_id} must me integer\n {phone} must be integer")

        else:
            pass


