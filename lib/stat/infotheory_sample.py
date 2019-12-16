import numpy as np
from lib.stat.binning import bin_multivariate_uniform, bin_multivariate_adaptive, extent_to_volume
from lib.stat.infotheory_discrete import discrete_entropy_1D, discrete_KL_1D

# Compute empirical entropy of a sample frequency vector
def sample_discrete_entropy_1D(sample, base=np.exp(1)):
    return discrete_entropy_1D(sample / np.sum(sample), base)

def sample_discrete_KL_1D(s1, s2, base=np.exp(1)):
    return discrete_KL_1D(s1 / np.sum(s1), s2 / np.sum(s2), base)

# Compute relative phase space area taken by the multidimensional data
# Data assumed to be a 2D array [idx, dim]
# Bin data using nBox boxes per dimension
def sample_rel_area_phase_space(data, nBox):
    #nDim = data.shape[1] if data.ndim == 2 else 1
    binCounts = bin_multivariate_uniform(data, nBox)[1]
    return binCounts.shape[0] / data.shape[0]  #/ nBox**nDim

# Compute sample entropy for real data[idx, dim]
# Bin data using nBox boxes per dimension
def sample_entropy_uniform_binning(data, nBox):
    binCounts = bin_multivariate_uniform(data, nBox)[1]
    return sample_discrete_entropy_1D(binCounts)


def sample_entropy_adaptive_binning(data, minPointPerBin):
    nPointLst, extLst = bin_multivariate_adaptive(data, minPointPerBin)
    volLst = extent_to_volume(extLst)
    return -sample_discrete_KL_1D(np.array(nPointLst), np.array(volLst))