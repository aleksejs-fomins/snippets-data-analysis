##############################
# Statistical moments
##############################
import numpy as np

def sample_mean(data, axis=0):
    return np.average(data, axis=axis)

# Calculate sample mean and variance
# Note: np.var() not used because it is biased
def sample_mean_and_var(data, axis=0):
    N = len(data)
    mu = np.sum(data, axis=axis) / N
    #s2 = np.sum((data - mu)**2, axis=axis) / (N - 1)
    s2 = np.sum(np.array([(np.take(data, i, axis=axis) - mu)**2 for i in range(N)]), axis=0)/(N-1)
    return mu, s2

# Compute sample standard deviation given sample variance
# Does 1st order bias correction
def sample_var2std(s2, N):
    return np.sqrt(s2 * (N-1) / (N-1.5))

# Wrapper
def sample_mean_and_std(data, axis=0):
    mu, s2 = sample_mean_and_var(data, axis=axis)
    return mu, sample_var2std(s2, data.shape[axis])

