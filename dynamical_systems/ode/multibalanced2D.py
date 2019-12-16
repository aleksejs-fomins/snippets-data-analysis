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
N_OSC = 5
M_local = np.array([[-1,-1],[1, -1]])
M = np.zeros((2*N_OSC, 2*N_OSC))

# Local connectivity
for i in range(N_OSC):
    M[2*i:2*i+2, 2*i:2*i+2] = M_local
    
# Connect oscillators in chain
for i in range(N_OSC-1):
    M[2*i+2, 2*i] = 1
    
# Forcing only for first neuron
f_one = lambda t: np.round(np.sin(t)**2)

def f(t):
    rez = np.zeros(2*N_OSC)
    rez[0] = f_one(t)
    return rez

dt = 0.01
N_STEPS = 1000


#####################
# Run
#####################

# Define integrator-conforming RHS with inserted constants. Note SHO is time-invariant
rhs = lambda var, t: np.array(multilin_forced_rhs(var, M, f, t))

# Integrate the problem
rez = integrate_ode_ord1(rhs, np.zeros(2*N_OSC), dt, N_STEPS, method='scipy')

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
plt.plot(t_lst, f_one(t_lst), label='input')

for i in range(N_OSC):
    plt.plot(t_lst, rez[:, 2*i], label='exc'+str(i))
plt.legend()
plt.show()
