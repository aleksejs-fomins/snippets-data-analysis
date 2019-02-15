import numpy as np

# Right Hand Side of the 1st order forced 2D ode
def forced_2D_rhs(x, m, f, t, nu = 0):
    return m.dot(x) + f(t)
