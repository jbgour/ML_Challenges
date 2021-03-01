# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 16:24:59 2019

@author: JBG
"""

from numpy import *
from sklearn import cross_validation
from classify import classify
import pandas as pd
from preprocessingModule import *
import matplotlib.pyplot as pd
from MSEModule import * 

# Load data

X, y = preprocessingTrain('Data/9610-2005.csv') 

# Initialize cross validation
kf = cross_validation.KFold(X.shape[0], n_folds=10)

totalInstances = 0 # Variable that will store the total intances that will be tested  
totalMSE = 0 # Variable that will store the mean squared error 

for trainIndex, testIndex in kf:
    trainSet = X[trainIndex]
    testSet = X[testIndex]
    trainLabels = y[trainIndex]
    testLabels = y[testIndex]
        
    predictedLabels = classify(trainSet, trainLabels, testSet)
    # in classify, we choose the model
    
    meanSquaredError = MSE(testLabels, predictedLabels)
    
    print("Mean Squared Error: "+ str(meanSquaredError))
    
    totalMSE += meanSquaredError
    totalInstances += 1
        
print ('Total Mean Squared Error: ' + str(totalMSE/float(totalInstances)))

    
 