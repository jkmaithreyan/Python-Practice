balance = 5000

while True:
    try:
        user_input = int(input("""
1.check balance
2.deposit
3.withdraw
4.exit

Enter your need: """))
    except ValueError:
        print("enter valid numbers from (1 to 4)")
        continue
    else:
        if user_input == 1:
            print(f"Current Balalce --> {balance}")
        elif user_input == 2:
            deposit_amount = int(input("enter amount to deposit: "))
            balance = balance + deposit_amount
            print(f"new balance --> {balance}")
        elif user_input == 3:
            withdraw_amount = int(input("enter amount to withdraw: "))
            if withdraw_amount > balance:
                print("insufficient balance!")
            else:
                balance = balance - withdraw_amount
                print(f"new balance --> {balance}")
        elif user_input == 4:
            print("goodbye!")
            break
        else:
            print("please enter valid number from (1 - 4)")
    finally:
        print("happy banking with us!!!")