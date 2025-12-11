import sqlite3

conn = sqlite3.connect('flashcard_info.db')
cursor = conn.cursor()

#create table first

#cursor.execute("""CREATE TABLE IF NOT EXISTS flashcards(
#                subject TEXT,
#                question TEXT,
#                answer TEXT
#            )""")



#cursor.executemany('INSERT INTO flashcards VALUES(?,?,?)',flashcards2)


cursor.execute('SELECT rowid,* FROM flashcards ORDER BY subject')
items = cursor.fetchall()


cursor.execute('SELECT subject FROM flashcards ORDER BY subject')
subjects = cursor.fetchall()


cursor.execute('SELECT question,answer FROM flashcards WHERE subject=(?)',('History',))
questions = cursor.fetchall()

def pull_questions(subject):
    cursor.execute('SELECT question,answer FROM flashcards WHERE subject=(?)',(subject,))
    questions_list = cursor.fetchall()

    return questions_list

def close_conn():
    conn.close()

conn.commit()
