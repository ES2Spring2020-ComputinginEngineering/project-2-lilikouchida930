#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random


#*******************************************************

# FUNCTIONS
def openckdfile():
#Creates arrays in the variable explorer with values of attributes.
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

#......

def normalizeData(glucose, hemoglobin, classification):
#Normalizes each of the three data sets to a unitless scale of 0 to 1. 
    glucoseNorm = (glucose-np.amin(glucose))/(np.amax(glucose)-np.amin(glucose))
    hemoglobinNorm = (hemoglobin-np.amin(hemoglobin))/(np.amax(hemoglobin)-np.amin(hemoglobin))
    classNorm = (classification-np.amin(classification))/(np.amax(classification)-np.amin(classification))
    return glucoseNorm, hemoglobinNorm, classNorm

#......

def createTestCase():
#Randomly generates a float value in the range of the max and mins of each 
#attribute. 
    glucoseMin = np.amin(glucose)
    glucoseMax = np.amax(glucose)
    hemoglobinMin = np.amin(hemoglobin)
    hemoglobinMax = np.amax(hemoglobin)
    newGlucose = random.uniform(glucoseMin, glucoseMax)
    newHemoglobin = random.uniform(hemoglobinMin, hemoglobinMax)
    newGluNorm = (newGlucose-np.amin(glucose))/(np.amax(glucose)-np.amin(glucose))
    newHemoNorm = (newHemoglobin-np.amin(hemoglobin))/(np.amax(hemoglobin)-np.amin(hemoglobin))
    return newGluNorm, newHemoNorm

#......

def calculateDistanceArray(newGluNorm, newHemoNorm, glucoseNorm, hemoglobinNorm):
    zArray = np.zeros(158)
    x = newHemoNorm
    y = newGluNorm
    for i in range(len(hemoglobinNorm)):
        x0 = hemoglobinNorm[i]
        y0 = glucoseNorm[i]
        z = np.sqrt(((x-x0)**2)+((y-y0)**2))
        zArray[i] = z
    return zArray

#...... 

def nearestNeighborClassifier(newGluNorm, newHemoNorm, glucoseNorm, hemoglobinNorm, classNorm):
    min_index = np.argmin(zArray)
    nearest_class = classNorm[min_index]
    return nearest_class

#...... 

def graphData(glucoseNorm, hemoglobinNorm, classNorm):
    plt.figure()
    plt.plot(hemoglobinNorm[classification==1],glucoseNorm[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobinNorm[classification==0],glucoseNorm[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.title("Hemoglobin vs. Glucose Normalized")
    plt.show()
    
#...... 

def graphTestCase(newGluNorm, newHemoNorm, glucoseNorm, hemoglobinNorm, classNorm):
    plt.figure()
    plt.plot(hemoglobinNorm[classification==1],glucoseNorm[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobinNorm[classification==0],glucoseNorm[classification==0], "r.", label = "Class 0")
    plt.scatter(newHemoNorm, newGluNorm, s=100)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.title("Hemoglobin vs. Glucose Normalized w/ Test Case")
    plt.show() 

#...... 

def kNearestNeighborClassifier(k, newGluNorm, newHemoNorm,glucoseNorm, hemoglobinNorm, classNorm):
    sorted_indices = np.argsort(zArray)
    k_indices = sorted_indices[:k]
    k_classifications = classNorm[k_indices]
    classSum = 0
    for i in k_classifications:
        classSum = classSum + i
        classMajority = classSum/k
    return k_classifications, classMajority
        
    
    
    



#*******************************************************

# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucoseNorm, hemoglobinNorm, classNorm = normalizeData(glucose, hemoglobin, classification)
graphData(glucoseNorm, hemoglobinNorm, classNorm)
newGluNorm, newHemoNorm = createTestCase()
zArray = calculateDistanceArray(newGluNorm, newHemoNorm, glucoseNorm, hemoglobinNorm)
nearest_class = nearestNeighborClassifier(newGluNorm, newHemoNorm, glucoseNorm, hemoglobinNorm, classNorm)
graphTestCase(newGluNorm, newHemoNorm, glucoseNorm, hemoglobinNorm, classNorm)
k_classifications, classMajority = kNearestNeighborClassifier(10, newGluNorm, newHemoNorm,glucoseNorm, hemoglobinNorm, classNorm)
print();        

plt.figure()
plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()
