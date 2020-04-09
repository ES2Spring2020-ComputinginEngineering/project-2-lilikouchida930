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

def initializeClusters(k):
#This function will randomly select k coordinate pairs (x=hemoglobinNorm, y=glucoseNorm)
#to act as the initial clusters. These randomly selected x and y values will be added
#to to arrays called initialClusterArray_x and initialClusterArray_y. 
    initialClusterArray_x = np.zeros(k)
    initialClusterArray_y = np.zeros(k)
    for i in range(0, k):
        index = random.randint(0, 157)
        x0 = hemoglobinNorm[index]
        y0 = glucoseNorm[index]
        initialClusterArray_x[i] = x0
        initialClusterArray_y[i] = y0
    return initialClusterArray_x, initialClusterArray_y

#...........

def findDistance(hemoglobinNorm, initialClusterArray_x, initialClusterArray_y):
    distances = np.zeros((len(hemoglobinNorm), len(initialClusterArray_x)))
    for i in range(len(hemoglobinNorm)):
        for j in range(len(initialClusterArray_x)):
            x0 = hemoglobinNorm[i]
            y0 = glucoseNorm[i]
            x = initialClusterArray_x[j]
            y = initialClusterArray_y[j]
            z = np.sqrt(((x-x0)**2)+((y-y0)**2))
            distances[i][j] = z
    return distances

#...........

def findNearestCentroid():
#This function goes through each row in the distance array and finds the column in
#which the minimum value in that row occurs. This index is added to a new array
#called nearestCentroid. 
    nearestCentroid = np.zeros((len(hemoglobinNorm)))
    m = 0
    while m < len(distances):
        for row in distances:
            minDistance = np.argmin(row)
            nearestCentroid[m] = minDistance
            m = m+1 
        return nearestCentroid

#...........

def updateCentroids(k):
    updatedArray_x = np.zeros(k)
    updatedArray_y = np.zeros(k)
    for i in range(k):
        meanGlucose = np.mean(glucoseNorm[nearestCentroid==i])       
        meanHemoglobin = np.mean(hemoglobinNorm[nearestCentroid==i])
        updatedArray_x[i] = meanHemoglobin
        updatedArray_y[i] = meanGlucose
#    print(initialClusterArray_x, initialClusterArray_y)
    return updatedArray_x, updatedArray_y
        
#...........
    
def untilNoChange(k, initialClusterArray_x, initialClusterArray_y):
    while True:
        # need to have 4 total arrays
        distances = findDistance(hemoglobinNorm, initialClusterArray_x, initialClusterArray_y)
        nearestCentroid = findNearestCentroid()
#        print(initialClusterArray_x, initialClusterArray_y)
        updatedArray_x, updatedArray_y = updateCentroids(k)
#        print(updatedArray_x, updatedArray_y)
        # have 2 old and 2 new
        if np.array_equal(initialClusterArray_x,updatedArray_x) and np.array_equal(initialClusterArray_y,updatedArray_y):
            return updatedArray_x, updatedArray_y
        initialClusterArray_x = updatedArray_x
        initialClusterArray_y = updatedArray_y
#    estimatedClass(k)
#    estimatedClasses = estimatedClass(k)
#     
#    
#...........

            
def estimatedClass(k):  
    estimatedClasses = np.zeros(len(hemoglobinNorm))
    for i in range(len(hemoglobinNorm)): 
        for j in range(k):
            nearestCentroid = findNearestCentroid()
            estimatedClasses[i] = classNorm[k]
    return estimatedClasses
               
#
#     
 
#...........
 
#MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucoseNorm, hemoglobinNorm, classNorm = normalizeData(glucose, hemoglobin, classification)   
initialClusterArray_x, initialClusterArray_y = initializeClusters(2)
distances = findDistance(hemoglobinNorm, initialClusterArray_x, initialClusterArray_y)
nearestCentroid = findNearestCentroid()
updatedArray_x, updatedArray_y = updateCentroids(2)
        
untilNoChange(2, initialClusterArray_x, initialClusterArray_y)
