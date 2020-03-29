import numpy as np
import matplotlib.pyplot as plt
import h5py

# Append base directory
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(__file__))
base_dir = currentdir[:currentdir.index('python')] + 'python/'
sys.path.insert(0,base_dir)
print("Appended base directory", base_dir)

# Import external libraries
from aux.numerics.integrator_lib import integrate_ode_ord1
import aux.numerics.example_ode.chaotic as chaotic


#####################
# Initialize
#####################

# Define constants for SHO
dt = 0.01
nSteps = 10000
nTraj = 10

#param = [1.2, -1, 1, 0.5, 0.3]
param = [0.5, 1, 5, 8, 0.02]

#####################
# Run
#####################

# Define integrator-conforming RHS with inserted constants. Note SHO is time-invariant
rhs = lambda var, t: np.array(chaotic.rhs_duffing_2D(*var, t, *param))

# Integrate the problem
rez = [integrate_ode_ord1(rhs, np.random.uniform(-1, 1, 2), dt, nSteps, method='scipy') for iTraj in range(nTraj)]

#####################
# Plot
#####################
tLst = np.arange(nSteps+1)*dt

# Plot result
plt.figure()
for traj in rez:
    plt.plot(traj[:, 0], traj[:, 1])
plt.legend()
plt.show()
