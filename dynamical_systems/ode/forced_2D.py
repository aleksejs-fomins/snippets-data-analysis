import numpy as np
import matplotlib.pyplot as plt
import h5py

# Import external libraries
from lib.numerics.integrator_lib import integrate_ode_ord1
from lib.numerics.example_ode.forced_2D import forced_2D_rhs


#####################
# Initialize
#####################

# Both systems inhibit themselves (Leaky)
# 1st system excites 2nd
# 2nd system inhibits 1st
M = np.array([[-1, -1],[1, -1]])

# Both variables start in resting state
b = np.array([0, 0])

# Only first variable is forced
f = lambda t: np.array([0.25 * np.round(np.sin(t)**2), 0])
#f = lambda t: np.array([1, 0])

dt = 0.01
N_STEPS = 1000


#####################
# Run
#####################

# Define integrator-conforming RHS with inserted constants. Note SHO is time-invariant
rhs = lambda var, t: forced_2D_rhs(var, M, f, t)

# Integrate the problem
rez = integrate_ode_ord1(rhs, b, dt, N_STEPS, method='scipy')

#####################
# Plot
#####################

t_arr = np.linspace(0, dt*N_STEPS, N_STEPS+1)

# Plot result
plt.figure()
plt.plot(t_arr, rez[:,0], label = 'exc')
plt.plot(t_arr, rez[:,1], label = 'inh')
plt.plot(t_arr, f(t_arr)[0], label = 'force')
plt.legend()
plt.show()

