import numpy as np
import scipy.special as spsp
import matplotlib.pyplot as plt


def Hstep(x):
    return 1.0 * (x >= 0)


def prof1_exp(s0, tau, t):
    return s0 * np.exp(-t / tau)


def prof2_step(s0, t0, tau, t):
    return prof1_exp(s0, tau, t-t0) * Hstep(t-t0)


def prof3_smooth(s0, t0, tau, sigma, t):
    return prof1_exp(s0, tau, t - t0) \
       * np.exp((sigma / tau)**2 / 2.0) \
       * (1.0 + spsp.erf((t - t0 - sigma**2 / tau)/(sigma * np.sqrt(2)))) / 2.0


        # Profile 1
# x = np.linspace(0, 2, 100)
# y = prof1_exp(1.0, 1.0, x)
# plt.plot(x,y)
# plt.show()

# Profile 2
# x = np.linspace(0, 3, 100)
# y = prof2_step(1.0, 1.0, 1.0, x)
# plt.plot(x,y)
# plt.show()

# Profile 3
x = np.linspace(-3, 10, 100)
y1 = prof3_smooth(1.0, 1.0, 1.0, 1.0, x)
y2 = prof3_smooth(1.0, 1.0, 2.0, 1.0, x)
y3 = prof3_smooth(1.0, 1.0, 3.0, 1.0, x)
y4 = prof3_smooth(1.0, 1.0, 4.0, 1.0, x)
y5 = prof3_smooth(1.0, 1.0, 5.0, 1.0, x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)
plt.show()
