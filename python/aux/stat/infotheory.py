import random
import numpy as np
import aux.stat.empirical as empirical

# Compute logarithm of arbitrary base
def logAnyBase(x, base=np.exp(1)):
    return np.log(x)/np.log(base)
    
    
# Compute empirical entropy of a discrete data sample
def sampleEntropy1D(sample, base=np.exp(1)):
    N = np.sum(sample)
    distrNonZero = sample[sample > 0] / N
    return -np.dot(distrNonZero, logAnyBase(distrNonZero, base=base))
    

# Compute relative phase space area taken by the multidimensional data
# Data assumed to be a 2D array [idx, dim]
# Bin data using nBox boxes per dimension
def relPhaseSpaceArea(data, nBox, border=0.0001):
    dim = data.shape[1]
    binnedDataCounts = np.array(list(empirical.binData(data, nBox, border)[1]))
    return len(binnedDataCounts) / nBox**dim


# Compute sample entropy for real data[idx, dim]
# Bin data using nBox boxes per dimension
def binnedEntropy(data, nBox, border=0.0001):
    binnedDataCounts = np.array(list(empirical.binData(data, nBox, border)[1]))
    return sampleEntropy1D(binnedDataCounts)


# Compute Binned entropy for data[idx, dim] for a list of discretizations nBoxLst
# Return 1D array entropy[numBinIdx]
def binnedEntropyMulti(data, nBoxLst, border=0.0001):
    return np.array([binnedEntropy(data, nBox, border) for nBox in nBoxLst])


# Compute Binned relative phase space area for data[idx, dim] for a list of discretizations nBoxLst
# Return 1D array entropy[numBinIdx]
def binnedRelAreaMulti(data, nBoxLst, border=0.0001):
    return np.array([relPhaseSpaceArea(data, nBox, border) for nBox in nBoxLst])