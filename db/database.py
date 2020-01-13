import sqlite3

class DB:
    def __init__(self):
        self.connections = sqlite3.connect('data.db')
        self.cursor = self.connections.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY, name TEXT, gender TEXT, phone INTEGER, Type TEXT , email TEXT, address TEXT)')
        self.connections.commit()

    def __del__(self):
        self.connections.close()

    
    
    def list_contact(self):
        self.cursor.execute('SELECT COUNT(*) FROM contact')
        self.cursor.execute('SELECT * FROM contact')
        contact = [{'id': row[0], 'name': row[1], 'gender':row[2], 'email':row[3], 'phone': row[4], 'Type':row[5], 'address':row[6]} for row in self.cursor.fetchall()]
        return contact




   
    def insert(self, name, gender, phone, Type, email, address):

        try:
            self.cursor.execute('INSERT INTO contact VALUES(NULL,?,?,?,?,?,?)',(name, gender, phone, Type,email, address))
            

        except sqlite3.IntegrityError:
            print(f'{name} is already exists.')

        self.connections.commit()

       
        
        
    def update(self, id, name, gender, phone, Type, email, address):
        

        try:

            self.connections.execute('update contact set name=?, gender=?,phone=?, Type=?, email=?,address=? where id=?',(name, gender, phone, Type, email, address, id))

        except sqlite3.IntegrityError:
            print("The data is already")
        

    


    def delete(self, id):
        self.cursor.execute('DELETE FROM contact WHERE id=?', (id,))
        self.connections.commit()
      
    def search(self):
        pass



      

        