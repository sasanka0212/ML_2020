"""
Consider the iris dataset is stored in a .csv file. Load the data and use Naive Byesian Classifier to find the 
class of a data whose attributes are (6.4, 3.3, 1.9, 1.3).
"""

import NaiveBayes as nv
import numpy as np
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/ket-sourav-ket/ML_listings/master/demo/YQ_2021_Q8/iris.csv',header=None,encoding='utf-8')
Y=df.iloc[0: , 4].values
X=df.iloc[0: , 0:4].values

classifier = nv.NaiveBayesClassifier(X,Y.T)
prediction = classifier.predict(np.array([6.4,3.3,1.9,1.3]))

print('the flower is predicted to be ' + prediction)