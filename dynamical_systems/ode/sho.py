import numpy as np
import matplotlib.pyplot as plt
import h5py

# Import external libraries
from lib.numerics.integrator_lib import integrate_ode_ord1
from lib.numerics.example_ode.sho import sho_rhs, sho_energy


#####################
# Initialize
#####################

# Define constants for SHO
N_OSC = 10
w = np.random.uniform(5, 20, N_OSC)
x0 = np.random.uniform(-5, 5, N_OSC)
v0 = np.divide(np.random.uniform(-5, 5, N_OSC), w)
dt = 0.01
N_STEPS = 10000


#####################
# Run
#####################

# Define integrator-conforming RHS with inserted constants. Note SHO is time-invariant
rhs = lambda var, t: np.array(sho_rhs(var[:N_OSC], var[N_OSC:], w))

# Integrate the problem
rez = integrate_ode_ord1(rhs, np.hstack((x0, v0)), dt, N_STEPS, method='scipy')

#####################
# Write data to file
#####################

outfilename = "data/sho_" + str(N_OSC) + ".h5"
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

## Plot energy (use only with 1 oscillator, otherwise can't see anything)
#energies = np.array([sho_energy(var[:N_OSC], var[N_OSC:], w) for var in rez])
#KE = energies[:, 0]
#PE = energies[:, 1]

#plt.figure()
#plt.plot(KE, label='Kinetic')
#plt.plot(PE, label='Potential')
#plt.plot(KE+PE, label='Total')
#plt.legend()
#plt.show()


# # Plot movie
# plt.ion()
# fig, ax = plt.subplots()
# plots = [ax.plot(x, 0, 'o')[0] for x in rez[0][:N_OSC]]
# ax.set_xlim([np.min(rez[:, :N_OSC]), np.max(rez[:, :N_OSC])])
# plt.show()
#
# for iStep in range(1, N_STEPS):
#     try:
#         for iOsc in range(N_OSC):
#             plots[iOsc].set_xdata(rez[iStep][iOsc])
#         fig.canvas.draw()
#         fig.canvas.flush_events()
#
#     except KeyboardInterrupt:
#         print("Aborted by user!")
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
