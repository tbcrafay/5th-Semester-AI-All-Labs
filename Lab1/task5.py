"""

Store a person’s name, and include some whitespace characters at the beginning and end of
the name. Make sure you use each character combination, "\t" and "\n", at least once. Print
the name once, so the whitespace around the name is displayed. Then print the name using
each of the three stripping functions, lstrip( ), rstrip(), and strip().

"""


name_with_whitespace = "\t  \nEric \tIdle\n  "

print("--- Original Name (Whitespace Displayed) ---")
print(repr(name_with_whitespace))

print("\n--- Original Name (Formatted View) ---")
print(name_with_whitespace)

print("\n--- Demonstration of Stripping Functions ---")

left_stripped_name = name_with_whitespace.lstrip()
print(f"lstrip(): '{left_stripped_name}'")

right_stripped_name = name_with_whitespace.rstrip()
print(f"rstrip(): '{right_stripped_name}'")

fully_stripped_name = name_with_whitespace.strip()
print(f"strip():  '{fully_stripped_name}'")
