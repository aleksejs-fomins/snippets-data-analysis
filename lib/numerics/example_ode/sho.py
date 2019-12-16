import numpy as np

# Return length if type has length otherwise return 1
def typelen(v):
    return len(v) if hasattr(v, "__len__") else 1


# Right Hand Side of the 1st order simple harmonic oscillator ODE system
def sho_rhs(x, v, w, nu = 0):
    dv = -np.multiply(w**2, x)
    if nu != 0:
        dv += np.random.normal(0, nu, typelen(v))
    return np.hstack((v, dv))


# Analytic solution given initial values for x and v
def sho_true(x0, v0, w, tlst):
    xm = np.sqrt(x0**2 + np.divide(v0, w)**2)
    phi = np.arctan2(np.multiply(x0, w), v0)
    
    vm = np.multiply(xm, w)
    x = np.array([np.multiply(xm, np.sin(w*t + phi)) for t in tlst])
    v = np.array([np.multiply(vm, np.cos(w*t + phi)) for t in tlst])
    return x, v


def sho_energy(x, v, w):
    KE = v**2 / 2
    PE = np.multiply(w, x)**2 / 2
    return KE, PE
