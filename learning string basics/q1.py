num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
num3 = int(input("enter number 3: "))
num4 = int(input("enter number 4: "))
num5 = int(input("enter number 5: "))
greater = 0
if num1 > num2:
    greater = num2
elif num3 > greater:
    greater = num3
elif num4 > greater:
    greater = num4
elif num5 > greater:
    greater = num5
else:
    greater = num1
print(greater)


