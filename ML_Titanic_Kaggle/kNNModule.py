# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:00:03 2018

@author: JBG
"""

from sklearn.neighbors import KNeighborsClassifier


def kNN(trainSet, trainLabels, testSet):
    clf = KNeighborsClassifier(n_neighbors=19)
    clf.fit(trainSet, trainLabels.ravel())
    predictedLabels = clf.predict(testSet)
    return predictedLabels
