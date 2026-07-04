while True:
    try:
        num1 = int(input("enter a number: "))
        num2 = int(input("enter a number: "))
        operator = input("enter operation: ")
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        elif operator == "exit":
            print("goodbye!")
            break
        else:
            print("enter valid operation")
            continue

    except ValueError:
        print("enter valid number!")
    except ZeroDivisionError:
        print("cannot divide by zero!")
    else:
        print(f"Result --> {result}")
    finally:
        print("next calculation")