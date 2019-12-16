import numpy as np
import matplotlib.pyplot as plt
import h5py

# Import external libraries
from lib.numerics.integrator_lib import integrate_ode_ord1
from lib.numerics.example_ode.multibalanced2d import multilin_forced_rhs


#####################
# Initialize
#####################

# Define constants for SHO
M = np.array([[-1,-1],[1, -1]])
f = lambda t: np.array([np.round(np.sin(t)**2), 0])
dt = 0.01
N_STEPS = 1000


#####################
# Run
#####################

# Define integrator-conforming RHS with inserted constants. Note SHO is time-invariant
rhs = lambda var, t: np.array(multilin_forced_rhs(var, M, f, t))

# Integrate the problem
rez = integrate_ode_ord1(rhs, np.array([0, 0]), dt, N_STEPS, method='scipy')

######################
## Write data to file
######################

#outfilename = "data/sho_" + str(N_OSC) + ".h5"
#h5f = h5py.File(outfilename, "w")
#h5f['dt'] = dt
#h5f['w'] = w
#h5f['x'] = rez[:N_OSC]
#h5f['v'] = rez[N_OSC:]
#h5f.close()

#####################
# Plot
#####################
t_lst = np.linspace(0, dt*N_STEPS, N_STEPS+1)

# Plot result
plt.figure()
plt.plot(t_lst, rez[:, 0], label='exc')
plt.plot(t_lst, rez[:, 1], label='inh')
plt.plot(t_lst, f(t_lst)[0], label='input')
plt.legend()
plt.show()
