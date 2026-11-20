books = []

while True:

    print("\nLIBRARY MANAGEMENT SYSTEM")

    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        title = input("Enter book name: ")

        books.append({
            "title": title,
            "available": True
        })

        print("Book added successfully!")

    elif choice == "2":

        print("\nAVAILABLE BOOKS")

        for book in books:

            if book["available"]:
                status = "Available"
            else:
                status = "Borrowed"

            print(book["title"], "-", status)

    elif choice == "3":

        title = input("Enter book name to borrow: ")

        for book in books:

            if book["title"].lower() == title.lower() and book["available"]:

                book["available"] = False

                print("Book borrowed successfully!")

                break

        else:

            print("Book not available")

    elif choice == "4":

        print("Thank you!")
        break

    else:

        print("Invalid choice")