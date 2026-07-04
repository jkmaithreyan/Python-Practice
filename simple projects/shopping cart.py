cart = []


while True:
    user_choice = int(input("""
1. Add item
2. Remove item
3. View cart
4. Total price
5. Exit
                            
choose the option:"""))
    
    if user_choice == 1:
        name = input("enter item name: ")
        price = int(input("enter price: "))
        item ={
            "name": name,
            "price":price
        }
        cart.append(item)
    elif user_choice == 2:
        remove = input("enter item name to remove: ")
        for item in cart:
            if item["name"] == remove:
                cart.remove(item)
                break

    elif user_choice == 3:
        for item in cart:
            print(f"{item['name']} - {item['price']}")

    elif user_choice == 4:
        total = 0
        for item in cart:
            total = total + item["price"]
        print(f"Total : {total}")

    elif user_choice == 5:
        break
    
    else:
        print("invalid entry")








        
      
                        