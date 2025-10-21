""" 

Write Python Program to check whether an alphabet is a vowel or consonant? (use if, else
conditional statement).

"""

user = input("Enter an alphabet: ").lower()
if user in 'aeiou':
    print(f"{user} is a vowel.")
else:
    print(f"{user} is a consonant.")
    
