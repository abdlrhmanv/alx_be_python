positive_number = int(input("Enter the size of the pattern:"))

row = 0
while row < positive_number:
    for col in range(positive_number):
        print("*", end="")
    print()  # Print newline after each row
    row += 1