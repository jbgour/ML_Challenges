# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 16:26:42 2019

@author: JBG
"""

from numpy import *
import pandas as pd
from sklearn import preprocessing  

import matplotlib.pyplot as plt


def preprocessingTrain(pathFile):
    #pathFile is the path of the dataset
    #returns X and Y, after deleting useless attributes
    
    # Load data
    csv_file_object = pd.read_csv(pathFile, delimiter=',') # Load in the csv file
    XX=array(csv_file_object.values)  # Create a variable to hold the data, type array
    
    n= XX.shape[0]

    y = zeros((n-1,1))
    x = zeros((n-1,4))
    for i in range(2,n-3):
        y[i,0] = XX[i+3,5]
        x[i,0] = XX[i,5]
        x[i,1] = XX[i-1,5]
        x[i,2] = XX[i,6]
        x[i,3] = XX[i-1,6]
    
    return x, y

    
