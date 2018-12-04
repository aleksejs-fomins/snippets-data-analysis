import os
import math
import numpy as np
from operator import xor
from jidt_wrapper import readFloatsFile
from jidt_wrapper.JidtWrapper import JidtWrapper, np2JArr

# Create a TE wrapper class
jidtWrapper1 = JidtWrapper()

print('#############################################')
print('# Example 1: TE for Two-Partite Binary Data')
print('#############################################')

# Generate some random binary data.
sourceArray = np.random.randint(0, 2, 100)
sourceArray2 = np.random.randint(0, 2, 100)
destArray = np.hstack(([0], sourceArray[0:99]))

# Create a TE calculator and run it:
param = {'historyLength' : 2, 'kernelWidth' : 1}
print("For copied source, result should be close to 1 bit : %.4f" % jidtWrapper1.calcTwoPartiteTE_Discrete(sourceArray, destArray, param))
print("For random source, result should be close to 0 bits: %.4f" % jidtWrapper1.calcTwoPartiteTE_Discrete(sourceArray2, destArray, param))

print('#############################################')
print('# Example 2: TE for Multidimensional Two-Partite Binary Data')
print('#############################################')
# However here we want 2 rows by 100 columns where the next time step (row 2) is to copy the
# value of the column on the left from the previous time step (row 1):
# TODO: WTF are we actually calculating in this case?? Isnt the source just a 2d variable?
nData = 100
rowData = np.zeros((2, nData), dtype=int)
rowData[0] = np.random.randint(0, 2, nData)
rowData[1] = np.hstack((rowData[0, nData-1], rowData[0, 0:nData-1]))  # Copy the previous row, offset one column to the right

# Add observations of transfer across one cell to the right per time step:
param = {'historyLength' : 2, 'kernelWidth' : 1}
result2D = jidtWrapper1.calcTwoPartiteTE_Discrete(rowData, 1, param)
nObserv = jidtWrapper1.javaClass.getNumObservations()
print(('The result should be close to 1 bit here, since we are executing copy ' + \
      'operations of what is effectively a random bit to each cell here: %.3f ' + \
      'bits from %d observations') % (result2D, nObserv))


print('#############################################')
print('# Example 3: TE for Continuous Data Kernel')
print('#############################################')

# Generate some random normalised data.
numObservations = 1000
covariance = 0.4

# Make two uncorrelated normal-distributed sources
sourceArray  = np.random.uniform(0, 1, numObservations)
sourceArray2 = np.random.uniform(0, 1, numObservations)

# Destination array of random normals with partial correlation to previous value of sourceArray
destArray = np.zeros(numObservations)
destArray[1:] += covariance * sourceArray[:-1]
destArray[1:] += (1 - covariance) * np.random.uniform(0, 1, numObservations-1)

# Normalise the individual variables
# Use history length 1 (Schreiber k=1), kernel width of 0.5 normalised units
param = {'method': 'TE_KERNEL', 'initParam': [1, 0.5], 'properties': {"NORMALISE" : "true"}}
result1 = jidtWrapper1.runJavaTwoPartite((sourceArray, destArray), param)
result2 = jidtWrapper1.runJavaTwoPartite((sourceArray2, destArray), param)
# For copied source, should give something close to 1 bit:
# Expected correlation is expected covariance / product of expected standard deviations:
#  (where square of destArray standard dev is sum of squares of std devs of
#  underlying distributions)
corr_expected = covariance / (1 * np.sqrt(covariance**2 + (1-covariance)**2))
rez_expected = -0.5*np.log(1-np.power(corr_expected, 2)) / np.log(2)
print("TE result %.4f bits; expected to be close to %.4f bits for these correlated Gaussians but biased upwards" % (result1, rez_expected))
print("TE result %.4f bits; expected to be close to 0 bits for uncorrelated Gaussians but will be biased upwards" % result2)

print('#############################################')
print('# Example 4: TE for Continuous Data Kraskov')
print('#############################################')
# TODO: Check correct, result consistently more than original separate example

# Generate some random normalised data.
numObservations = 1000
covariance = 0.4

# Make two uncorrelated normal-distributed sources
sourceArray  = np.random.uniform(0, 1, numObservations)
sourceArray2 = np.random.uniform(0, 1, numObservations)

# Destination array of random normals with partial correlation to previous value of sourceArray
destArray = np.zeros(numObservations)
destArray[1:] += covariance * sourceArray[:-1]
destArray[1:] += (1 - covariance) * np.random.uniform(0, 1, numObservations-1)

# Create a TE calculator and run it:
# Use Kraskov parameter K=4 for 4 nearest points
param = {'method': 'TE_KRASKOV', 'initParam': [1], 'properties': {"NORMALISE": "true", "k": "4"}}
result1 = jidtWrapper1.runJavaTwoPartite((sourceArray, destArray), param)   # Perform calculation with correlated source
result2 = jidtWrapper1.runJavaTwoPartite((sourceArray2, destArray), param)  # Perform calculation with uncorrelated source:

# Note that the calculation is a random variable (because the generated
#  data is a set of random variables) - the result will be of the order
#  of what we expect, but not exactly equal to it; in fact, there will
#  be a large variance around it.
# Expected correlation is expected covariance / product of expected standard deviations:
#  (where square of destArray standard dev is sum of squares of std devs of
#  underlying distributions)
corr_expected = covariance / (1 * np.sqrt(covariance**2 + (1-covariance)**2))
rez_expected = -0.5*np.log(1-np.power(corr_expected, 2))
print("TE result %.4f nats; expected to be close to %.4f nats for these correlated Gaussians" % (result1, rez_expected))
print("TE result %.4f nats; expected to be close to 0 nats for these uncorrelated Gaussians" % result2)



