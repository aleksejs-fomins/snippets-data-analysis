import numpy as np

def integrate_ode_ord1(rhs, x0, dt, n, method='naive_ord1'):
    rez = np.zeros((n+1, len(x0)))
    rez[0] = x0
                   
    if method == 'naive_ord1':
        for i in range(n):
            rez[i+1] = rez[i] + rhs(rez[i], dt*i)*dt
    elif method == 'rk2':
        #rez[1] = rez[0] + rhs(rez[0], 0)*dt
        #for i in range(1, n):
            #rez[i+1] = rez[i-1] + rhs(rez[i], dt*i)*dt
        for i in range(n):
            k1 = dt*rhs(rez[i], dt*i)
            k2 = dt*rhs(rez[i] + k1/2, dt*(i+0.5))
            rez[i+1] = rez[i] + k2
            
    elif method == 'rk4':
        for i in range(n):            
            k1 = dt*rhs(rez[i],        dt*i)
            k2 = dt*rhs(rez[i] + k1/2, dt*(i+0.5))
            k3 = dt*rhs(rez[i] + k2/2, dt*(i+0.5))
            k4 = dt*rhs(rez[i] + k3,   dt*(i+1))
            rez[i+1] = rez[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    else:
        raise ValueError('Unknown method', method)
        
    return rez
