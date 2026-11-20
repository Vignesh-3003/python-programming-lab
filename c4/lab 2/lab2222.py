filename = "students.txt"

while True:

    print("\nSTUDENT DATA MANAGER")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        with open(filename, "a") as file:

            file.write(roll + "," + name + "\n")

        print("Student data saved successfully!")

    elif choice == "2":

        try:

            with open(filename, "r") as file:

                print("\nSTUDENT RECORDS")

                for line in file:
                    print(line.strip())

        except FileNotFoundError:

            print("No records found")

    elif choice == "3":

        print("Program closed")
        break

    else:

        print("Invalid choice")