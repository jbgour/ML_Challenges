# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:41:01 2018

@author: JBG
"""

# it is a module to help vizualizing data influence


from numpy import *
from sklearn import cross_validation
from classify import classify
import pandas as pd
from preprocessingModule import *
import matplotlib.pyplot as plt

# Load data
X, y = preprocessingTrain('Data/train.csv')

def premierPlot():
    names = ['died','survived']
    values = [0,0]
    n= y.shape[0]
    for i in range(n):
        if y[i,0]==0:
            values[0] += 1
        else:
            values[1]+= 1
    values[0] = values[0]/n*100
    values[1] = values[1]/n*100
    plt.ylabel('proportion of Titanic people')
    plt.title('Vizualization of the training Dataset')
    plt.bar(names,values)
    plt.show()

def plotSex():
    names = ['died','survived']
    MaleValues = [0,0]
    FemaleValues = [0,0]
    n= y.shape[0]
    nMale= 0
    nFemale = 0
    for i in range(n):
        if X[i,1] == 0:
            nMale+=1
            if y[i,0]==0:
                MaleValues[0] += 1
            else:
                MaleValues[1]+= 1
        else:
            nFemale +=1
            if y[i,0]==0:
                FemaleValues[0] += 1
            else:
                FemaleValues[1]+= 1
    print(nMale,nFemale)
    MaleValues = [i/nMale*100 for i in MaleValues]
    FemaleValues = [i/nFemale*100 for i in FemaleValues]
    plt.figure(1)
    plt.suptitle('Gender Influence')
    plt.subplot(121)
    plt.bar(names,MaleValues,label = 'Male dataSet')
    plt.ylabel('proportion of Males')
    plt.subplot(122)
    plt.bar(names,FemaleValues,label = 'Female dataSet')
    plt.ylabel('proportion of females')
    plt.show()
    
def plotPort():
    names = ['S','C','Q']
    Values = [0,0,0]
    n= y.shape[0]
    nS= 0
    nC = 0
    nQ = 0
    for i in range(n):
        if X[i,-1] == 0:
            nS+=1
            if X[i,1]==1:
                Values[0] += 1
        elif X[i,-1] == 1:
            nC +=1
            if X[i,1]==1:
                Values[1] += 1
        else :
            nQ +=1
            if X[i,1]==1:
                Values[2] += 1
        
    Values[0] = Values[0]/nS*100
    Values[1] = Values[1]/nC*100
    Values[2] = Values[2]/nQ*100


    plt.bar(names,Values)
    plt.ylabel('proportion of people who survived')

    plt.show()
    
def plotClass():
    names = [1,2,3]
    Values = [0,0,0]
    n= y.shape[0]
    n1 = 0
    n2 = 0
    n3 = 0
    for i in range(n):
        if X[i,0] == 1:
            n1 += 1
            if y[i,0]==1:
                Values[0] += 1
        elif X[i,0] == 2:
            n2 += 1
            if y[i,0]==1:
                Values[1] += 1
        else :
            n3 += 1
            if y[i,0]==1:
                Values[2] += 1
        
    Values[0] = Values[0]/n1*100
    Values[1] = Values[1]/n2*100
    Values[2] = Values[2]/n3*100


    plt.bar(names,Values)
    plt.ylabel('proportion of people who survived')
    plt.title('Influence of the class')
    plt.show()
 
def plotIsAlone():
    names = ['isAlone','not Alone']
    Values = [0,0]
    n = y.shape[0]
    n0 = 0
    n1 = 0
    for i in range(n):
        if X[i,-1] == 0:
            n0 += 1
            if y[i,0]==1:
                Values[0] +=1
        else:
            n1 +=1
            if y[i,0] == 1:
                Values[1] +=1
    
    Values[0] = Values[0]/n0*100
    Values[1] = Values[1]/n1*100
    
    plt.bar(names,Values)
    plt.ylabel('proportion of people who survived')
    plt.title('Influence of the family')
    plt.show()