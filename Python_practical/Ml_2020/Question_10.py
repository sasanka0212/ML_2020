import matplotlib.pyplot as plt
import numpy as np
import math as m
from tabulate import tabulate
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
 
# Creating vectors X and Y
x = np.array([0,1,2,3,4])
y = x**2
 
fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(x, y)
 
# Show the plot
plt.show()

myTable = [[0, m.cos(0)],[1, m.cos(1)], [2, m.cos(2)], [3, m.cos(3)], [4, m.cos(4)]]
head = ["x","y"]
print(tabulate(myTable, headers=head, tablefmt="grid"))

y = np.array([1,0.540,-0.416,-0.989,-0.653])
n = np.size(x)
  
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean,y_mean
  
Sxy = np.sum(x*y)- n*x_mean*y_mean
Sxx = np.sum(x*x)-n*x_mean*x_mean
  
b1 = Sxy/Sxx
b0 = y_mean-b1*x_mean
print('slope b1 is', b1)
print('intercept b0 is', b0)
  
plt.scatter(x,y)
plt.xlabel('Independent variable X')
plt.ylabel('Dependent variable y')