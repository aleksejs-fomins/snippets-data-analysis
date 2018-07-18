from brian2 import *
start_scope()

tau = 10*ms
eqs = '''
dv/dt = (1-v)/tau : 1 (unless refractory)
'''

G = NeuronGroup(1, eqs, threshold='v>0.8', reset='v = 0', refractory=5*ms, method='exact')

M = StateMonitor(G, 'v', record=0)
spikemon = SpikeMonitor(G)
run(50*ms)
print('Spike times: %s' % spikemon.t[:])
plot(M.t/ms, M.v[0])
for t in spikemon.t:
    axvline(t/ms, ls='--', c='C1', lw=3)

xlabel('Time (ms)')
ylabel('v')
show()



