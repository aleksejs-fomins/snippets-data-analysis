import numpy as np
import lib.stat.moments as moments

# # Construct empirical CDF of data and sample nPoint datapoints from it
# # Returns 1D array [idxPoint]
# def resampleCDF_1D(sortedData, nPoint):
#     return invCDF_1D(sortedData, np.random.uniform(0, 1, nPoint))

# Sample nPoint points uniform-randomly from a set. Points may repeat
# Returns 1D array [idxPoint]
def bootstrap_sample_univariate(data, nPoint):
    newIdxs = np.random.randint(0, data.shape[0], nPoint)
    return data[newIdxs]


# Resample data using bootstrap method, assuming that all dimensions are independent
def bootstrap_sample_multivatiate(data, nPoint, independentDim = True):
    if independentDim:
        nDim = data.shape[1]
        rez = np.zeros((nPoint, nDim))
        for iDim in range(nDim):
            rez[:, iDim] = bootstrap_sample_univariate(data[:, iDim], nPoint)
        return rez
    else:
        return bootstrap_sample_univariate(data, nPoint)


# Construct surrogates for data[idx, dim] under assumption of statistical independence for different discretizations
# Compute an integral estimator for the data (e.g. sample entropy), and return its mean and variance over multiple trials
# Result is a 2d array [surrIdx, numBinIdx]
def resample_independent_vars(data, nTrial, estimator, method):
    nPoint, nDim = data.shape
    #nDiscrPoint = len(nBoxLst)
    rez = np.zeros(nTrial)
    
    # Compute 1D entropies by resampling, add them up
    if method == "semi-analytic":
        for iSample in range(nTrial):
            for iDim in range(nDim):
                dataSurr1D = bootstrap_sample_univariate(data[:, iDim], nPoint)
                rez[iSample] += estimator(dataSurr1D)
                
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
            rez[iSample] = estimator(dataShuffle)
    
    # Resample each dimension independently, then compute entropy
    elif method == "resample":
        for iSample in range(nTrial):
            dataSurr = bootstrap_sample_multivatiate(data, nPoint, independentDim=True)
            rez[iSample] = estimator(dataSurr)

    else:
        raise ValueError("method", method, "is not known")
        
    return moments.sample_mean_and_std(rez, axis=0)
