import numpy as np

'''
  TODO:
   * Convention for parameter selection
   * Convention for initial conditions
'''

class KuramotoOscillator:
    def __init__(self, dt, N, K):
        self.dt = dt
        self.N = N
        self.A = np.random.uniform(0, 2*np.pi, N) * dt
        self.B = K * dt
    
    def nextx(self, x):
        cosx = np.cos(x)
        sinx = np.sin(x)
        
        rcosf = np.mean(cosx)
        rsinf = np.mean(sinx)
        
        return np.remainder(x + self.A + self.B*(rsinf*cosx - rcosf*sinx), 2*np.pi)
        
    def run(self, nStep):
        
        rez = np.zeros((nStep+1, self.N))
        rez[0, :] = np.random.uniform(0, 2*np.pi, self.N)
        
        for i in range(nStep):
            rez[i+1,:] = self.nextx(rez[i, :])
        
        return rez

