"""

Write a Python script that asks users for their favourite color. Create the following output
(assuming blue is the chosen color) (hint: use ‘+’ and ‘*’)
blueblueblueblueblueblueblueblueblueblue
blue                                blue
blueblueblueblueblueblueblueblueblueblue


"""

color = input("What is your favourite color? ")
repeats = 15 
top_bottom_line = color * repeats

width = len(top_bottom_line)
space_length = width - len(color) - len(color)
middle_space = " " * space_length
middle_line = color + middle_space + color

print(top_bottom_line)
print(middle_line)
print(top_bottom_line)
