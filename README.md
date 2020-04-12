This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

ES 2
Liliko Uchida
Project 2
Due April 13

****************************************************************************************
NearestNeighborClassification.py
****************************************************************************************

- includes all functions and mainscript for nearest neighbor classification method. 

FUNCTIONS:

1) openckdfile -->opens sample data set. Returns arrays of hemoglobin, glucose and classifications

2) def normalizeData --> normalizes sample data set. Takes in sample data sets. Returns arrays of normalized hemoglobin, glucose, and classification values

3) createTestCase --> generates random test case. Returns two single element arrays, one corresponding to glucose value and one corresponding to hemoglobin value, creating a randomized test case. 

4) calculateDistanceArray --> creates an array of distances between each sample data point and new test case. Takes normalized glucose and hemoglobin arrays, and new glucose and hemoglobin values from test case. Returns a distance array with the distances of each sample data point from new test case.

5) nearestNeighborClassifier --> classifies the test case as the class which is associated with its nearest data point. takes normalized glucose and hemoglobin arrays and new glucose and hemoglobin values of randomized test case. Returns nearest_class variable.

6) graphData --> graphs sample data. Takes normalized glucose, hemoglobin, and classification arrays

7) graphTestCase --> graphs test case among sample data. Takes normalized hemoglobin and glucose arrays and new hemoglobin and glucose values for randomized test case along with normalized classifications array.

8) kNearestNeighborClassifier --> classifies new test case as the mean classification associated with its k nearest neighbors. Takes a desired value k, new hemoglobin and glucose values for randomized test case, and normalized hemoglobin and glucose arrays. Returns classMajority variable.


TO RUN:
Change red integer value (k value) to desired k value in ln 114. run. 
In variable explorer, classMajority displays result of k-nearest neighbor.
nearest_class displays result of nearest neighbor. 


****************************************************************************************
kMeansClustering_functions.py
****************************************************************************************

- include functions for k-means clustering classification method

FUNCTIONS:

1) openckdfile --> see previous

2) normalizeData --> see previous

3) initializeClusters --> initializes k amount of starting clusters. Takes desired integer k.returns k starting clusters in the form of array pairs. 

4) findDistance --> finds distance between each sample data point and each initial cluster. Takes normalized hemoglobin array, and initial cluster arrays. Returns distance arrays with distances from each sample data point to each k-th cluster. 

5) findNearestCentroid --> assigns each sample data point to the nth cluster to which it is nearest to. Takes distances array. returns array with number of k-th cluster to which each sample data point is closest to. 

6) updateCentroids -->  Updates centroid values with mean values of previous data points associated with each k-th cluster. takes desired k integer value and nearestCentroid array. Returns two updated arrays, one corresponding to hemoglobin and one corresponding to glucose average values.

7) untilNoChange --> repeats the update and reinitialize cluster process until an end condition is met. Takes desired integer k, updated arrays, and initial cluster arrays. Returns updated arrays once end condition is met. 

8) findDistanceFinal --> once end condition is met, calculates the distance between each sample data point and each finalized cluster. Returns a nearestCentroidFinal array.

9) calculatePercentage --> counts the number of correctly labeled CKD and nonCKD patients and returns these values as variables. 

10) graphingKMeans --> graphs clusters and sample data sets. Takes in normalized glucose and hemoglobin arrays, normalized classifications, and updated arrays. 


****************************************************************************************
kMeansClustering_driver.py
****************************************************************************************

- includes mainscript for k-means clustering classification method

TO RUN:

Change red integer values in lns 9, 12, 13, 14, 15 to desired values of k. Input k = 2 for part about correctly/incorrectly labeled CKD/nonCKD patients. 