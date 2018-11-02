from scipy import integrate
import numpy as np


# List of all distances from vertex p to vertices in vList
def distList(vList, p):
    return [np.linalg.norm(np.array(v) - np.array(p)) for v in vList]


def function1D_L2(f1, f2, xl, xr):
    return np.sqrt(integrate.quad(lambda x: (f1(x) - f2(x)) ** 2, xl, xr)[0])