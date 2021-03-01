# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 01:02:42 2018

@author: JBG
"""

from numpy import *
from classify import classify
import pandas as pd
from preprocessingModule import *


# Load data
listFeatures = [0,1,4,5,7]
trainSet, trainLabels = preprocessingTrain('Data/train.csv',listFeatures) 
testSet = preprocessingTest('Data/test.csv',listFeatures) 
	
predictedLabels = list(classify(trainSet, trainLabels, testSet))
for i in range(len(predictedLabels)):
    predictedLabels[i] = int(predictedLabels[i]) #just transforming floats into integers

d = {'PassengerId':[i for i in range(892,892+418)], 'Survived':predictedLabels} #abiding rules
df = pd.DataFrame(d, columns = ['PassengerId','Survived'])  #creating my dataframe

df.to_csv('results.csv',index = None, header=True) #export the csv file