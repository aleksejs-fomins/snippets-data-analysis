import numpy as np
import scipy.integrate as integrate
#import sdeint

def integrate_ode_ord1(rhs, x0, dt, nStep, method='naive_ord1', periodic=None):
    nDof = len(x0)

    if method == 'naive_ord1':
        rez = np.zeros((nStep+1, nDof))
        rez[0] = x0
        for i in range(nStep):
            rez[i+1] = rez[i] + rhs(rez[i], dt*i)*dt
        
    elif method == 'rk2':
        rez = np.zeros((nStep+1, nDof))
        rez[0] = x0
        for i in range(nStep):
            k1 = dt*rhs(rez[i], dt*i)
            k2 = dt*rhs(rez[i] + k1/2, dt*(i+0.5))
            rez[i+1] = rez[i] + k2
        
    elif method == 'rk4':
        rez = np.zeros((nStep+1, nDof))
        rez[0] = x0
        for i in range(nStep):
            k1 = dt*rhs(rez[i],        dt*i)
            k2 = dt*rhs(rez[i] + k1/2, dt*(i+0.5))
            k3 = dt*rhs(rez[i] + k2/2, dt*(i+0.5))
            k4 = dt*rhs(rez[i] + k3,   dt*(i+1))
            rez[i+1] = rez[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        
    elif method == 'scipy':
        t = np.linspace(0.0, dt*nStep, nStep+1)
        rez = integrate.odeint(rhs, x0, t)
        
    else:
        raise ValueError('Unknown method', method)
    
    # TODO: Figure out a good way to do periodicity
    # If some DOF are periodic, normalize them to correct range to avoid numerical errors
    if periodic is not None:
        for j in range(nDof):
            if periodic[j] is not None:
                rez[:, j] = np.remainder(rez[:, j], periodic[j])

    return rez


#def integrate_sde_ord1(F, G, x0, dt, nStep, eqtype='ito'):
    #tspan = np.linspace(0.0, dt*nStep, nStep+1)
    #if eqtype == 'ito':
        #rez = sdeint.itoint(F, G, x0, tspan)
    #elif eqtype == 'stratonovich':
        #rez = sdeint.stratint(F, G, x0, tspan)
    #else:
        #raise ValueError('Unknown equation type', eqtype)
    #return rez
