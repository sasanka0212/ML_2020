# Assignment 01_1

"""
Write a python program to perform addition, subtraction, multiplication of matrices without using 
any library.
"""

# without using any library functions

matrix1 = []
matrix2 = []
matrix3 = []
matrix4 = []
matrix5 = []
temp = []
rowLen1 = int(input('enter row no for 1st matrix:'))
colLen1 = int(input('enter column no for 1st matrix:'))

for i in range(rowLen1):
    for j in range(colLen1):
        ele = input('enter element no[%d][%d]:'%(i,j))
        temp.append(int(ele))
    matrix1.append(temp.copy())
    temp.clear()

rowLen2 = int(input("enter row no for 2nd matrix:"))
colLen2 = int(input("enter column lo for 2nd matrix :"))

for i in range(rowLen2):
    for j in range(colLen2):
        ele = input('enter element no[%d][%d]:'%(i,j))
        temp.append(int(ele))
    matrix2.append(temp.copy())
    temp.clear()

print("1st matrix : ")
print(matrix1)
print("2nd matrix : ")
print(matrix2)

if rowLen1==rowLen2 and colLen1==colLen2:
    for i in range(rowLen2):
        for j in range(colLen2):
            temp.append(matrix1[i][j] + matrix2[i][j])
        matrix3.append(temp.copy())
        temp.clear()
    for i in range(rowLen2):
        for j in range(colLen2):
            temp.append(matrix1[i][j] - matrix2[i][j])
        matrix4.append(temp.copy())
        temp.clear()
    print("addition of two matrix : ")
    print(matrix3)
    print("subtraction of two matrix : ")
    print(matrix4)
else:
    print("addition is not possible")
    print("subtraction is not possible")

# calculate the multiplication
if colLen1==rowLen2:
    for i in range(rowLen1):
        for j in range(colLen2):
            temp.append(0)
            for k in range(rowLen2):
                temp[j] += (matrix1[i][k] * matrix2[k][j])
        matrix5.append(temp.copy())
        temp.clear()
    print("multiplication of two matrix : ")
    print(matrix5)
elif colLen2==rowLen1:
    for i in range(rowLen2):
        for j in range(colLen1):
            temp.append(0)
            for k in range(rowLen1):
                temp[j] += (matrix2[i][k] * matrix1[k][j])
        matrix5.append(temp.copy())
        temp.clear()
    print("multiplication of two matrix : ")
    print(matrix5)
else:
    print("multiplication is not possible")