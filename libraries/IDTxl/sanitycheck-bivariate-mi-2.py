# Import classes
import numpy as np
from idtxl.bivariate_mi import BivariateMI
from idtxl.data import Data
from idtxl.visualise_graph import plot_network
import matplotlib.pyplot as plt

#############################
#  Experiment 1 - X does not depend on its own past
#############################

# # a) Generate test data
# nSamples = 1000
# nTrials = 5
# dataShape = (nTrials, nSamples)
# src = np.random.uniform(0, 1, dataShape)
# x = src + 0.1 * np.random.normal(0, 1, dataShape)
# y = 1 - 2*src + 0.1 * np.random.normal(0, 1, dataShape)
# x = x[:, :-1]
# y = y[:, 1:]
# dataIDTxl = Data(np.array([x, y]), dim_order='prs')
#
# # Plot data self-prediction and neighbor-prediction
# fig, ax = plt.subplots(ncols=2)
# ax[0].set_title('Predicting X from its own past')
# ax[1].set_title('Predicting X from past of Y')
# ax[0].plot(x[:, :-1], x[:, 1:], '.')
# ax[1].plot(y[:, :-1], x[:, 1:], '.')
# plt.show()
#
#
# # b) Initialise analysis object and define settings
# network_analysis = BivariateMI()
# settings = {'cmi_estimator': 'JidtGaussianCMI',
#             'max_lag_sources': 1,
#             'min_lag_sources': 1}
#
# # c) Run analysis
# results = network_analysis.analyse_network(settings=settings, data=dataIDTxl)
#
# # d) Plot inferred network to console and via matplotlib
# results.print_edge_list(weights='max_te_lag', fdr=False)
# plot_network(results=results, weights='max_te_lag', fdr=False)
# plt.show()


#############################
#  Experiment 1 - X does depend on its own past
#############################

# # a) Generate test data
# nSamples = 1000
# nTrials = 5
# dataShape = (nTrials, nSamples)
# src = np.outer(np.ones(nTrials), np.linspace(0, 1, nSamples))
# x = src + 0.1 * np.random.normal(0, 1, dataShape)
# y = 1 - 2*src + 0.1 * np.random.normal(0, 1, dataShape)
# x = x[:, :-1]
# y = y[:, 1:]
# dataIDTxl = Data(np.array([x, y]), dim_order='prs')
#
# # Plot data self-prediction and neighbor-prediction
# fig, ax = plt.subplots(ncols=2)
# ax[0].set_title('Predicting X from its own past')
# ax[1].set_title('Predicting X from past of Y')
# ax[0].plot(x[:, :-1], x[:, 1:], '.')
# ax[1].plot(y[:, :-1], x[:, 1:], '.')
# plt.show()
#
#
# # b) Initialise analysis object and define settings
# network_analysis = BivariateMI()
# settings = {'cmi_estimator': 'JidtGaussianCMI',
#             'max_lag_sources': 1,
#             'min_lag_sources': 1}
#
# # c) Run analysis
# results = network_analysis.analyse_network(settings=settings, data=dataIDTxl)
#
# # d) Plot inferred network to console and via matplotlib
# results.print_edge_list(weights='max_te_lag', fdr=False)
# plot_network(results=results, weights='max_te_lag', fdr=False)
# plt.show()

