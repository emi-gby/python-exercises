import sqlite3

conn = sqlite3.connect("contacts_info.db")
cursor = conn.cursor()


def create_table():

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts(
            first_name TEXT,
            last_name TEXT,
            phone TEXT,
            email TEXT,
            address TEXT              
        )""")


    conn.commit()



def get_items():
    cursor.execute("SELECT rowid,* FROM contacts ORDER BY first_name")
    items = cursor.fetchall()
    return items


def add_data(contact_data):
    cursor.execute("INSERT INTO contacts VALUES(?,?,?,?,?)",contact_data)

    conn.commit() 

    update_data()


def delete_data(id):
    cursor.execute('DELETE FROM contacts WHERE rowid = (?)',(id,))
    conn.commit() 
    
    update_data()  


def edit_data(contact_data,id):
    parameters = contact_data + (id,)
    cursor.execute('''UPDATE contacts SET first_name = ?, last_name = ?,
                   phone = ?, email = ?, address = ? 
                   WHERE rowid = ?''',parameters)
    conn.commit()
    
    update_data()


new_items_list = []
def update_data():
    cursor.execute("SELECT rowid,* FROM contacts ORDER BY first_name")
    new_items = cursor.fetchall() 
    new_items_list.clear() 
    new_items_list.append(new_items) 


 
def close_conn():
    conn.close()
