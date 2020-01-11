import sqlite3


def create():
    connections = sqlite3.connect('data.db')
    cursor = connections.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS contact(Id integer, name text primary key,phone integer,address text )')
    connections.commit()
    connections.close()


def add(Id,name,phone,address):
    connections = sqlite3.connect('data.db')
    cursor = connections.cursor()

    try:


        cursor.execute('INSERT INTO contact VALUES(?,?,?,?)',(Id,name,phone,address))
        

    except sqlite3.IntegrityError:
        print(f'{name} is already exists.')

  
    connections.commit()
    connections.close()


def list_contact():
    connections = sqlite3.connect('data.db')
    cursor = connections.cursor()

    cursor.execute('SELECT COUNT(*) FROM contact')

    

    cursor.execute('SELECT * FROM contact ORDER BY NAME')
    contact = [{'Id': row[0], 'name': row[1],'phone':row[2], 'address': row[3]} for row in cursor.fetchall()]
    connections.close()
    #print(movies)
    return contact


def update_contact(Id,name,phone,address):
    connections = sqlite3.connect('data.db')
    cursor = connections.cursor()
    
   
    try:

        connections.execute('update contact set name=?,phone=?,address=? where id=?',(name,phone,address,Id))

    except sqlite3.IntegrityError:
        print("The data is already")
    connections.commit()
    connections.close()

    


def delete_contact(name):
    connections = sqlite3.connect('data.db')
    cursor = connections.cursor()
    cursor.execute('DELETE FROM contact WHERE name=?', (name,))
    connections.commit()
    connections.close()

#list_movie()





