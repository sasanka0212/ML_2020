# Assignment 03 - Question 01

"""
You are given two integer arrays A and B of dimentions N x M, your task is to perform the following 
operations -
1. add(A+B)
2. subtract(A-B)
3. multiply(A-B)
4. integer division(A/B)
5. mod(A%B) 
get the inputs and display the outputs in a file.(can use library functions)
"""

import numpy as np
import sys as s

stdoutOrigin = s.stdout 

M = int(input("enter row size : "))     #get input from user
N = int(input("enter column size : "))

arr1 = np.empty([M,N], dtype = int)
arr2 = np.empty([M,N], dtype = int)

print("enter value for 1st matrix : ")
for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        arr1[i][j] = int(input("enter value : "))

print("enter value for 2nd matrix : ")
for i in range(len(arr2)):
    for j in range(len(arr2[0])):
        arr2[i][j] = int(input("enter value : "))

s.stdout = open("ass_1.txt", "w")
print("1st matrix:\n", arr1)
print("2nd matrix:\n", arr2)

arr3 = np.empty([M,N], dtype = int)
arr3 = arr1 + arr2
print("addition of two matrix:\n", arr3)

arr4 = np.empty([M,N], dtype = int)
arr4 = arr1 - arr2
print("substraction of two array:\n ", arr4)

if len(arr1[0])==len(arr2):
    arr5 = np.empty([len(arr1),len(arr2[0])], dtype = int)
    arr5 = np.matmul(arr1, arr2)
    print("multiplication of two array :\n", arr5)
else:
    print("dimentions are not satisfied for multiplication...")

arr6 = np.empty([M,N], dtype = int)
for i in range(M):
    for j in range(N):
        arr6[i][j] = arr1[i][j] // arr2[i][j]
print("integer division of two arrays :\n", arr6)

arr7 = np.empty([M,N], dtype = int)
for i in range(M):
    for j in range(N):
        arr7[i][j] = arr1[i][j] % arr2[i][j]
print("modulous of two arrays :\n", arr7)

s.stdout.close()
s.stdout=stdoutOrigin