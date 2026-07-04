try:
    num = int(input("enter a number: "))
except ValueError:
    print("please enter valid number.")
else:
    print(f" square of {num} is {num*num}")
finally:
    print("Thanks for using calculator")