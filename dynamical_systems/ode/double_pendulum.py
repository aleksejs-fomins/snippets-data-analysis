import numpy as np
import matplotlib.pyplot as plt
import h5py

# Import external libraries
from lib.numerics.integrator_lib import integrate_ode_ord1
from lib.numerics.example_ode.double_pendulum import dp_rhs, dp_energy


#####################
# Initialize
#####################

# Define system parameters
m1 = 0.1 # kg
m2 = 0.1 # kg
l1 = 0.1 # m
l2 = 0.1 # m
g = 9.8  # N/kg


# Define simulation parameters
dt = 0.01
N_STEPS = 1000

# Define initial conditions
#var0 = np.array([np.pi/2, np.pi/2, 0, 0])
#var0 = np.array([np.pi, np.pi, 0, 0])
var0 = np.radians([120, -10, 0, 0])

#####################
# Run
#####################

# Define integrator-conforming RHS with inserted constants. Note that Kuramoto is time-invariant
rhs = lambda var, t: np.array(dp_rhs(var, m1,m2,l1,l2,g))

# Run simulation
periodic = [2 * np.pi, 2 * np.pi, None, None]  # Angles are periodic, velocities are not
rez = integrate_ode_ord1(rhs, var0, dt, N_STEPS, method='scipy', periodic=periodic)

# Postprocess
rez[:, 0] = rez[:, 0] - np.pi/2
rez[:, 1] = rez[:, 1] - np.pi/2

x1 = l1*np.cos(rez[:, 0])
y1 = l1*np.sin(rez[:, 0])
x2 = x1+l2*np.cos(rez[:, 1])
y2 = y1+l2*np.sin(rez[:, 1])


# #####################
# # Write data to file
# #####################
#
# outfilename = "data/dp.h5"
# h5f = h5py.File(outfilename, "w")
# h5f['dt'] = dt
# h5f['m1'] = m1
# h5f['m2'] = m2
# h5f['l1'] = l1
# h5f['l2'] = l2
# h5f['x1'] = x1
# h5f['x2'] = x2
# h5f['y1'] = y1
# h5f['y2'] = y2
# h5f['w1'] = rez[:, 2]
# h5f['w2'] = rez[:, 3]
# h5f.close()


#####################
# Plot
#####################

## Plot velocity
fig,ax = plt.subplots(ncols=5)
ax[0].plot(rez[:, 0], rez[:, 1])
ax[1].plot(np.sin(rez[:, 0]), np.sin(rez[:, 1]))
ax[2].plot(rez[:, 2], rez[:, 3])
ax[3].plot(rez[:-1, 2], rez[1:, 3])
ax[4].plot(rez[:-1, 3], rez[1:, 2])
ax[0].set_title("Phase space for angles")
ax[1].set_title("Phase space for x-coordinates")
ax[2].set_title("Lagged 0->1 Phase space for x-coordinates")
ax[3].set_title("Lagged 1->0 Phase space for x-coordinates")
plt.legend()
plt.show()

#############################################
# Sanity check - plot total energy over time
#############################################
# KE1,KE2,PE1,PE2 = dp_energy(rez, m1, m2, l1, l2, g)
#
#
# plt.figure()
# #plt.plot(KE1)
# #plt.plot(KE2)
# #plt.plot(PE1)
# #plt.plot(PE2)
# plt.plot(KE1+KE2, label="Kinetic")
# plt.plot(PE1+PE2, label="Potential")
# plt.plot(KE1+KE2+PE1+PE2, label="Total")
# plt.legend()
# plt.show()

#############################################
# Plot movie
#############################################
# plt.ion()
# fig, ax = plt.subplots(tight_layout=True, figsize=(7,7))
# ball0, = ax.plot(x1[0], y1[0], 'o')
# ball1, = ax.plot(x2[0], y2[0], 'o')
# radlim = 1.1 * (l1+l2)
# plt.xlim(-radlim, radlim)
# plt.ylim(-radlim, radlim)
# plt.show()
#
# for i in range(1, N_STEPS):
#     try:
#         ball0.set_xdata(x1[i])
#         ball0.set_ydata(y1[i])
#         ball1.set_xdata(x2[i])
#         ball1.set_ydata(y2[i])
#         fig.canvas.draw()
#         fig.canvas.flush_events()
#
#     except KeyboardInterrupt:
#         print("Aborted by user!")
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
