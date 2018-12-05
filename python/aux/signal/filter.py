import numpy as np
from scipy.interpolate import interp1d

# Compute the approximate convolution with decaying exponential,
# given time-discretization and decay constant
def approxDecayConv(data, TAU, DT):
    if TAU == 0:
        return data
    else:
        nPoint = len(data)
        alpha = DT / TAU
        beta = 1 - alpha
        rez = np.zeros(nPoint+1)
        for i in range(nPoint):
            rez[i+1] = rez[i] * beta + data[i]

        return rez[1:] * alpha
    

# Compute the approximate low-pass-filter of discretized data,
#  given time-discretization and decay constant
# Same as approxDecayConv, but corrects for lag by shifting result
#  back in time by TAU/DT/2
def approxLPF(data, TAU, DT):
    if TAU == 0:
        return data
    else:
        nPoint = len(data)
        alpha = DT / TAU
        beta = 1 - alpha
        shiftCorr = int(1/alpha/2)
        rez = np.zeros(nPoint+1+shiftCorr)
        
        # Compute convolution for all points where data is available
        for i in range(nPoint):
            rez[i+1] = rez[i] * beta + data[i]
            
        # Extend convolution for a few points into the future by repeating the last point
        for i in range(nPoint, nPoint+shiftCorr):
            rez[i+1] = rez[i] * beta + data[nPoint-1]

        return rez[1+shiftCorr:] * alpha
    

# Smoothen data by averaging points over a window
def windowAvg1D(data, windowSize):
    ndata = len(data)
    gap = windowSize // 2
    rez = np.zeros(ndata + 1)
    tmp = np.zeros(ndata + 2*gap)
    tmp[:gap] = 2*data[0] - data[:gap][::-1]
    tmp[-gap:] = 2*data[-1] - data[-gap:][::-1]
    tmp[gap:-gap] = data
    
    for i in range(ndata + 1):
        rez[i] = np.average(tmp[i:i+windowSize])
        
    # Problem: resulting array is 1 point longer than source. Need to reinterpolate
    xold = np.linspace(0, 1, len(data)+1)
    xnew = np.linspace(0, 1, len(data))
    f2 = interp1d(xold, rez, kind='cubic')
    return f2(xnew)