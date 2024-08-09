import os
import platform

def clearScreen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def login():
    user = 'admin'
    password = 'admin123'
    login_attempts = 0
    
    while login_attempts < 3:
        clearScreen()
        username = input('Enter username: ')
        
        if username != user:
            print('Invalid Username')
            login_attempts += 1
            if login_attempts < 3:
                print(f'Attempt {login_attempts} of 3. Try again.')
            input('Press Enter to continue...')
            continue
        
        password_input = input('Enter password: ')
        
        if password_input != password:
            login_attempts += 1
            if login_attempts < 3:
                print(f'Attempt {login_attempts} of 3. Try again.')
            input('Press Enter to continue...')
        else:
            print('Login successful!')
            input('Press Enter to continue...')
            return
    
    print('Maximum login attempts reached. Program terminated.')

def display_books(books):
    clearScreen()
    if books:
        print("Books in Library:")
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book}")
    else:
        print("No books in the library.")
    input("Press Enter to continue...")

def add_book(books):
    clearScreen()
    book = input("Enter the title of the book to add: ")
    books.append(book)
    print(f'Book "{book}" added successfully!')
    input("Press Enter to continue...")

def remove_book(books):
    clearScreen()
    display_books(books)
    if books:
        book_number = int(input("Enter the number of the book to remove: "))
        if 1 <= book_number <= len(books):
            removed_book = books.pop(book_number - 1)
            print(f'Book "{removed_book}" removed successfully!')
        else:
            print("Invalid book number.")
    input("Press Enter to continue...")

def search_book(books):
    clearScreen()
    search_title = input("Enter the title of the book to search: ").lower()
    found_books = [book for book in books if search_title in book.lower()]
    if found_books:
        print("Books found:")
        for book in found_books:
            print(f"- {book}")
    else:
        print("No matching books found.")
    input("Press Enter to continue...")

def main():
    books = []
    while True:
        clearScreen()
        print("Library Management System")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_books(books)
        elif choice == '2':
            add_book(books)
        elif choice == '3':
            remove_book(books)
        elif choice == '4':
            search_book(books)
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()

