try:
    num1 = int(input("enter number: "))
    num2 = int(input("enter number: "))
    print(f"divided value --> {num1/num2}")
except ValueError:
    print("enter a valid number.")
except ZeroDivisionError:
    print("cannot divided by zero")
    