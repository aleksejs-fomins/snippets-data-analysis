import numpy as np
import bisect


'''
TODO:
  * Implement adaptive binning, where each box tries to have the same number of points inside

'''

def sort_rows_by_col(data, col):
    return data[data[:, col].argsort()]

# Convert list of extents [[xmin, ymin], [xmax, ymax]] to list of volumes. Dimension is arbitrary
def extent_to_volume(extLst):
    return [np.prod(ext[1] - ext[0]) for ext in extLst]


# Bin multidimensional data of shape [val x dim]
# Every dimension is binned into nBins
# The bounding box is given by the minimum and maximum datapoint
# Return: for each non-zero bin: integer coordinates, number of points inside
def bin_multivariate_uniform(data, nBins):
    nData = len(data)
    xMin = np.min(data, axis = 0)
    xMax = np.max(data, axis = 0)
    dx = (xMax - xMin) / nBins

    # Identify integer bin for every point
    idxs = np.floor((data - xMin) / dx).astype(int)

    # By convention the point on the border of the last bin is still in that bin
    idxs[idxs == nData] = nData - 1

    # Find all unique rows and count them. Returns (idxs, counts)
    return np.unique(idxs, axis=0, return_counts=True)

# Bin multidimensional data of shape [val x dim]
# Sequentially sort each dimension, then split points equally along that dimension, continue recursively
# Return list of effective bins after all bins have approximately the expected minimal point count
def bin_multivariate_adaptive(data, minPointPerBin, extent=None, cutDim=0):
    nData, nDim = data.shape
    if extent is None:
        extent = np.array((
            [np.min(data[:, iDim]) for iDim in range(nDim)],
            [np.max(data[:, iDim]) for iDim in range(nDim)]
        ))

    if nData <= minPointPerBin:
        return [nData], [extent]

    cutN = nData // 2
    dataSorted = sort_rows_by_col(data, cutDim)
    dataL = dataSorted[:cutN]
    dataR = dataSorted[cutN:]
    extentL = np.copy(extent)
    extentR = np.copy(extent)
    cutVal = np.mean(dataSorted[cutN-1:cutN+1, cutDim])  # Cut along the middle between the two points
    extentL[1, cutDim] = cutVal
    extentR[0, cutDim] = cutVal

    cutDimNext = (cutDim + 1) % nDim
    nDataLstL, extLstL = bin_multivariate_adaptive(dataL, minPointPerBin, extent=extentL, cutDim=cutDimNext)
    nDataLstR, extLstR = bin_multivariate_adaptive(dataR, minPointPerBin, extent=extentR, cutDim=cutDimNext)
    return nDataLstL + nDataLstR, extLstL + extLstR
