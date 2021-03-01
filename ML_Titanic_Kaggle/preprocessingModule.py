# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:54:04 2018

@author: JBG
"""

from numpy import *
import pandas as pd
from sklearn import preprocessing  
from toolbox import *
# Load data


def preprocessingTrain(pathFile, listFeatures):
    #pathFile is the path of the dataset
    #returns X and Y, after deleting useless attributes
    
    # Load data
    csv_file_object = pd.read_csv(pathFile, delimiter=',') # Load in the csv file
    XX=array(csv_file_object.values)  # Create a variable to hold the data, type array
    
    n= XX.shape[0]
    X = zeros((n,8))
    y = zeros((n,1))

    for i in range(n):
        
        lX = XX[i,0].split(',') # Split of the first column so that it usable

        y[i,0] = lX[1]          # Save labels to y        
        del lX[1]               # delete the label inserted in y
        
            
        ## processing of male
        ## 0 for male, 1 for female
        if lX[4] == 'male':   
            lX[4] = 0
        elif lX[4] == 'female':
            lX[4] = 1
        
        
         ## when the age is unknown, we set it to NaN
        if lX[5] == '':
            lX[5] = NaN
        
        
        ## processing of cabins
        ## 0 if no cabin, 1 if there is
        if lX[10] == '':
            lX[10] = 0
        else:
            lX[10] = 1
                 
        ## processing of ports 
        ## 0 for Southampton or unknown, 1 for Cherbourg, 2 for Queens
        if lX[11] == 'S' or lX[11] == '':
            lX[11] = 0
        elif lX[11] == 'C':
            lX[11] = 1
        else:
            lX[11] = 2
            
                
        ## processing of isAlone
        ## 0 if alone, 1 else
        if int(lX[6]) == 0:
            if int(lX[7]) == 0:
                X[i,6] = 0
            else :
                X[i,6] = 1
        else: 
            X[i,6] = 1
        
        
        #processing of person title
        k = 1        
        title = ''
        while lX[3][k] != ' ':
            title += lX[3][k]
            k +=1
        if title == 'Mr.':
            X[i,7] = 0
        elif title  == 'Miss.':
            X[i,7] = 1
        elif title  == 'Mrs.':
            X[i,7] = 2
        elif title  == 'Master.':
            X[i,7] = 3
        else:
            X[i,7] = 4
            
       
        
        
        del lX[0]               # delete the PassengerID
        
        del lX[1:3]             # delete name and surname, not useful
        #del lX[2]               # delete the age
        del lX[3]               # delete sibsp
        del lX[3]               # delete parch
        del lX[3]               # delete ticket
        #del lX[2]               # delete fare
        del lX[4]               # delete cabin

        
        for k in range(5):
            X[i,k] = lX[k]
        
        
        ##setting the age to the average value when unknown and when age is asked
        if 2 in listFeatures:
            X = nanToAvg(X,2) # nanToAvg is in toolbox module
        

    print('hey')
    #X = preprocessing.scale(X)
    return X[:,listFeatures],y 
    # 0 : PClass
    # 1 : Sex
    # 2 : age
    # 3 : fare
    # 4 : cabin
    # 5 : port
    # 6 : isAlone
    # 7 : title
    

def preprocessingTest(pathFile,listFeatures):
    #pathFile is the path of the dataset
    #returns X and Y, after deleting unuseful attributes
    
    # Load data
    csv_file_object = pd.read_csv(pathFile, delimiter=',') # Load in the csv file
    XX=array(csv_file_object.values)  # Create a variable to hold the data, type array
    n= XX.shape[0]
    X = zeros((n,8))

    for i in range(n):
        lX = XX[i,0].split(',') # Split of the first column so that it usable
        
        ## processing of male
        ## 0 for male, 1 for female
        if lX[4] == 'male':   
            lX[4] = 0
        elif lX[4] == 'female':
            lX[4] = 1
        
        
         ## when the age is unknown, we set it to NaN
        if lX[5] == '':
            lX[5] = NaN
        
        if lX[9] == '':
            lX[9] = NaN
        
        ## processing of cabins
        ## 0 if no cabin, 1 if there is
        if lX[10] == '':
            lX[10] = 0
        else:
            lX[10] = 1
                 
        ## processing of ports 
        ## 0 for Southampton or unknown, 1 for Cherbourg, 2 for Queens
        if lX[11] == 'S' or lX[11] == '':
            lX[11] = 0
        elif lX[11] == 'C':
            lX[11] = 1
        else:
            lX[11] = 2
            
                
        ## processing of isAlone
        ## 0 if alone, 1 else
        if int(lX[6]) == 0:
            if int(lX[7]) == 0:
                X[i,6] = 0
            else :
                X[i,6] = 1
        else: 
            X[i,6] = 1
        
        
        #processing of person title
        k = 1        
        title = ''
        while lX[3][k] != ' ':
            title += lX[3][k]
            k +=1
        if title == 'Mr.':
            X[i,7] = 0
        elif title  == 'Miss.':
            X[i,7] = 1
        elif title  == 'Mrs.':
            X[i,7] = 2
        elif title  == 'Master.':
            X[i,7] = 3
        else:
            X[i,7] = 4
            
       
        
        
        del lX[0]               # delete the PassengerID
        
        del lX[1:3]             # delete name and surname, not useful
        del lX[3]               # delete sibsp
        del lX[3]               # delete parch
        del lX[3]               # delete ticket
        del lX[4]               # delete cabin

        
        for k in range(5):
            X[i,k] = lX[k]
        
        
        ##setting the age to the average value when unknown and when age is asked
        if 2 in listFeatures:
            X = nanToAvg(X,2) # nanToAvg is in toolbox module
        
        if 3 in listFeatures:
            X = nanToAvg(X,3)

        
    #X = preprocessing.scale(X)
    return X[:,listFeatures]
    # 0 : PClass
    # 1 : Sex
    # 2 : age
    # 3 : fare
    # 4 : cabin
    # 5 : port
    # 6 : isAlone
    # 7 : title