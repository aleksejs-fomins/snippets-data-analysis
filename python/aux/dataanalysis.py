import numpy as np

## Construct 1D uniform histogram given number of bins
def data2uniformhist1D(data, nbin):
    ndata = len(data)
    dMin = min(data)
    dMax = max(data)
    dMax += 0.0000001 * dMax

    delta = float(dMax - dMin) / nbin

    rezx = [dMin + delta * (0.5 + i) for i in range(0, nbin)]
    rezy = [0] * nbin

    for it in data:
        rezy[int((it - dMin) / delta)] += 1

    nrm = 1.0 / ndata / delta
    rezy = [ity * nrm for ity in rezy]

    return rezx, rezy


# Construct 1D non-uniform histogram given number of points per bin
def data2nonuniformhist1D(data, nDataPerBin):
    nrm = nDataPerBin / float(len(data))
    dataSorted = sorted(data)

    rezx = []
    rezy = []
    tmpWindow = []
    for it in dataSorted:
        tmpWindow.append(it)
        if len(tmpWindow) == nDataPerBin:
            width = tmpWindow[nDataPerBin-1] - tmpWindow[0]
            rezx.append(np.average(tmpWindow))
            rezy.append(nrm / width)
            tmpWindow = []

    # Process remainder, even if it is a little smaller than the rest of the bins
    if len(tmpWindow) > 0:
        width = tmpWindow[len(tmpWindow)-1] - tmpWindow[0]
        rezx.append(np.average(tmpWindow))
        rezy.append(nrm / width)

    return rezx, rezy


## Construct cumulative distribution function (CDF) for 1D data
def cdf1d(data):
    ndata = len(data)
    dataSorted = sorted(data)

    norm = 1.0 / ndata
    rezx = []
    rezy = [norm * (i / 2) for i in range(1, ndata * 2 + 1)]

    for it in dataSorted:
        rezx.append(it)
        rezx.append(it)

    return rezx, rezy

