import numpy as np

# Multilinear generic forced 1st order ODE system
def multilin_forced_rhs(x, M, f, t, nu = 0):
    return M.dot(x) + f(t)

