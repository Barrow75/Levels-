# Library management

def AvailableBooks(available):

    if not  available:
        print("Book currently not available")
    else:
        for title, name in available.items():
            print(f'- {name}')



def Borrow_Book(available, borrowed):
    book_name = input("What book wopuld you like to borrow? ")
    for title, name in available.items():
        if name.lower() == book_name.lower():
            borrowed[title] = available.pop(title)
            print(f"You have borrowed {name}")
            return
    print("Book is not available")


def Return_Book(available, borrowed):
    book_name = input("Book you want to return? ")
    for title, name in borrowed.items():
        if name.lower() == book_name.lower():
            available[title] = borrowed.pop(title)
            print(f"You borrowed {name}")
    print("Book is not in borrowed")


def Add_Book(available):
    book_name = input("Add a book")
    book_key = f"title_{len(available) + 1}"
    available[book_key] = book_name
    print(f"{book_name} has been added to available books")


def main():
    library = {
        'Title_1': "Hands on Hacking",
        'Title_2': "Linux Commands",
        "Title_3": 'Python'
    }
    borrowed_books = {}

    while True:
        try:
            user_choice = int(input("Choose options: \n" "1. View Available Books, \n"
                                    "2. Borrow a Book, \n"
                                    "3. Return a Book, \n"
                                    "4. Add a new Book, \n"
                                    "Choose: "))

            if user_choice == 1:
                AvailableBooks(library)
            elif user_choice == 2:
                Borrow_Book(library, borrowed_books)
            elif user_choice == 3:
                Return_Book(library, borrowed_books)
            elif user_choice == 4:
                AvailableBooks(library)
                print("Thank you for using the library system")

                break

        except ValueError:
            print("Invalid")
       # break


#main()
if __name__ == "__main__":
    main()
