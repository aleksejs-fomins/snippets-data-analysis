from brian2 import *
import tutorials.synapses.vis_con as vis
start_scope()

N = 10
G = NeuronGroup(N, 'v:1')

S = Synapses(G, G)
S.connect(j='k for k in range(i-3, i+4) if i!=k', skip_if_invalid=True)
vis.visualise_connectivity(S)