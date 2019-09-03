import database
import time
import sqlite3



user_choice = """

Choice 1) Press 'a' to add contact.
Choice 2) Press 'l' to list contacts.
Choice 3) Press 'u' to update contact.
Choice 3) Press 'd' to delete the contact.
Choice 4) Press 'q' to quit .


"""

def menu():
    database.create()
    print("<--------------------------WELCOME TO CONTACT BOOK---------------------------->")
    choice = input(f"{user_choice} Enter the choice:")
    while choice!= 'q':

        if choice is 'a':
            add_contact()
            time.sleep(2)
        elif choice is 'l':
            list_contact()
            time.sleep(2)

        elif choice is 'u':
            update()
            time.sleep(2)
      
        elif choice is 'd':
            delete_contact()
            time.sleep(2)
        else:
            print("Undefined choice!")
        choice = input(f'{user_choice}Enter Choice:')
def add_contact():

    Id = input("Enter the contact ID:")
    
    name = input("Enter the name of movies:")

    phone = input("Enter the phone number:")

    address = input("Enter the contact address:")

    database.add(Id,name,phone,address)


def list_contact():
    count = 0
    print(count)


    contact = database.list_contact()
    print("")

    print("Here are your contact list")
    print("")

    for c in contact:
        count += 1
    print(f"<-----------Number of Contacts: {count} ------------>")

   

    for c in contact:
        
     
        print(f"ID={c['Id']}")
        print(f"Phone Number={c['phone']}")
        print(f"Name = {c['name']}")
        print(f"Address={c['address']}")
        print("")
   
       

def update():
    Id = input("Enter the id of person you want to change:")
    name = input("Enter the new name:")
    phone = input("Enter the new phone number:")
    address = input("Enter the new address:")

    database.update_contact(Id,name,phone,address)

   

    






  
         


def delete_contact():
    name = input('Enter the name of the movie to delete:')
    database.delete_movies(name)
    print("The movies is been deleted.")


menu()






    

            



