"""
Write a program to implement the Naive Bayesian Classifier for a sample training dataset stored a .csv file.
Compute the accuracy of the classifier, considering few test datasets.
"""

import NaiveBayes as nv
import numpy as np
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/ket-sourav-ket/ML_listings/master/demo/YQ_2021_Q8/iris.csv',header=None,encoding='utf-8')
Y=np.atleast_2d(df.iloc[0: , 4].values).T
X=df.iloc[0: , 0:4].values



X_train= np.concatenate((X[0:25],X[50:75],X[100:125]),axis=0)
Y_train = np.concatenate((Y[0:25],Y[50:75],Y[100:125]),axis=0)
X_test = np.concatenate((X[25:50],X[75:100],X[125:150]),axis=0)
Y_test = np.concatenate((Y[25:50],Y[75:100],Y[125:150]),axis=0)




classifier = nv.NaiveBayesClassifier(X_train,Y_train)
prediction = np.copy(Y_test)

hit_counter=0

for i in range(X_test.shape[0]):
    prediction[i]= classifier.predict(X_test[i])
    if (prediction[i]==Y_test[i]):
        hit_counter+=1

accuracy= (hit_counter/Y_test.shape[0])*100

print(f"the accuracy of the naive bayes classifier is {accuracy}%")