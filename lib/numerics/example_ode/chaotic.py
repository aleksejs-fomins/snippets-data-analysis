import numpy as np

def rhs_lorenz2d(x, y):
    return [x - y - x**3, x - x**2 * y]

def rhs_example1_2d(x, y):
    return [y, (1 - x**2 - y**2)*y - x]

def rhs_example2_2d(x, y):
    return [y, (1 - x**2)*y - x]

def rhs_duffing_2D(x, v, t, w, a, b, c, d):
    return [v, c*np.cos(w*t) - d*v - a*x - b*x**3]