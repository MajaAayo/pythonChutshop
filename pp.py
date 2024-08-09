import os
import platform
import sys

library: list = []
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
        try:
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
                print('Invalid Password')
                login_attempts += 1
                if login_attempts < 3:
                    print(f'Attempt {login_attempts} of 3. Try again.')
                input('Press Enter to continue...')
            else:
                print('Login successful!')
                input('Press Enter to continue...')
                return
        
        except KeyboardInterrupt:
            print("\nProcess interrupted. Exiting program.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            input('Press Enter to continue...')

    print('Maximum login attempts reached. Program terminated.')
    sys.exit()

def addBook(library):
    clearScreen()
    title = input("Enter the title of the book to add: ")
    author = input("Enter author name: ")
    price = input("Enter book price: ")
    
    book = {
        'title': title,
        'author': author,
        'price': price
    }
    
    library.append(book)
    # yield library
    
    print(f'Book "{title}" added successfully!')
    input("Press Enter to continue...")
def displayBook(library):
    clearScreen()
    print("Available books:")
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book}")
    
    input("Press Enter to continue...")

def searchBook(library):
    clearScreen()
    search_title = input("Enter the title of the book to search: ")
    found_books = [book for book in library if search_title in book]
    if found_books:
        print("Books found:")
        for book in found_books:
            print(f"- {book}")
    else:
        print("No matching books found.")
    input("Press Enter to continue...")
def removeBook(library):
    clearScreen()
    title_to_remove = input("Enter the title of the book to remove: ").strip()
    
    # Find and remove the book based on title
    book_found = False
    for book in library:
        if book['title'].strip() == title_to_remove:
            library.remove(book)
            print(f'Book "{title_to_remove}" removed successfully!')
            book_found = True
            break
    
    if not book_found:
        print(f'Book "{title_to_remove}" not found.')
    
    input("Press Enter to continue...")



def main():

    # login() 

    while True:
        clearScreen()
        print("Library Management System")
        print("1. Add a book")
        print("2. Display all books")
        print("3. Search for a book")
        print("4. Remove a book")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): ").strip())
            
            if choice == 1:
                addBook(library)
            elif choice == 2:
                displayBook(library)
            elif choice == 3:
                searchBook(library)
            elif choice == 4:
                removeBook(library)
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
                input("Press Enter to continue...")
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
