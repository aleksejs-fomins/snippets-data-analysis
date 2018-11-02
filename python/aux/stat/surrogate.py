#import random
import numpy as np
import aux.stat.moments as moments
import aux.stat.empirical as empirical

# Resample data using bootstrap method, assuming that all dimensions are independent
def resampleBootstrapByDim(data):
    rez = np.zeros(data.shape)
    for iDim in range(data.shape[1]):
        rez[:, iDim] = empirical.resampleBootstrap(data[:, iDim], data.shape[0])
    return rez


# Construct surrogates for data[idx, dim] under assumption of statistical independence for different discretizations
# Compute an integral estimator for the data (e.g. sample entropy), and return its mean and variance over multiple trials
# Result is a 2d array [surrIdx, numBinIdx]
def independentVariableEstimate(data, nBoxLst, nTrial, estimator, method):
    nPoint = data.shape[0]
    nDim = data.shape[1]
    nDiscrPoint = len(nBoxLst)
    rez = np.zeros((nTrial, nDiscrPoint))
    
    # Compute 1D entropies by resampling, add them up
    if method == "semi-analytic":
        for iSample in range(nTrial):
            dataSurr = resampleBootstrapByDim(data)
            for iDim in range(nDim):
                rez[iSample] += estimator(dataSurr[:, iDim], nBoxLst)
                
    # Shuffle N-1 dimension data, compute full ND binned entropy
    elif method == "shuffle":
        dataShuffle = np.copy(data)
        
        for iSample in range(nTrial):
            # Shuffle data of all dimensions except last to save computational time
            # Anyway, last data will be random with respect to all other data
            for iDim in range(nDim - 1):
                #random.shuffle(dataShuffle[:, iDim])
                np.random.shuffle(dataShuffle[:, iDim])
            
            # Compute relative areas and entropies for this shuffle
            rez[iSample] = estimator(dataShuffle, nBoxLst)
    
    # Resample each dimension independently, then compute entropy
    elif method == "resample":
        for iSample in range(nTrial):
            dataSurr = resampleBootstrapByDim(data)
            rez[iSample] = estimator(dataSurr, nBoxLst)

    else:
        raise ValueError("method", method, "is not known")
        
    return moments.sample_mean_and_std(rez, axis=0)