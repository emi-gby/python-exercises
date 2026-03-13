import sqlite3

# Define ANSI colors for terminal text
colors = {'red':'\033[31m', 'green':'\033[32m', 'magenta':'\033[35m',
          'cyan':'\033[36m', 'reset':'\033[0m'}

class BookSystem():
    def __init__(self):
        # Initialize SQLite database connection
        self.db_name = "books.db"
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row  # Rows behave like dictionaries
        self.cursor = self.conn.cursor()
        self.create_table()

        self.run_system()

    def create_table(self):
        """Creates the books table if it doesn't exist yet"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                availability TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_book(self):
        '''Adds a book (title/author/availability) to the books table'''
        title = input('Enter the book title: ').strip().capitalize()
        if self.check_empty_input('title', title) == False:
            return

        author = input('Enter the author of the book: ').strip().capitalize()
        if self.check_empty_input('author', author) == False:
            return

        status = input('Is the book available (Y/N)? ').lower().strip()
        if status == 'y':
            availability = 'Book Available'
        elif status == 'n':
            availability = 'Book Unavailable'
        else:
            print('-------------------------------')
            print(f'{colors["cyan"]}Answer must be "Y" or "N"!{colors["reset"]}')
            print(f'{colors["red"]}Registration canceled! Try again.{colors["reset"]}')
            return

        # Insert book into database
        self.cursor.execute('INSERT INTO books (title, author, availability) VALUES (?, ?, ?)',
                            (title, author, availability))
        self.conn.commit()
        print('-------------------------------')
        print(f'{colors["green"]}Book added successfully!{colors["reset"]}')

    def check_empty_input(self, category, value):
        '''Checks if user input is empty; returns False if so'''
        if len(value) == 0:
            print('-------------------------------')
            print(f'{colors["cyan"]}{category.capitalize()} cannot be empty!{colors["reset"]}')
            print(f'{colors["red"]}Registration canceled! Try again.{colors["reset"]}')
            return False

    def list_books(self):
        '''Lists all books'''
        self.cursor.execute('SELECT * FROM books')
        books = self.cursor.fetchall()
        if len(books) == 0:
            print('-------------------------------')
            print(f'{colors["green"]}No books registered.{colors["reset"]}')

        for book in books:
            for category in book.keys():
                print(f'{colors["magenta"]}{category}{colors["reset"]} : {colors["cyan"]}{book[category]}{colors["reset"]}')
            print('-------------------------------')

    def update_book(self):
        '''Updates book details according to user choice'''
        try:
            book_id = int(input('Enter the book id to update: '))

            self.cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
            selected_book = self.cursor.fetchone()

            if selected_book is None:
                print('-------------------------------')
                print(f'{colors["red"]}Book not found. Try again.{colors["reset"]}')
                return

            category = input('Which category to update (title/author/availability)? ').lower().strip()
            if category in ['title', 'author', 'availability']:
                print(f'Current {category.capitalize()}: {selected_book[category]}')
                new_value = input('Enter new value: ').strip().capitalize()
                if self.check_empty_input(category, new_value) == False:
                    return

                if category == 'availability':
                    if new_value == 'Y':
                        new_value = 'Book Available'
                    elif new_value == 'N':
                        new_value = 'Book Unavailable'
                    else:
                        print('-------------------------------')
                        print(f'{colors["cyan"]}Answer must be "Y" or "N"!{colors["reset"]}')
                        print(f'{colors["red"]}Update canceled! Try again.{colors["reset"]}')
                        return

                sql = f'UPDATE books SET {category} = ? WHERE id = ?'
                self.cursor.execute(sql, (new_value, book_id))
                self.conn.commit()
                print('-------------------------------')
                print(f'{colors["green"]}Update successful!{colors["reset"]}')

            else:
                print('-------------------------------')
                print(f'{colors["red"]}Invalid category! Try again.{colors["reset"]}')
                return

        except ValueError:
            print('-------------------------------')
            print(f'{colors["red"]}Value must be an integer! Try again.{colors["reset"]}')

    def remove_book(self):
        '''Removes a book by its id'''
        try:
            book_id = int(input('Enter the book id to remove: '))

            self.cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
            selected_book = self.cursor.fetchone()
            if selected_book is None:
                print('-------------------------------')
                print(f'{colors["red"]}Book not found. Try again.{colors["reset"]}')
                return

            self.cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
            self.conn.commit()
            print('-------------------------------')
            print(f'{colors["green"]}Book removed successfully!{colors["reset"]}')

        except ValueError:
            print('-------------------------------')
            print(f'{colors["red"]}Value must be an integer! Try again.{colors["reset"]}')

    def generate_report(self):
        '''Generates report according to user selection'''
        print("--------- REPORTS ---------")
        print('What would you like to view?')
        print("1 - All books")
        print("2 - Books by author")
        print("3 - Available/unavailable books")
        print("0 - Back")
        print('-------------------------------')

        choice = input('Choose an option: ').strip()
        self.cursor.execute('SELECT * FROM books')
        books = self.cursor.fetchall()

        if choice == '1':
            for book in books:
                print(f'id-({colors["magenta"]}{book["id"]}{colors["reset"]}) : {colors["cyan"]}{book["title"]}{colors["reset"]}')
        elif choice == '2':
            for book in books:
                print(f'id-({colors["magenta"]}{book["id"]}{colors["reset"]}) = {book["title"]} : {colors["cyan"]}{book["author"]}{colors["reset"]}')
        elif choice == '3':
            for book in books:
                print(f'id-({colors["magenta"]}{book["id"]}{colors["reset"]}) = {book["title"]} : {colors["cyan"]}{book["availability"]}{colors["reset"]}')
        elif choice == '0':
            return
        else:
            print(f'{colors["red"]}Invalid option! Choose another.{colors["reset"]}')

    def menu(self):
        '''Displays main menu and returns user choice'''
        print('-------------------------------')
        print('------ Book System ------')
        print('-------------------------------')
        print('Choose an option:')
        print('1 - Add Book')
        print('2 - List Books')
        print('3 - Update Book')
        print('4 - Remove Book')
        print('5 - Generate Report')
        print('6 - Exit')
        print('-------------------------------')

        option = input('Choose an option: ').strip()
        print('-------------------------------')
        return option

    def run_system(self):
        while True:
            choice = self.menu()
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.list_books()
            elif choice == '3':
                self.update_book()
            elif choice == '4':
                self.remove_book()
            elif choice == '5':
                self.generate_report()
            elif choice == '6':
                print(f'{colors["green"]}System terminated!{colors["reset"]}')
                self.conn.close()
                break
            else:
                print(f'{colors["red"]}Invalid option! Choose another.{colors["reset"]}')

if __name__ == '__main__':
    app = BookSystem()
