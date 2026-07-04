email = str(input("enter email: "))
if "@" in email and email.endswith(".com"):
    print("valid email")
else:
    print("invalid email")