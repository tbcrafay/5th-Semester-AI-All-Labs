"""
Write a function called absolute_num() that accepts one parameter, num. The function should
return only positive value, and apply condition on it. This function returns the absolute value of
the entered number
"""

def absolute_num(num):
    if num < 0:
        return -num
    else:
        return num


print(absolute_num(-10))  