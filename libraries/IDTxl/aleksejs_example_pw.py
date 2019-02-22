# import standard libraries
import numpy as np
import copy as cp
import matplotlib.pyplot as plt
from matplotlib import colors

# IDTxl libraries
from idtxl.bivariate_mi import BivariateMI
from idtxl.bivariate_te import BivariateTE
from idtxl.multivariate_te import MultivariateTE
from idtxl.data import Data
from idtxl.visualise_graph import plot_network

#######################
# Generate Data
#######################

N_NODE = 5
N_DATA = 10000  # 4000
LAG_MIN = 1
LAG_MAX = 4

# Generate data that is cycled backwards for every new node
# Thus the node with highest index should appear to have the "earliest" version of the same data
np.random.seed(0)
data = np.zeros((N_NODE, N_DATA))
data[0] = np.random.normal(0, 1, N_DATA)
for i in range(1, N_NODE):
    data[i] = np.hstack((data[i-1][1:], data[i-1][0]))

# Have to add some noise to data or IDTxl will blow up :D
data += np.random.normal(0, 0.1, N_NODE*N_DATA).reshape((N_NODE, N_DATA))

#######################
# Run IDTxl
#######################
# a) Convert data to ITDxl format
dataIDTxl = Data(data, dim_order='ps')

# b) Initialise analysis object and define settings
N_METHOD = 3
title_lst = [
    # "BivariateMI for shift-based data",
    # "BivariateTE for shift-based data",
    "MultivariateTE for shift-based data"]
# method_lst = ['BivariateMI', 'BivariateTE', 'MultivariateTE']
method_lst = ['MultivariateTE']
# network_analysis_lst = [BivariateMI(), BivariateTE(), MultivariateTE()]
network_analysis_lst = [MultivariateTE()]

settings = {'cmi_estimator': 'JidtGaussianCMI',
            'max_lag_sources': LAG_MAX,
            'min_lag_sources': LAG_MIN}

# c) Run analysis
results_lst = [net_analysis.analyse_network(settings=settings, data=dataIDTxl) for net_analysis in network_analysis_lst]

#######################
# Convert results to matrices and plot them
#######################

fig, ax = plt.subplots(nrows=N_METHOD, ncols=3)
normTE = colors.Normalize(vmin=0, vmax=1)
normLag = colors.Normalize(vmin=0, vmax=LAG_MAX)
normP = colors.Normalize(vmin=0, vmax=0.1)

for i, results, method in zip(list(range(N_METHOD)), results_lst, method_lst):
    if 'TE' in method:
        metric_name = 'selected_sources_te'
    elif 'MI' in method:
        metric_name = 'selected_sources_mi'
    else:
        raise ValueError('Unexpected method', method)

    # Fill initial matrices with NAN so that the cells with no connections appear empty
    te_mat = np.zeros((N_NODE, N_NODE)) + np.nan
    lag_mat = np.zeros((N_NODE, N_NODE)) + np.nan
    p_mat = np.zeros((N_NODE, N_NODE)) + np.nan

    for iTrg in range(N_NODE):
        rezThis = results.get_single_target(iTrg, fdr=False)

        # If any connections were found, get their data  at all was found
        if rezThis[metric_name] is not None:
            rezThisZip = zip(
                rezThis[metric_name],
                rezThis['selected_sources_pval'],
                [val[1] for val in rezThis['selected_vars_sources']],
                [val[0] for val in rezThis['selected_vars_sources']]
            )

            for te, p, lag, iSrc in rezThisZip:
                te_mat[iSrc][iTrg] = te
                lag_mat[iSrc][iTrg] = lag
                p_mat[iSrc][iTrg] = p

    plTE  = ax[i][0].imshow(te_mat, cmap='jet')
    plLag = ax[i][1].imshow(lag_mat, cmap='jet')
    plP   = ax[i][2].imshow(p_mat, cmap='jet')

    ax[i][0].set_title(method)
    ax[i][1].set_title("Lags")
    ax[i][2].set_title("p-value")

    fig.colorbar(plTE, ax=ax[i][0])
    fig.colorbar(plLag, ax=ax[i][1])
    fig.colorbar(plP, ax=ax[i][2])

    plTE.set_norm(normTE)
    plLag.set_norm(normLag)
    plP.set_norm(normP)


plt.show()


#######################
# Normalize mTE values within target (to handle unequal bias)
#######################

res_mte = cp.copy(results_lst[method_lst.index('MultivariateTE')])  # so we don't break something by accident
mte_values = np.zeros((N_NODE, N_NODE)) + np.nan

for t in res_mte.targets_analysed:

    te = res_mte.get_single_target(target=t, fdr=False)['te']
    sel_source = res_mte.get_single_target(target=t, fdr=False)['selected_vars_sources']
    print('sel. sources - target {}'.format(t))
    print(sel_source)
    if te is None:
        continue

    te /= max(res_mte.get_single_target(target=t, fdr=False)['te'])
    sources = np.array([s[0] for s in sel_source])
    mte_values[t, sources] = te

fig, ax = plt.subplots(ncols=2, figsize=(10, 4))
a = ax[0].imshow(te_mat, cmap='jet')
plt.colorbar(a, ax=ax[0], fraction=0.046)
ax[0].set_title('normalisation over targets')
a = ax[1].imshow(np.fliplr(np.flipud(mte_values)), cmap='Blues')
plt.colorbar(a, ax=ax[1], fraction=0.046)
ax[1].set_title('normalisation within targets')
plt.show()
