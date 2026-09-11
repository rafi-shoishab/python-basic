fav_book = []

while True:
    print("0. exit")
    print("1. add book: ")
    print("2. remove book: ")
    print("3. show book list")

    choice = input("enter ur choice 0-3: ")

    if choice == '0':
        print("thanks")
        break
    elif choice == '1':
        book = input("enter ur book name u want to add: ")
        fav_book.append(book)
        print(f"{book} added in ur book list")
    
    elif choice == '2':
        book = input("enter ur book name u want to remove: ")

        if book in fav_book:
            fav_book.remove(book)
            print(f"{book} removed from ur book list")
        else:
            print(f"{book} is not exist in ur book list")

    elif choice == '3':
        if fav_book:
            print("Your books list:")
            for index, book in enumerate(fav_book, start=1):
                print(f"{index} = {book}")
        else:
            print("ur book list is empty")