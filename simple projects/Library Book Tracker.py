library = []

while True:
    user_choice = int(input("""
1. Add book
2. Search book
3. Show all books
4. Remove book
5. Exit

choose option: """))
    
    if user_choice == 1:
        name = input("Enter book name: ")
        author = input("enter author name: ")
        available = input("enter availability (yes/no): ")
        if available == "yes":
            available = True
        else:
            available = False
        books = {
            "name": name,
            "author": author,
            "available": available
        }
        library.append(books)
        print(library)

    elif user_choice == 2:
        search = input("enter book name: ")
        for books in library:
            if search == books["name"]:
                print(books["available"])
                break

    elif user_choice == 3:
        for books in library:
            print(f"{books['name']} -- {books['author']} -- {'yes' if books['available'] else 'no'}")

    elif user_choice == 4:
        remove  = input("enter book name to remove: ")
        for books in library:
            if remove == books["name"]:
                library.remove(books)
                break

    elif user_choice == 5:
        print("goodbye!")
        break

    else:
        print("invalid entry")

    


        