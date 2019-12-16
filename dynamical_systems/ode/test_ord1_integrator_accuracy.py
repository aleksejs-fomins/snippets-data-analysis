import numpy as np
import matplotlib.pyplot as plt

# Import external libraries
from lib.numerics.integrator_lib import integrate_ode_ord1
from lib.numerics.example_ode.sho import sho_rhs, sho_true


# Define constants for SHO
w = 5
x0 = 5
v0 = 0
dt = 0.01
nstep = 100000

# Define integrator-conforming RHS with inserted constants. Note SHO is time-invariant
rhs1 = lambda var, t: np.array(sho_rhs(var[0], var[1], w))

# Compute true values
ttrue = np.linspace(0, dt*nstep, nstep+1)
xtrue, vtrue = sho_true(x0, v0, w, ttrue)

# Plot value and error for different methods
fig, ax = plt.subplots(nrows=2, ncols=4, tight_layout=True)
methods = ['naive_ord1', 'rk2', 'rk4', 'scipy']

for i, method in enumerate(methods):
    rez = integrate_ode_ord1(rhs1, np.array([x0, v0]), dt, nstep, method=method)

    ax[0][i].plot(rez[:, 0], label='x')
    ax[0][i].plot(rez[:, 1], label='v')
    ax[0][i].legend()
    ax[0][i].set_title('result for method='+ method)

    ax[1][i].semilogy(np.abs(rez[:, 0]-xtrue), label='x')
    ax[1][i].semilogy(np.abs(rez[:, 1]-vtrue), label='v')
    ax[1][i].legend()
    ax[1][i].set_title('error for method='+ method)
plt.show()
