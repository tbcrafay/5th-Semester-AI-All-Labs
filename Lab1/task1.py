"""

Write a script that take user input for a number then adds 3 to that number. Then multiplies the
result by 2, subtract 4, then again adds 3, then print the result.

"""

user = int(input("Enter a number: "))
added = user + 3
print("After adding 3:", added)
multiplied = added * 2 
print("After multiplying by 2:", multiplied)
subtracted = multiplied - 4
print("After subtracting 4:", subtracted)
final_result = subtracted + 3
print("The final result is:", final_result)
