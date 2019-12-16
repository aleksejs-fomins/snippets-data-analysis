import numpy as np


def kuramoto_rhs(x, w, k, nu=0):
    N = x.shape[0]
    
    cosx = np.cos(x)
    sinx = np.sin(x)
    kcosx = k.dot(cosx) / N
    ksinx = k.dot(sinx) / N
    
    #rcosf = np.mean(cosx)
    #rsinf = np.mean(sinx)
    #dx = w + k*(rsinf*cosx - rcosf*sinx)
    
    dx = w + np.multiply(cosx, ksinx) - np.multiply(sinx, kcosx)
    
    if nu != 0:
        dx += np.random.normal(0, nu, N)
    
    return dx

