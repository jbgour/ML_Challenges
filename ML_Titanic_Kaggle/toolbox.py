# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 23:04:55 2018

@author: JBG
"""

#just a module to transform nan values by the average of the column

import numpy as np

def nanToAvg(mat,columnNumber):
    col = mat[:,columnNumber]
    p = col.shape[0]
    l = []
    for k in range(p):
        if np.isnan(col[k]) == False :
            l.append(col[k])
    avg = np.mean(l)
    for k in range(p):
        if np.isnan(col[k]):
            col[k] = avg
    mat[:,columnNumber] = col        
    return mat

