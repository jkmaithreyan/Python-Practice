contact_book = []

while True:
    user_choice = int(input("""
1. Add contact
2. Search contact
3. Show all contacts
4. Delete contact
5. Exit

Enter your choice: """))
    
    if user_choice == 1:
        name = input("enter name: ")
        number = input("enter number: ")
        if len(number) != 10:
            print("enter valid number")
            continue
        email = str(input("enter email: "))

        details = {
            "name": name,
            "number": number,
            "email": email
        }
        contact_book.append(details)

    elif user_choice == 2:
        search = input("enter name to get details: ")
        for details in contact_book:
            if search == details["name"]:
                print(f"{details}")

    elif user_choice == 3:
        for details in contact_book:
            print(f"name: {details['name']} -> number: {details['number']} -> email: {details['email']}")

    elif user_choice == 4:
        delete = input("enter name to delete contact: ")
        for details in contact_book:
            if delete == details["name"]:
                contact_book.remove(details)
                break

    elif user_choice == 5:
        print("goodbye!")
        break

    else:
        print("invalid entry")

