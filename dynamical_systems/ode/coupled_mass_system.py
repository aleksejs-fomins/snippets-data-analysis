import numpy as np
import matplotlib.pyplot as plt
import h5py

# Import external libraries
from lib.numerics.integrator_lib import integrate_ode_ord1
from lib.numerics.example_ode.coupled_spring_mass import csm_rhs


#####################
# Initialize
#####################

# Define system parameters
N_OSC = 10
m = 0.1 * np.ones(N_OSC)    # kg
L = 0.1 * np.ones(N_OSC+1)  # m
w = 15 * np.ones(N_OSC+1)  # N/kg

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
rhs = lambda var, t: np.array(csm_rhs(var[:N_OSC], var[N_OSC:], m, w, L))

# Run simulation
rez = integrate_ode_ord1(rhs, np.hstack((x0, v0)), dt, N_STEPS, method='scipy')


#####################
# Write data to file
#####################

outfilename = "data/cms_" + str(N_OSC) + ".h5"
h5f = h5py.File(outfilename, "w")
h5f['dt'] = dt
h5f['w'] = w
h5f['x'] = rez[:N_OSC]
h5f['v'] = rez[N_OSC:]
h5f.close()


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



