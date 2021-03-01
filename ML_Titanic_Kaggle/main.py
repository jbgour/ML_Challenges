from numpy import *
from sklearn import cross_validation
from classify import classify
import pandas as pd
from preprocessingModule import *
import matplotlib.pyplot as plt

# Load data
listFeatures = [0,1,4,5,7]
X, y = preprocessingTrain('Data/train.csv', listFeatures) 

# Initialize cross validation
kf = cross_validation.KFold(X.shape[0], n_folds=10)

totalInstances = 0 # Variable that will store the total intances that will be tested  
totalCorrect = 0 # Variable that will store the correctly predicted intances  

for trainIndex, testIndex in kf:
    trainSet = X[trainIndex]
    testSet = X[testIndex]
    trainLabels = y[trainIndex]
    testLabels = y[testIndex]

    predictedLabels = classify(trainSet, trainLabels, testSet)
    # in classify, we choose the model
    
    correct = 0	
    for i in range(testSet.shape[0]):
        if predictedLabels[i] == testLabels[i]:
            correct += 1

    print ('Accuracy: ' + str(float(correct)/(testLabels.size)))
    totalCorrect += correct
    totalInstances += testLabels.size
        
print ('Total Accuracy: ' + str(totalCorrect/float(totalInstances)))
