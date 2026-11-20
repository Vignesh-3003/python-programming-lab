contacts = []

while True:

    print("\nCONTACT BOOK")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)

        print("Contact added successfully!")

    elif choice == "2":

        print("\nSaved Contacts:")

        for contact in contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])

    elif choice == "3":

        print("Thank you!")
        break

    else:
        print("Invalid choice")