import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

from database import DB

class ContactCreate(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DB()
        self.contact_form()

    
 

    def contact_form(self):
        geometry = "500x500"
        self.geometry(geometry)
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

        label_3 = tk.Label(self, text="Gender", width=20, font=("bold", 10))
        label_3.place(x=80, y=230)


        self.gender = tk.StringVar()
        
        
       
        tk.Radiobutton(self, text='Male', variable=self.gender.set("Male"), value='Male', bg='lightblue',fg='blue').place(x=240,y=230)
        tk.Radiobutton(self, text='Female', variable=self.gender.set("Female"), value='Female', bg='lightblue',fg='blue').place(x=330, y=230)



        label_4 = tk.Label(self, text='Address', width=20, font=('bold', 10))
        label_4.place(x=80, y=280)

        self.address = tk.Entry(self)
        self.address.place(x=240, y= 280)

        label_5 = tk.Label(self, text="Type", width=20, font=("bold", 10))
        label_5.place(x=80, y=330)

        self.type= tk.StringVar()
       
       
    
        ttk.Radiobutton(self, text='Mobile', variable=self.type.set("Mobile"), value='Mobile').place(x=242, y=330)
        ttk.Radiobutton(self, text='Telephone', variable=self.type.set("Telephone"), value='Telephone').place(x=320, y=330)

        tk.Button(self, text='Submit', command=self.add_to_db, width=15, bg='brown', fg='white').place(x=180, y=400)


        
       
        
    
    def add_to_db(self):
        name = self.name.get()
        gender = self.gender.get()
        address = self.address.get()
        Type = self.type.get()
        phone = self.phone.get()
        if msgbox.askyesno("Add Contact?", "Shall we proceed?"):
            if name== "" or address == "" or phone == "":
                msgbox.showerror("error", "All fields are required")

            

          
            else:

                try:

                    self.db.insert(str(name), str(gender),int(phone), str(Type) ,str(address))
                    msgbox.showinfo('success', 'Successfully Created')
                    print(name, gender, phone, Type, address)
                    self.destroy()

                except ValueError:
                    msgbox.showerror("field", "Fields Error")
                    msgbox.showinfo("info", f"{user_id} must me integer\n {phone} must be integer")


            

        else:
            pass
