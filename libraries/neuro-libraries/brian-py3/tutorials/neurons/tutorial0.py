from brian2 import *
start_scope()

tau = 10*ms
eqs = '''
dv/dt = (1-v)/tau : 1
'''

G = NeuronGroup(1, eqs, method='exact')
M = StateMonitor(G, 'v', record=True)
print('Before v = %s' % G.v[0])
run(100*ms)
print('After v = %s' % G.v[0])
print('Expected value of v = %s' % (1-exp(-100*ms/tau)))

plot(M.t/ms, M.v[0])
plot(M.t/ms, 1-exp(-M.t/tau), 'C1--',label='Analytic')
xlabel('Time (ms)')
ylabel('v')
legend()
show()