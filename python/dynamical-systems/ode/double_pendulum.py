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
from aux.numerics.example_ode.double_pendulum import dp_rhs, dp_energy


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
N_STEPS = 10000

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
rez = integrate_ode_ord1(rhs, var0, dt, N_STEPS, method='rk4', periodic=periodic)

# Postprocess
rez[:, 0] = rez[:, 0] - np.pi/2
rez[:, 1] = rez[:, 1] - np.pi/2

x1 = l1*np.cos(rez[:, 0])
y1 = l1*np.sin(rez[:, 0])
x2 = x1+l2*np.cos(rez[:, 1])
y2 = y1+l2*np.sin(rez[:, 1])

#####################
# Plot
#####################

## Plot velocity
#plt.figure()
#plt.plot(rez[:, 0], label='x1')
#plt.plot(rez[:, 1], label='x2')
#plt.plot(rez[:, 2], label='v1')
#plt.plot(rez[:, 3], label='v2')
#plt.legend()
#plt.show()

# Sanity check - plot total energy over time
#KE1 = np.array([m1*l1*l1*w1*w1/2 for w1 in rez[:, 2]])
#KE2 = np.array([m2*l2*l2*w2*w2/2 for w2 in rez[:, 3]])
#KE12 = np.array([m2*l1*l2*w1*w2*np.cos(x1-x2) for x1,x2,w1,w2 in rez])
#PE1 = m1*g*y1
#PE2 = m2*g*y2
KE1,KE2,PE1,PE2 = dp_energy(rez, m1, m2, l1, l2, g)


plt.figure()
#plt.plot(KE1)
#plt.plot(KE2)
#plt.plot(PE1)
#plt.plot(PE2)
plt.plot(KE1+KE2, label="Kinetic")
plt.plot(PE1+PE2, label="Potential")
plt.plot(KE1+KE2+PE1+PE2, label="Total")
plt.legend()
plt.show()

## Plot movie
#plt.ion()
#fig, ax = plt.subplots(tight_layout=True, figsize=(7,7))
#ball0, = ax.plot(x1[0], y1[0], 'o')
#ball1, = ax.plot(x2[0], y2[0], 'o')
#radlim = 1.1 * (l1+l2)
#plt.xlim(-radlim, radlim)
#plt.ylim(-radlim, radlim)
#plt.show()

#for i in range(1, N_STEPS):
    #try:
        #ball0.set_xdata(x1[i])
        #ball0.set_ydata(y1[i])
        #ball1.set_xdata(x2[i])
        #ball1.set_ydata(y2[i])
        #fig.canvas.draw()
        #fig.canvas.flush_events()

    #except KeyboardInterrupt:
        #print("Aborted by user!")
        #try:
            #sys.exit(0)
        #except SystemExit:
            #os._exit(0)
