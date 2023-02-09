# Assignment 01_2

"""
Write a python program to perform addition, subtraction, multiplication of matrices using library.
"""

# using numpy module

from numpy import *
matrix1 = array([])
matrix2 = array([])
rowLen1, colLen1 = int(input("enter row no :")), int(input("enter column no :"))

for i in range(rowLen1):
    temp = array([])
    for j in range(colLen1):
        x = float(input("enter ele :"))
        append(temp,x)
        append(matrix1,temp)

rowLen2, colLen2 = int(input("enter row no :")), int(input("enter column no :"))

for i in range(rowLen1):
    temp = array([])
    for j in range(colLen1):
        x = float(input("enter ele :"))
        append(temp,x)
        append(matrix2,temp)

print("1st matrix : ")
print(matrix1)
print("2nd matrix : ")
print(matrix2)

# addition of two matrix
if rowLen1==rowLen2 and colLen1==colLen2:
    matrix3 = matrix1 + matrix2
    matrix4 = matrix1 - matrix2
    print("addition of two matrix : ")
    print(matrix3)
    print("subtraction of two matrix : ")
    print(matrix4)
else:
    print("addition and subtraction are not possible")

# multiplication of two matrix
if colLen2==rowLen2:
    matrix5 = matrix1 * matrix2
    print("multiplication of two matrix : ")
    print(matrix5)
elif colLen2==rowLen1:
    matrix5 = matrix2 * matrix1
    print("multiplication of two matrix : ")
    print(matrix5)
else:
    print("multiplication is not possible")