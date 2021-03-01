# here we chosse the model

from numpy import *
from LinearRegressionModule imprt *

def classify(trainSet, trainLabels, testSet,k):
	
    predictedLabels = linearRegression(trainSet, trainLabels, testSet)
    # could be kNN, boosting, logReg, rForest, DTM, MLP
    return predictedLabels

