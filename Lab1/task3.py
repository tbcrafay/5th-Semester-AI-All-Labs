"""

Write a script that takes input as radius then calculate area of circle. (hint: A = πr²)

"""

radius = float(input("Enter the radius of the circle: "))
Area = 3.14159 * (radius ** 2)
print(f"The area of the circle with radius {radius} is {Area:.2f}")