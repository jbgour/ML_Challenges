# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:33:46 2018

@author: JBG
"""

from sklearn.tree import DecisionTreeClassifier

def DTM(trainSet, trainLabels, testSet):
    clf = DecisionTreeClassifier(random_state = 0,max_depth = 5)
    clf = clf.fit(trainSet,trainLabels)
    predictedLabels = clf.predict(testSet)
    return predictedLabels