#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:27:59 2020

@author: lilikouchida
"""

#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random

#************************************************************************************************
#FUNCTIONS
#***********************************************************************************************

def openckdfile():
#NAME: openckdfile
#INPUTS: n/a
#FUNCTION: opens sample data set
#OUTPUTS: glucose, hemoglobin and classification (single-row arrays)
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

#........... 
    
def normalizeData(glucose, hemoglobin, classification):
#NAME: normalizeData
#INPUTS: glucose, hemoglobin, classification (single-row arrays)
#FUNCTION: normalizes sample data set on a unitless scale from 0-1
#OUTPUTS: glucose_normalized, hemoglobin_normalized and class_normalized (arrays)
    glucose_normalized = (glucose-np.amin(glucose))/(np.amax(glucose)-np.amin(glucose))
    hemoglobin_normalized = (hemoglobin-np.amin(hemoglobin))/(np.amax(hemoglobin)-np.amin(hemoglobin))
    class_normalized = (classification-np.amin(classification))/(np.amax(classification)-np.amin(classification))
    return glucose_normalized, hemoglobin_normalized, class_normalized

#...........
 
def initializeClusters(k):
#NAME: initializeClusters
#INPUTS: k desired initial clusters
#FUNCTION: generates k random data points from the sample data set
#OUTPUTS: initial_clusters_arr (array w/ dimensions 2xk)
    initial_clusters_arr = np.zeros((2,k))
    for j in range(k):
        index = random.randint(0, 157)
        initial_clusters_arr[0,j] = hemoglobin_normalized[index] #top row is hemoglobin
        initial_clusters_arr[1,j] = glucose_normalized[index] #bottom row is glucose
    return initial_clusters_arr

#...........
 
def findDistance(k, hemoglobin_normalized, glucose_normalized, initial_clusters_arr):
#NAME: findDistance
#INPUTS: k, hemoglobin_normalized,glucose_normalized, inital_clusters_arr
#FUNCTION: calculates the distance between each data point in the sample set and each initial cluster
#OUTPUTS: distances_arr (array w/ dimensions 158xk)
    distances_arr = np.zeros((len(hemoglobin_normalized), k))
    for j in range(k):
        for i in range(len(hemoglobin_normalized)):
           x0 = hemoglobin_normalized[i] 
           y0 = glucose_normalized[i]
           x = initial_clusters_arr[0,j] 
           y = initial_clusters_arr[1,j]
           z = np.sqrt(((x-x0)**2)+((y-y0)**2)) 
           distances_arr[i][j] = z
    return distances_arr 

#...........

def findNearestCentroid(distances_arr):
#NAME: findNearestCentroid
#INPUTS: distances_arr
#FUNCTION: finds which cluster each sample data point is closest to
#OUTPUTS: nearest_centroid (array of length 158)
    nearest_centroid = np.zeros((len(hemoglobin_normalized)))
    for i in range(np.shape(distances_arr)[0]):
        minDistance = np.argmin(distances_arr[i,:])
        nearest_centroid[i] = minDistance
    return nearest_centroid

 
#...........

def updateCentroids(k, nearest_centroid):
#NAME: updateCentroids
#INPUTS: k,nearest_centroid
#FUNCTION: updates clusters to be the mean values of hemoglobin and glucose values associated with each cluster
#OUTPUTS:updated_arr (array w/ same dimensions as initial_clusters_arr)
    updated_arr = np.zeros((2,k))
    for i in range(k):
        avg_glucose = np.mean(glucose_normalized[nearest_centroid==i])       
        avg_hemoglobin = np.mean(hemoglobin_normalized[nearest_centroid==i])
        updated_arr[0,i] = avg_hemoglobin
        updated_arr[1,i] = avg_glucose
        print ("updating centroids")
    return updated_arr


         
#...........

def untilNoChange(k, updated_arr, initial_clusters_arr):
#NAME: untilNoChange
#INPUTS: k, updated_arr, initial_clusters_arr
#FUNCTION: updates clusters and calcuates nearest centroids repetitively until end condition is met
#OUTPUTS: updated_arr, initial_clusters_arr 
    while True: 
        print ("in progress")
        if abs(np.min(initial_clusters_arr - updated_arr)) < 0.00001:
           print("done")
           return updated_arr, initial_clusters_arr
        else:
            print("still working")
            initial_clusters_arr = updated_arr
            distances_arr = findDistance(k, hemoglobin_normalized, glucose_normalized, initial_clusters_arr)
            nearest_centroid = findNearestCentroid(distances_arr)
            updated_arr = updateCentroids(k, nearest_centroid)


 #...........
 

def numberCorrect(nearest_centroid, class_normalized):
#NAME: numberCorrect
#INPUTS: nearest_centroid, class_normalized
#FUNCTION: counds the number of correctly labelled CKD patients and correctly labeled nonCKD patients
#OUTPUTS:
    corr_lab_CKD = 0
    corr_lab_nonCKD = 0
    for i in range(len(nearest_centroid)):
        if nearest_centroid[i]==1 and class_normalized[i]==1:
            corr_lab_CKD = corr_lab_CKD+1
        elif nearest_centroid[i]==0 and class_normalized[i]==0:
            corr_lab_nonCKD = corr_lab_nonCKD+1
    return corr_lab_CKD, corr_lab_nonCKD
  


 #........... 


def graphingKMeans(glucose_normalized, hemoglobin_normalized, class_normalized, updated_arr):
#NAME: graphingKMeans
#INPUTS: glucose_normalized, hemoglobin_normalized, class_normalized, updated_arr
#FUNCTION: graphs final clusters against sample data set with finalized classifications after update iteration
#OUTPUTS: plot figure
    plt.figure()
    for i in range(int(nearest_centroid.max()+1)):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin_normalized[nearest_centroid==i],glucose_normalized[nearest_centroid==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(updated_arr[0,i], updated_arr[1,i], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()


            
#   
  
#..........
glucose, hemoglobin, classification = openckdfile()
glucose_normalized, hemoglobin_normalized, class_normalized = normalizeData(glucose, hemoglobin, classification)
initial_clusters_arr = initializeClusters(2)
distances_arr = findDistance(2, hemoglobin_normalized, glucose_normalized, initial_clusters_arr)
nearest_centroid = findNearestCentroid(distances_arr)
updated_arr = updateCentroids(2, nearest_centroid)
updated_arr, initial_clusters_arr = untilNoChange(2, updated_arr, initial_clusters_arr)
#final_distances_arr = findDistanceFinal(2, hemoglobin_normalized, updated_arr)
#final_nearest_centroid = findNearestCentroidFinal(2, final_distances_arr)
corr_lab_CKD, corr_lab_nonCKD = numberCorrect(nearest_centroid, class_normalized)
graphingKMeans(glucose_normalized, hemoglobin_normalized, class_normalized, updated_arr)
 
