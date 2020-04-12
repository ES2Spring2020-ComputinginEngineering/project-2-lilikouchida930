#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random


#FUNCTIONS

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

glucose, hemoglobin, classification = openckdfile()
#...........
    
def normalizeData(glucose, hemoglobin, classification):
#Normalizes each of the three data sets to a unitless scale of 0 to 1. 
    glucoseNorm = (glucose-np.amin(glucose))/(np.amax(glucose)-np.amin(glucose))
    hemoglobinNorm = (hemoglobin-np.amin(hemoglobin))/(np.amax(hemoglobin)-np.amin(hemoglobin))
    classNorm = (classification-np.amin(classification))/(np.amax(classification)-np.amin(classification))
    return glucoseNorm, hemoglobinNorm, classNorm

glucoseNorm, hemoglobinNorm, classNorm = normalizeData(glucose, hemoglobin, classification)
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

initialClusterArray_x, initialClusterArray_y = initializeClusters(2)
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

distances = findDistance(hemoglobinNorm, initialClusterArray_x, initialClusterArray_y)

#...........

def findNearestCentroid():
#This function goes through each row in the distance array and finds the column in distances
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

nearestCentroid = findNearestCentroid()
 
#...........

def updateCentroids(k):
    updatedArray_x = np.zeros(k)
    updatedArray_y = np.zeros(k)
    for i in range(k):
        meanGlucose = np.mean(glucoseNorm[nearestCentroid==i])       
        meanHemoglobin = np.mean(hemoglobinNorm[nearestCentroid==i])
        updatedArray_x[i] = meanHemoglobin
        updatedArray_y[i] = meanGlucose
    return updatedArray_x, updatedArray_y

updatedArray_x, updatedArray_y = updateCentroids(2)

        
#...........

def untilNoChange(k, updatedArray_x, updatedArray_y,initialClusterArray_x, initialClusterArray_y):
    updatedArray_x, updatedArray_y = updateCentroids(k)
    i = 0
    while i < 100:
        if np.array_equal(initialClusterArray_x,updatedArray_x) and np.array_equal(initialClusterArray_y,updatedArray_y):
            print("done")
            return updatedArray_x, updatedArray_y
        else:
            print("still working")
            initialClusterArray_x = updatedArray_x
            initialClusterArray_y = updatedArray_y
            updatedArray_x, updatedArray_y = updateCentroids(k)
            i = i + 1
        
updatedArray_x, updatedArray_y =untilNoChange(2, updatedArray_x, updatedArray_y,initialClusterArray_x, initialClusterArray_y)
#...........
            
def findDistanceFinal(hemoglobinNorm, updatedArray_x, updatedArray_y):
    distancesFinal = np.zeros((len(hemoglobinNorm), len(updatedArray_x)))
    for i in range(len(hemoglobinNorm)):
        for j in range(len(updatedArray_x)):
            x0 = hemoglobinNorm[i]
            y0 = glucoseNorm[i]
            x = updatedArray_x[j]
            y = updatedArray_y[j]
            z = np.sqrt(((x-x0)**2)+((y-y0)**2))
            distancesFinal[i][j] = z
    return distancesFinal

distancesFinal = findDistanceFinal(hemoglobinNorm, updatedArray_x, updatedArray_y)

#...........

def findNearestCentroidFinal():
    nearestCentroidFinal = np.zeros((len(hemoglobinNorm)))
    m = 0
    distancesFinal = findDistanceFinal(hemoglobinNorm, updatedArray_x, updatedArray_y)
    while m < len(distancesFinal):
        for row in distancesFinal:
            minDistanceFinal = np.argmin(row)
            nearestCentroidFinal[m] = minDistanceFinal
            m = m+1 
        return nearestCentroidFinal

nearestCentroidFinal = findNearestCentroidFinal()
    


def estimatedClass(k): 
#In correspondence to the last part of the project, estimateClass(k) assigns each 
#pre-existing data point to the classification which its nearest centroid has. 
    estimatedClasses = np.zeros(len(hemoglobinNorm))
    nearestCentroidFinal = findNearestCentroidFinal()
    for i in range(len(nearestCentroidFinal )): 
        for j in range(k):
            estimatedClasses[i] = classNorm[j]
    return estimatedClasses

estimatedClasses = estimatedClass(2)
   
 
#...........
 
#MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucoseNorm, hemoglobinNorm, classNorm = normalizeData(glucose, hemoglobin, classification)   
initialClusterArray_x, initialClusterArray_y = initializeClusters(4)
distances = findDistance(hemoglobinNorm, initialClusterArray_x, initialClusterArray_y)
nearestCentroid = findNearestCentroid()
updatedArray_x, updatedArray_y = updateCentroids(4)
        
updatedArray_x, updatedArray_y, nearestCentroid = untilNoChange(4, updatedArray_x, updatedArray_y, initialClusterArray_x, initialClusterArray_y)
estimatedClasses = estimatedClass(4)