print('#############################################')
print('# Example 5: TE Binary Multivariate Transfer')
print('#############################################')

# Generate some random binary data.
numRows = 2
numObservations = 100
sourceArray1 = np.random.randint(0, 2, numRows*numObservations).reshape((numObservations, numRows))
sourceArray2 = np.random.randint(0, 2, numRows*numObservations).reshape((numObservations, numRows))

# Destination variable takes a copy of the first bit of the source in bit 1,
#  and an XOR of the two bits of the source in bit 2:
destArray = np.zeros((numObservations, numRows), dtype=int)
destArray[1:, 0] = sourceArray1[:-1, 0]
destArray[1:, 1] = xor(sourceArray1[:-1, 0], sourceArray1[:-1, 1])

# We need to construct the joint values of the dest and source before we pass them in,
#  and need to use the matrix conversion routine when calling from Matlab/Octave:
sourceArray1Combined = jidtWrapper1.computeCombinedValues(sourceArray1)
sourceArray2Combined = jidtWrapper1.computeCombinedValues(sourceArray2)
destArrayCombined    = jidtWrapper1.computeCombinedValues(destArray)

param = {'historyLength' : 4, 'kernelWidth' : 1}
result1 = jidtWrapper1.calcTwoPartiteTE_Discrete(sourceArray1Combined, destArrayCombined, param)
result2 = jidtWrapper1.calcTwoPartiteTE_Discrete(sourceArray2Combined, destArrayCombined, param)

print('For source which the 2 bits are determined from, result should be close to 2 bits : %.3f' % result1)
print('For random source, result should be close to 0 bits in theory: %.3f' % result2)
print('The result for random source is inflated towards 0.3 due to finite observation length (%d).'
      'One can verify that the answer is consistent with that from a random source by checking:'
      'teCalc.computeSignificance(1000); ans.pValue\n' % numObservations)


print('#############################################')
print('# Example 6: Dynamic Calling Mutual Info')
print('#############################################')

datafile = os.path.join(os.getcwd(), 'jidt_wrapper/data/4ColsPairedNoisyDependence-1.txt')
data = np.array(readFloatsFile.readFloatsFile(datafile))

paramUniVar = {'method': 'MI_MV_KRASKOV', 'initParam': [1, 1], 'properties': {}, 'NO_CONV_JARRAY' : True}
paramJoint  = {'method': 'MI_MV_KRASKOV', 'initParam': [2, 2], 'properties': {}, 'NO_CONV_JARRAY' : True}
miUniVar = jidtWrapper1.runJavaTwoPartite((data[:, 0], data[:, 2]), paramUniVar)
miJoint  = jidtWrapper1.runJavaTwoPartite((data[:, [0, 1]], data[:, [2, 3]]), paramJoint)

print("Mutual entropy of two univariate variables = ", miUniVar)
print("Mutual entropy of two joint 2D variables = ", miJoint)



# print('#############################################')
# print('# Example 7: Ensemble Method TE Continuous Data')
# print('#############################################')
#
# # Generate some random normalised data.
# numObservations = 1000
# covariance = 0.4
# numTrials = 10
# kHistoryLength = 1
#
#
# param = {'method': 'TE_KRASKOV', 'initParam': [kHistoryLength], 'properties': {"k": "4"}, 'CONTINUOUS_DATA' : True}
# teCalc = TEClass.runJavaTwoPartite((), param)
#
# for trial in range(0, numTrials):
#     # Create a new trial, with destArray correlated to previous value of sourceArray:
#     sourceArray = np.random.normal(0, 2, numObservations)
#     destArray = np.zeros(numObservations)
#     destArray[1:] += covariance * sourceArray[:-1]
#     destArray[1:] += (1 - covariance) * np.random.uniform(0, 1, numObservations - 1)
#
#     # Add observations for this trial:
#     print("Adding samples from trial %d ..." % trial)
#     teCalc.addObservations(np2JArr(sourceArray), np2JArr(destArray))
#
# # We've finished adding trials:
# print("Finished adding trials")
# teCalc.finaliseAddObservations()
#
# # Compute the result:
# print("Computing TE ...")
# result = teCalc.computeAverageLocalOfObservations()
# # Note that the calculation is a random variable (because the generated
# #  data is a set of random variables) - the result will be of the order
# #  of what we expect, but not exactly equal to it; in fact, there will
# #  be some variance around it (smaller than example 4 since we have more samples).
# print("TE result %.4f nats; expected to be close to %.4f nats for these correlated Gaussians " % \
#       (result, math.log(1.0 / (1 - math.pow(covariance, 2)))))
#
# # And here's how to pull the local TEs out corresponding to each input time
# # series under the ensemble method (i.e. for multiple trials).
# localTEs = teCalc.computeLocalOfPreviousObservations()
# localValuesPerTrial = teCalc.getSeparateNumObservations()  # Need to convert to int for indices later
# startIndex = 0
# for localValuesInThisTrial in localValuesPerTrial:
#     endIndex = startIndex + localValuesInThisTrial - 1
#     print("Local TEs for trial %d go from array index %d to %d" % (trial, startIndex, endIndex))
#     print("  corresponding to time points %d:%d (indexed from 0) of that trial" % (kHistoryLength, numObservations - 1))
#     # Access the local TEs for this trial as:
#     localTEForThisTrial = localTEs[startIndex:endIndex]
#     # Now update the startIndex before we go to the next trial
#     startIndex = endIndex + 1
# # And make a sanity check that we've looked at all of the local values here:
# print("We've looked at %d local values in total, matching the number of samples we have (%d)" % (
# startIndex, teCalc.getNumObservations()))


print('#############################################')
print('# Example 7: Ensemble Method TE Continuous Data')
print('#############################################')



