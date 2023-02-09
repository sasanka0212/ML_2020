# Assignment 03 - Question 02

"""
write a program to inverse 3x3 matrix. create class matrix and built the methods inverse, adjoint,
traanspose, determinant for the above program.(can use library functions)
"""

import numpy as np
mat = np.array([[5,6,1], [8,9,11], [10,7,4]])

class Matrix:
    def __init__(self, mat):
        self.mat = mat
    def adjoint(self):
        mtrx = self.mat.ravel()  #ravel() converts 2d array to 1d. Just to make things easier.
        A= +((mtrx[4]*mtrx[8])-(mtrx[5]*mtrx[7]))
        B= -((mtrx[3]*mtrx[8])-(mtrx[5]*mtrx[6]))
        C= +((mtrx[3]*mtrx[7])-(mtrx[6]*mtrx[4]))
        D= -((mtrx[1]*mtrx[8])-(mtrx[2]*mtrx[7]))
        E= +((mtrx[0]*mtrx[8])-(mtrx[2]*mtrx[6]))
        F= -((mtrx[0]*mtrx[7])-(mtrx[1]*mtrx[6]))
        G= +((mtrx[1]*mtrx[5])-(mtrx[2]*mtrx[4]))
        H= -((mtrx[0]*mtrx[5])-(mtrx[2]*mtrx[3]))
        I= +((mtrx[0]*mtrx[4])-(mtrx[1]*mtrx[3]))
        #Convert back to 3×3 matrix format
        self.cofactor = np.array([[A, B, C],
                            [D, E, F],
                            [G, H, I]])
        self.adjnt = self.cofactor.T
        print("adjoint matrix:\n", self.adjnt)
    def determinant(self):
        self.det_val = np.linalg.det(self.mat)
        print("determinant value:\n",self.det_val)
    def transpose(self):
        self.transpose_mat = self.mat.T
        print("transpose matrix:\n",self.transpose_mat)
    def inverse(self):
        self.inv_mat = np.empty((3,3))
        for i in range(3):
            for j in range(3):
                self.inv_mat[i][j] = self.adjnt[i][j] / self.det_val
        print("inverse matrix:\n",self.inv_mat)

obj = Matrix(mat)
obj.adjoint()
obj.determinant()
obj.transpose()
obj.inverse()