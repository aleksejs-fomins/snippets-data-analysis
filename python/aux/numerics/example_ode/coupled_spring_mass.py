import numpy as np

# Compute right hand side of a system of masses coupled by springs
# TODO: What is a valid model for non-small oscillations?
def csm_rhs(x, v, m, w, L):
    xmin = 0
    xmax = np.sum(L)
    
    # Compute deformation of each spring
    # Note that springs on both edges are coupled to walls
    delta_L = -L
    delta_L[0]    += x[0] - xmin
    delta_L[-1]   += xmax - x[-1]
    delta_L[1:-1] += x[1:] - x[:-1]

    # Compute acceleration of each mass due to two forces acting on it
    F = np.multiply(w**2, delta_L)
    #F = np.multiply(F, 1 + 0.1 * np.divide(L, delta_L + L))
    dv = np.divide(F[1:] - F[:-1], m)
    
    return np.hstack((v, dv))
