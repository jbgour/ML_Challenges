# here we chosse the model

from numpy import *
from LinearRegressionModule import *
from kNNModule import *
from SVRModule import *

def classify(trainSet, trainLabels, testSet):
	
    predictedLabels = linearRegression(trainSet, trainLabels, testSet)
    # could be kNN, boosting, logReg, rForest, DTM, MLP
    return predictedLabels

