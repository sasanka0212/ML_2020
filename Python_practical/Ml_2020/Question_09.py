import numpy as np
import matplotlib.pyplot as plt
  
# Taking a 4 * 4 matrix
A = np.array([[6, 1, 1, 3],
              [4, 10, 5, 1],
              [2, 8, 7, 6],
              [3, 1, -9, 7]])
  
# Calculating the inverse of the matrix
B = np.linalg.inv(A)
print("inverse of the given array : ", B)

plt.rcParams["figure.figsize"] = [7.00, 4.00]
plt.rcParams["figure.autolayout"] = True

colorPlotA = plt.imshow(A, cmap = "copper_r")
plt.colorbar(colorPlotA)
plt.show()