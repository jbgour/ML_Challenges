# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:20:12 2018

@author: JBG
"""

from sklearn import neural_network

def MLP(trainSet,trainLabels, testSet):
    clf = neural_network.MLPClassifier()
    clf.fit(trainSet,trainLabels.ravel())
    predictedLabels = clf.predict(testSet)
    return predictedLabels