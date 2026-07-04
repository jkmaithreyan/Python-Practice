password = input("enter password: ")

if len(password) < 8:
    print("password must contain 8 or above characters.")

else:
    has_number = False
    has_capital = False
    has_special = False
    for char in password:
        if char in "1234567890":
            has_number = True
        elif char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            has_capital = True
        elif char in "!@#$":
            has_special = True

    print(f"has number: {'pass' if has_number else 'fail'}")
    print(f"has capital: {'pass' if has_capital else 'fail'}")
    print(f"has special: {'pass' if has_special else 'fail'}")

    if has_number and has_capital and has_special:
        print("strong password")
    else:
        print("weak password")

        
        