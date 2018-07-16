import numpy as np
import matplotlib.pyplot as plt

def gaussian(t, s):
    return np.exp(-(t / s)**2 / 2.0)


def forwardsIntegrator(smax, sigma, tau, nstep):
    TMIN = -5.0 * sigma
    TMAX = 10.0 * np.sqrt(tau)
    DT = (TMAX - TMIN) / nstep

    t_sol = [TMIN]
    f_sol = [0.0]

    for i in range(1, nstep + 1):
        t_sol.append(t_sol[i - 1] + DT)
        f_sol.append(f_sol[i - 1] * (1.0 - DT / tau) + smax * DT * gaussian(t_sol[i - 1], sigma))

    return t_sol, f_sol



#sigmaList = [1.0, 0.5, 0.1]
#tauList = [1.0] * len(sigmaList)
tauList = [10.0, 1.0, 0.1]
sigmaList = [it / 10.0 for it in tauList]
sigmaxList = [1.0 / np.sqrt(s * t) for s,t in zip(sigmaList, tauList)]
nstepList = [10000] * len(sigmaList)



for SIGMA, SIGMAX, TAU, NSTEP in zip(sigmaList, sigmaxList, tauList, nstepList):
    t_sol, f_sol = forwardsIntegrator(SIGMAX, SIGMA, TAU, NSTEP)

    plt.plot(t_sol, f_sol)

plt.show()





# x = np.linspace(-5, 5, 100)
# y = gaussian(x)
# plt.plot(x,y)
# plt.show()