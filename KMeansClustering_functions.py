#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random


#FUNCTIONS

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

#...........
    
def normalizeData(glucose, hemoglobin, classification):
#Normalizes each of the three data sets to a unitless scale of 0 to 1. 
    glucoseNorm = (glucose-np.amin(glucose))/(np.amax(glucose)-np.amin(glucose))
    hemoglobinNorm = (hemoglobin-np.amin(hemoglobin))/(np.amax(hemoglobin)-np.amin(hemoglobin))
    classNorm = (classification-np.amin(classification))/(np.amax(classification)-np.amin(classification))
    return glucoseNorm, hemoglobinNorm, classNorm

#...........

#MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucoseNorm, hemoglobinNorm, classNorm = normalizeData(glucose, hemoglobin, classification)   