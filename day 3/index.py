num = int(input("Enter the number whose multiplication table you want to display: "))

# Initialize the counter
i = 1

print("Multiplication Table of", num)
print("---------------------------")

# While loop to print the multiplication table
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
