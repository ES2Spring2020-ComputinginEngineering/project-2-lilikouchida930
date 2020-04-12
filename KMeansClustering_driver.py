#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions


#MAIN SCRIPT

glucose, hemoglobin, classification = kmc.openckdfile()
glucoseNorm, hemoglobinNorm, classNorm = kmc.normalizeData(glucose, hemoglobin, classification)
initialClusterArray_x, initialClusterArray_y = kmc.initializeClusters(2)
distances = kmc.findDistance(hemoglobinNorm, initialClusterArray_x, initialClusterArray_y)
nearestCentroid = kmc.findNearestCentroid(distances)
updatedArray_x = kmc.np.zeros(2)
updatedArray_y = kmc.np.zeros(2)
updatedArray_x,updatedArray_y = kmc.updateCentroids(2, nearestCentroid)
updatedArray_x, updatedArray_y = kmc.untilNoChange(2, updatedArray_x, updatedArray_y,initialClusterArray_x, initialClusterArray_y)
distancesFinal = kmc.findDistanceFinal(hemoglobinNorm, updatedArray_x, updatedArray_y)
nearestCentroidFinal = kmc.findNearestCentroidFinal()
corr_lab_CKD, corr_lab_nonCKD = kmc.calculatePercentages()
kmc.graphingKMeans(glucoseNorm, hemoglobinNorm, classNorm, updatedArray_x, updatedArray_y)


