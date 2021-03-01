# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:22:56 2018

@author: JBG
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

def rForest(trainSet,trainLabels, testSet):
    clf = RandomForestClassifier(max_depth = 7)
    clf.fit(trainSet,trainLabels.ravel())
    predictedLabels = clf.predict(testSet)
    return predictedLabels
    