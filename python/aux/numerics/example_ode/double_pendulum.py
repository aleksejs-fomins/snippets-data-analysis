import numpy as np

#def dp_rhs(var, m1, m2, l1, l2, g):
    #x1,x2,v1,v2 = var
    
    #eta1 = m1 / (m1 + m2)
    #eta2 = m2 / (m1 + m2)
    #sin1 = np.sin(x1)
    #sin2 = np.sin(x2)
    #dcos = np.cos(x1-x2)
    #dsin = np.sin(x1-x2)
    
    #norm = eta1 + eta2 * dsin**2
    #dv1 = - (eta2 * dsin * (dcos * v1**2 + (l2/l1)*v2**2) + (g/l1)*(sin1 - eta2*dcos*sin2)) / norm
    #dv2 = (dsin*(eta2*dcos*v2**2+(l1/l2)*v1**2)-(g/l2)*(sin2 - dcos*sin1)) / norm
    
    #return np.array([v1,v2,dv1,dv2])
    
    
    
#def dp_rhs(var, m1, m2, l1, l2, g):
    ## Vars
    #x1,x2,v1,v2 = var
    
    ## Parameters
    #w1_2 = g / l1
    #w2_2 = g / l2
    #alpha = m2 / (m1 + m2)
    #beta = l1 / l2
    #alpha_d_beta = alpha / beta
    
    ## Precomp
    #sin1 = np.sin(x1)
    #sin2 = np.sin(x2)
    #x_delta = x1-x2
    #sin_delta = np.sin(x_delta)
    #cos_delta = np.cos(x_delta)
    
    ## Solve linear system for velocities
    #rhs = np.array([
        #alpha * sin_delta * v1**2 - w1_2 * sin1,
        #-beta * sin_delta * v2**2 - w2_2 * sin2])
    #M = np.array([[1.0, alpha_d_beta * cos_delta], [beta * cos_delta, 1.0]])

    #dv2, dv1 = np.linalg.solve(M, rhs)
    
    #return [v1,v2,dv1,dv2]
    
    
def dp_rhs(var, m1, m2, l1, l2, g):
    # Vars
    x1,x2,w1,w2 = var

    # Precomp
    del_ = x2 - x1
    sin1 = np.sin(x1)
    sin2 = np.sin(x2)
    sin_del = np.sin(del_)
    cos_del = np.cos(del_)
    den1 = (m1 + m2)*l1 - m2*l1*cos_del*cos_del
    den2 = (l2/l1)*den1
    
    
    dw1 = (m2*l1*w1*w1*sin_del*cos_del +
               m2*g*sin2*cos_del +
               m2*l2*w2*w2*sin_del -
               (m1 + m2)*g*sin1)/den1
    
    dw2 = (-m2*l2*w2*w2*sin_del*cos_del +
               (m1 + m2)*g*sin1*cos_del -
               (m1 + m2)*l1*w1*w1*sin_del -
               (m1 + m2)*g*sin2)/den2

    return [w1,w2,dw1,dw2]


# Kinetic and potential energy of a double pendulum
def dp_energy(var, m1, m2, l1, l2, g):
    t1arr = var[:, 0]
    t2arr = var[:, 1]
    v1arr = l1 * var[:, 2]
    v2arr = l2 * var[:, 3]
    
    y1 = l1 * np.sin(t1arr)
    y2 = y1 + l2 * np.sin(t2arr)
    
    KE1 = m1 * np.array([v1**2 / 2 for v1 in v1arr])
    KE2 = m2 * np.array([(v1**2 + v2**2 + 2*v1*v2*np.cos(t1 - t2) ) / 2 for t1,t2,v1,v2 in zip(t1arr, t2arr, v1arr, v2arr)])
    PE1 = m1 * g * y1
    PE2 = m1 * g * y2
    
    return KE1, KE2, PE1, PE2
