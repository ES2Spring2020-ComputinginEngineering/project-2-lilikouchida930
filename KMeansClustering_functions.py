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

def initializeClusters(k):
#This function will randomly select k coordinate pairs (x=hemoglobinNorm, y=glucoseNorm)
#to act as the initial clusters. These randomly selected x and y values will be added
#to to arrays called initialClusterArray_x and initialClusterArray_y. 
    initialClusterArray_x = np.zeros(k+1)
    initialClusterArray_y = np.zeros(k+1)
    for i in range(0, k):
        index = random.randint(0, 158)
        x0 = hemoglobinNorm[index]
        y0 = glucoseNorm[index]
        initialClusterArray_x[i] = x0
        initialClusterArray_y[i] = y0
    return initialClusterArray_x, initialClusterArray_y

def findNearestCluster():
    zArray = np.zeros(158)
    for i in range (len(initialClusterArray_x)-1):
        x = initialClusterArray[i]
        y = initialClusterArray[i]
        
    

#...........

#MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucoseNorm, hemoglobinNorm, classNorm = normalizeData(glucose, hemoglobin, classification)   
initialClusterArray_x, initialClusterArray_y = initializeClusters(2)