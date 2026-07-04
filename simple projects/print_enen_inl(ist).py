numbers = []
even_numbers = []

times = int(input(" enter how many numbers: "))
for i in range(1,times + 1):
    num = int(input(f"enter number {i}: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)
        

