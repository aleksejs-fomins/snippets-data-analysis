from scipy import integrate
import numpy as np


# List of all distances from vertex p to vertices in vList
def dist_l2_mat_vec(vList, p):
    return [np.linalg.norm(np.array(v) - np.array(p)) for v in vList]


def dist_l2_func_1D(f1, f2, xl, xr):
    return np.sqrt(integrate.quad(lambda x: (f1(x) - f2(x)) ** 2, xl, xr)[0])