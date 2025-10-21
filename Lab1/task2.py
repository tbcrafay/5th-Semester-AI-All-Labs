"""

Write a script that takes input as Celsius and then convert Celsius to Fahrenheit. (hint:
Fahrenheit = (Celsius * 1.8) + 32)

"""


celsius_temp = float(input("Enter temperature in Celsius: "))

converted_temp = (celsius_temp * 1.8) + 32

print(f"{celsius_temp}°C is equal to a converted value of {converted_temp:.2f}")

