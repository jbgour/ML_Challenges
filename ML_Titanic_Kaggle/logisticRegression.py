# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:45:36 2018

@author: JBG
"""

from sklearn.linear_model import LogisticRegression



def logReg(trainSet,trainLabels,testSet):
    clf = LogisticRegression(random_state=0).fit(trainSet, trainLabels.ravel())
    clf.fit(trainSet,trainLabels.ravel())
    predictedLabels = clf.predict(testSet)
    return predictedLabels