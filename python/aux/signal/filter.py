import numpy as np

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