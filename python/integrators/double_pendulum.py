import numpy as np
from integrator_lib import integrate_ode_ord1
import matplotlib.pyplot as plt

def dp_rhs(var, m1, m2, l1, l2, g):
    x1,x2,v1,v2 = var
    
    eta1 = m1 / (m1 + m2)
    eta2 = m2 / (m1 + m2)
    sin1 = np.sin(x1)
    sin2 = np.sin(x2)
    dcos = np.cos(x1-x2)
    dsin = np.sin(x1-x2)
    
    norm = eta1 + eta2 * dsin**2
    dv1 = - (eta2 * dsin * (dcos * v1**2 + (l2/l1)*v2**2) + (g/l1)*(sin1 - eta2*dcos*sin2)) / norm
    dv2 = (dsin*(eta2*dcos*v2**2+(l1/l2)*v1**2)-(g/l2)*(sin2 - dcos*sin1)) / norm
    
    return np.array([v1,v2,dv1,dv2])


m1 = 0.1 # kg
m2 = 0.1 # kg
l1 = 0.1 # m
l2 = 0.1 # m
g = 9.8  # N/kg

rhs1 = lambda var, t: dp_rhs(var, m1,m2,l1,l2,g)

methods = ['naive_ord1', 'rk2', 'rk4']


rez = integrate_ode_ord1(rhs1, np.array([np.pi/2, np.pi/2, 0, 0]), 0.01, 10000, method='rk4')

x1 = l1*np.cos(rez[:, 0])
y1 = l1*np.sin(rez[:, 0])
x2 = x1+l2*np.cos(rez[:, 1])
y2 = y1+l2*np.sin(rez[:, 1])

print(rez.shape)


plt.figure()
plt.plot(x1,y1)
plt.plot(x2,y2)
radlim = 1.1*(l1+l2)
plt.xlim(-radlim, radlim)
plt.ylim(-radlim, radlim)
plt.show()
