import sqlite3

conn = sqlite3.connect('basic_python/ideas_done/todo_app/todo_list.db')

cursor = conn.cursor()



def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS todo(
               list TEXT,
               checkbox TEXT
               )''')

    
def get_items():
    cursor.execute('SELECT rowid, * FROM todo')
    items = cursor.fetchall()

    return items

def add_item(item):
    cursor.execute('INSERT INTO todo VALUES(?,?)',(item,'off'))
    conn.commit()

    update_data()


def delete_item(id):
    cursor.execute('DELETE FROM todo WHERE rowid = (?)',(id,))
    conn.commit()

    update_data()

def on_value(id):
    cursor.execute('UPDATE todo SET checkbox = (?) WHERE rowid = (?)',('on',id))
    conn.commit()

def close_conn():
    conn.close()


new_items_list = []
def update_data():
    cursor.execute("SELECT rowid,* FROM todo ")
    new_items = cursor.fetchall() 
    new_items_list.clear() 
    new_items_list.append(new_items) 

