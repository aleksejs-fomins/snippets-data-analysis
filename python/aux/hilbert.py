from scipy import integrate
import numpy as np


def function1D_L2(f1, f2, xl, xr):
    return np.sqrt(integrate.quad(lambda x: (f1(x) - f2(x)) ** 2, xl, xr)[0])