#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions


#MAIN SCRIPT
glucose, hemoglobin, classification = kmc.openckdfile()
glucoseNorm, hemoglobinNorm, classNorm = kmc.normalizeData(glucose, hemoglobin, classification)   
initialClusterArray_x, initialClusterArray_y = kmc.initializeClusters(2)
distances = kmc.findDistance(hemoglobinNorm, initialClusterArray_x, initialClusterArray_y)
nearestCentroid = kmc.findNearestCentroid()
updatedArray_x, updatedArray_y = kmc.updateCentroids(2)
        
updatedArray_x, updatedArray_y, nearestCentroid = kmc.untilNoChange(2, updatedArray_x, updatedArray_y, initialClusterArray_x, initialClusterArray_y)
estimatedClasses = kmc.estimatedClass(2)