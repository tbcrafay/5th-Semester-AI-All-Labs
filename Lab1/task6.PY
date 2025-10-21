"""
Write a python script that take a user input and to create the multiplication table (from 1 to 10)
of that number.

"""

num = int(input("Enter a number to generate its multiplication table: "))
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")   