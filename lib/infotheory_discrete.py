import numpy as np

def log_any_base(x, base=np.exp(1)):
    return np.log(x) / np.log(base)

# Compute entropy of a discrete probability distribution
def discrete_entropy_1D(p, base=np.exp(1)):
    pNonZero = p[p > 0]  # Summands with p=0 evaluate to 0 by definition
    logP = log_any_base(pNonZero, base)
    return -np.dot(pNonZero, logP)

# Compute KL-divergence of a discrete probability distribution
def discrete_KL_1D(p, q, base=np.exp(1)):
    pZeroIdx = p == 0
    qZeroIdx = q == 0
    if np.any(qZeroIdx & ~pZeroIdx):
        return np.inf  # KL-divergence is infinite if q is zero but p is not zero in at least 1 bin
    else:
        pNonZero = p[~pZeroIdx]
        qNonZero = q[~pZeroIdx]  # Same shape as p
        logP = log_any_base(pNonZero, base)
        logQ = log_any_base(qNonZero, base)
        return np.dot(pNonZero, logP - logQ)