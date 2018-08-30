from brian2 import *
start_scope()

N = 1000
tau = 10*ms
vr = -70*mV
vt0 = -50*mV
delta_vt0 = 5*mV
tau_t = 100*ms
sigma = 0.5*(vt0-vr)
v_drive = 2*(vt0-vr)
duration = 400*ms

eqs = '''
dv/dt = (v_drive+vr-v)/tau + sigma*xi*tau**-0.5 : volt
dvt/dt = (vt0-vt)/tau_t : volt
'''

reset = '''
v = vr
vt += delta_vt0
'''

G = NeuronGroup(N, eqs, threshold='v>vt', reset=reset, refractory=5*ms, method='euler')
spikemon = SpikeMonitor(G)
M1 = StateMonitor(G, 'v', record=0)
M2 = StateMonitor(G, 'vt', record=0)

G.v = 'rand()*(vt0-vr)+vr'
G.vt = vt0

run(duration)

figure(figsize=(12,4))
subplot(121)
plot(M1.t/ms, M1.v[0])
xlabel('Time (ms)')
ylabel('v')
subplot(122)
plot(M2.t/ms, M2.vt[0])
xlabel('Time (ms)')
ylabel('vt')
show()

_ = hist(spikemon.t/ms, 100, histtype='stepfilled', facecolor='k', weights=ones(len(spikemon))/(N*defaultclock.dt))
xlabel('Time (ms)')
ylabel('Instantaneous firing rate (sp/s)')
show()