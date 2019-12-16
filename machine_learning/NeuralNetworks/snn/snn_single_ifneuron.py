# This simple test checks how a single leaky integrate-and-fire
# neuron responds to a periodic input current

import numpy as np
import matplotlib.pyplot as plt
from snn import ifneuron

PARAM_DISCR_T0 = 0.0
PARAM_DISCR_DT = 0.01
PARAM_DISCR_NT = 10000

PARAM_MEMBR_R = 40.0
PARAM_MEMBR_C = 1.0
PARAM_MEMBR_V0 = 5.0
PARAM_MEMBR_VT = 11.0
PARAM_MEMBR_VE = 0.0

PARAM_AX_DELAY = 1.0
PARAM_AX_TAU_M = 1.5
PARAM_AX_TAU_N = 1.0

PARAM_INPUT_CURRENT = 2.0
PARAM_INPUT_FREQ = 0.25

# INIT NEURON
Ifn1 = ifneuron.IFNeuron(
    PARAM_MEMBR_R,
    PARAM_MEMBR_C,
    PARAM_MEMBR_V0,
    PARAM_MEMBR_V0,
    PARAM_MEMBR_VT,
    PARAM_MEMBR_VE,
    PARAM_DISCR_T0,
    PARAM_DISCR_DT,
    PARAM_AX_DELAY,
    PARAM_AX_TAU_M,
    PARAM_AX_TAU_N)

# DEFINE FIXED INPUT CURRENT FUNCTION
def f(t, A, w):
    return A * (np.sin(w * t) + 1.0)

# INIT TIMES, INPUT CURRENT, MEMBRANE POTENTIAL and POST-SYNAPTIC CURRENT
ts = [Ifn1.T]
fs = [f(Ifn1.T, PARAM_INPUT_CURRENT, PARAM_INPUT_FREQ)]
vs_neu = [Ifn1.V]
vs_post = [0.0]

# TIME-PROPAGATION: EXPLICIT 1st ORDER FDTD
for i in range(0, PARAM_DISCR_NT):
    Ifn1.step(fs[i])
    ts.append(Ifn1.T)
    fs.append(f(Ifn1.T, PARAM_INPUT_CURRENT, PARAM_INPUT_FREQ))
    vs_neu.append(Ifn1.V)
    vs_post.append(Ifn1.post_synaptic_I())

# PLOT RESULTS
plt.figure(1)
ax1 = plt.subplot(311)
ax1.set_ylabel("Input Current")
ax1.set_xticks([])
plt.plot(ts, fs)

ax2 = plt.subplot(312)
ax2.set_ylabel("Membrane Potential")
ax2.set_xticks([])
plt.plot(ts, vs_neu)

ax3 = plt.subplot(313)
ax3.set_xlabel("Time")
ax3.set_ylabel("Post-Synaptic Current")

plt.plot(ts, vs_post)
plt.show()