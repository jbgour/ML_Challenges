# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:57:21 2018

@author: JBG
"""

from sklearn import ensemble

def boosting(trainSet,trainLabels, testSet):
    clf = ensemble.GradientBoostingClassifier(max_depth = 7)
    clf.fit(trainSet,trainLabels.ravel())
    predictedLabels = clf.predict(testSet)
    return predictedLabels