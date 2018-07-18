from brian2 import *
import tutorials.synapses.vis_con as vis
start_scope()

N = 10
G = NeuronGroup(N, 'v:1')

S = Synapses(G, G)
S.connect(condition='abs(i-j)<4 and i!=j')
vis.visualise_connectivity(S)