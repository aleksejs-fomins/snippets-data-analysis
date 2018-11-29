import numpy as np


def kuramoto_rhs(x, w, k, nu=0):
    cosx = np.cos(x)
    sinx = np.sin(x)
    
    rcosf = np.mean(cosx)
    rsinf = np.mean(sinx)
    
    dx = w + np.multiply(k, rsinf*cosx - rcosf*sinx)
    if nu != 0:
        dx += np.random.normal(0, nu, dv.shape[0])
    
    return dx

