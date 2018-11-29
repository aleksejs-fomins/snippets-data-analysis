import numpy as np
import matplotlib.pyplot as plt

# Append base directory
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(__file__))
base_dir = currentdir[:currentdir.index('python')] + 'python/'
sys.path.insert(0,base_dir)
print("Appended base directory", base_dir)

# Import external libraries
from aux.numerics.integrator_lib import integrate_ode_ord1
from aux.numerics.example_ode.coupled_spring_mass import csm_rhs


#####################
# Initialize
#####################

# Define system parameters
N_OSC = 10
m = 0.1 * np.ones(N_OSC)    # kg
L = 0.1 * np.ones(N_OSC+1)  # m
k = 200 * np.ones(N_OSC+1)  # N/kg

# Define simulation parameters
dt = 0.01
N_STEPS = 10000

# Define initial conditions
xmin = 0
xmax = np.sum(L)
v0 = np.random.normal(0, 1, N_OSC)
#v0 = np.zeros(N_OSC)
x0 = np.copy(L[:-1])
for i in range(1, N_OSC):
    x0[i] += x0[i-1]


#####################
# Run
#####################

# Define integrator-conforming RHS with inserted constants. Note that Kuramoto is time-invariant
rhs = lambda var, t: np.array(csm_rhs(var[:N_OSC], var[N_OSC:], m, k, L))

# Run simulation
rez = integrate_ode_ord1(rhs, np.hstack((x0, v0)), dt, N_STEPS, method='scipy')


#####################
# Plot
#####################

## Plot result
#plt.figure()
#plt.plot(rez)
#plt.show()

# Plot movie
plt.ion()
fig, ax = plt.subplots()
plots = [ax.plot(x, 0, 'o')[0] for x in rez[0][:N_OSC]]
ax.set_xlim([xmin, xmax])
plt.show()

for iStep in range(1, N_STEPS):
    try:
        for iOsc in range(N_OSC):
            plots[iOsc].set_xdata(rez[iStep][iOsc])
        fig.canvas.draw()
        fig.canvas.flush_events()

    except KeyboardInterrupt:
        print("Aborted by user!")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)



