"""

Write a Python program to construct the following pattern. (using nested loop)
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=' ')
    print() 

