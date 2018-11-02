import numpy as np

    

# Bin multidimensional data
# Data assumed to be a 2D array [idx, dim]
# Return: for each non-zero bin: integer coordinates, number of points inside
def binData(data, nBox, border=0.0001):
    nData = len(data)
    xMin = np.min(data, axis = 0) - border
    xMax = np.max(data, axis = 0) + border
    dx = (xMax - xMin) / nBox
    
    pointDict = dict()
    for x in data:
        if type(x) == np.ndarray:
            key = tuple(np.divide(x-xMin, dx).astype(int))
        else:
            key = int((x-xMin) / dx)
        
        if key in pointDict:
            pointDict[key] += 1
        else:
            pointDict[key] = 1
    
    return pointDict.keys(), pointDict.values()


# Evaluate empirical CDF at point x. Data must be sorted
def empCDF(data1Dsorted, x):
    return np.searchsorted(data1Dsorted, x) / len(data1Dsorted)


# Evaluate inverse empirical CDF at probability p. Data must be sorted
def invCDF_1D(data1Dsorted, p):
    nData = len(data1Dsorted)
    if type(p) == np.ndarray:
        dataIdxs = (p * nData).astype(int)
        dataIdxs[dataIdxs > nData-1] = nData-1
    else:
        dataIdxs = min(int(p * nData), nData-1)
    return data1Dsorted[dataIdxs]


# Construct empirical CDF of data and sample nPoint datapoints from it
# Returns 1D array [idxPoint]
def resampleCDF_1D(sortedData, nPoint):
    return invCDF_1D(sortedData, np.random.uniform(0, 1, nPoint))

# Sample nPoint points uniform-randomly from a set. Points may repeat
# Returns 1D array [idxPoint]
def resampleBootstrap(data, nPoint):
    return data[np.random.randint(0, data.shape[0], nPoint)]

    