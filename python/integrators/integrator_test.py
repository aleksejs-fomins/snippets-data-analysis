import numpy as np
from integrator_lib import integrate_ode_ord1
import matplotlib.pyplot as plt

def osc_rhs(var, t, w2):
    x,v = var
    return np.array([v, -w2 * x])


w2 = 10
w = np.sqrt(w2)
x0 = 5
v0 = 0
dt = 0.01
nstep = 10000

ttrue = np.linspace(0, nstep*dt, nstep+1)
xtrue = x0*np.cos(w*ttrue)
vtrue = -x0*w*np.sin(w*ttrue)

rhs1 = lambda var, t: osc_rhs(var, t, w2)

fig, ax = plt.subplots(nrows=2, ncols=3, tight_layout=True)

methods = ['naive_ord1', 'rk2', 'rk4']

for i, method in enumerate(methods):
    rez = integrate_ode_ord1(rhs1, np.array([x0, v0]), dt, nstep, method=method)

    ax[0][i].plot(rez[:, 0], label='x')
    ax[0][i].plot(rez[:, 1], label='v')
    ax[0][i].legend()
    ax[0][i].set_title('result for method='+ method)

    ax[1][i].plot(np.abs(rez[:, 0]-xtrue), label='x')
    ax[1][i].plot(np.abs(rez[:, 1]-vtrue), label='v')
    ax[1][i].legend()
    ax[1][i].set_title('error for method='+ method)
plt.show()
