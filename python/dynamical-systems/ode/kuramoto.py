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
from aux.numerics.example_ode.kuramoto_oscillator import kuramoto_rhs



'''
  TODO:
   * Convention for parameter selection
   * Convention for initial conditions
'''

#####################
# Initialize
#####################

# Define system parameters
N_OSC = 20
K = 5.0 * np.ones((N_OSC, N_OSC))
W = np.random.uniform(0, 2*np.pi, N_OSC)

# Define simulation parameters
dt = 0.01
N_STEPS = 10000

# Define initial conditions
x0 = np.random.uniform(0, 2*np.pi, N_OSC)


#####################
# Run
#####################

# Define integrator-conforming RHS with inserted constants. Note that Kuramoto is time-invariant
rhs = lambda x, t: np.array(kuramoto_rhs(x, W, K))

# Run simulation
periodic = 2 * np.pi * np.ones(N_OSC)
rez = integrate_ode_ord1(rhs, x0, dt, N_STEPS, method='rk4', periodic=periodic)

# postprocess
xarr = np.cos(rez)
yarr = np.sin(rez)


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
line1, = ax.plot(xarr[0], yarr[0], 'o')
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])
plt.show()

for i in range(1, N_STEPS):
    try:
        line1.set_xdata(xarr[i])
        line1.set_ydata(yarr[i])
        fig.canvas.draw()
        fig.canvas.flush_events()

    except KeyboardInterrupt:
        print("Aborted by user!")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)



