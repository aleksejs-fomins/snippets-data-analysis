"""
===========================
The double pendulum problem
===========================

This animation illustrates the double pendulum problem.
"""

# Double pendulum formula translated from the C code at
# http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg


def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[2] - state[0]
    den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) +
               M2*G*sin(state[2])*cos(del_) +
               M2*L2*state[3]*state[3]*sin(del_) -
               (M1 + M2)*G*sin(state[0]))/den1

    dydx[2] = state[3]

    den2 = (L2/L1)*den1
    dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_) +
               (M1 + M2)*G*sin(state[0])*cos(del_) -
               (M1 + M2)*L1*state[1]*state[1]*sin(del_) -
               (M1 + M2)*G*sin(state[2]))/den2

    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0.0, 20, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

# Kinetic and potential energy
KE1 = np.array([M1*L1*L1*w1*w1/2 for w1 in y[:, 1]])
KE2_1 = np.array([M2*L2*L2*w2*w2/2 for w2 in y[:, 3]])
KE2_2 = np.array([M2*L1*L1*w1*w1/2 for w1 in y[:, 1]])
KE2_3 = np.array([M2*L1*L2*w1*w2*np.cos(x1-x2) for x1,w1,x2,w2 in y])
PE1 = M1*G*y1
PE2 = M2*G*y2

plt.figure()
plt.plot(KE1+KE2_1+KE2_2+KE2_3, label="Kinetic")
plt.plot(PE1+PE2, label="Potential")
plt.plot(KE1+KE2_1+KE2_2+KE2_3+PE1+PE2, label="Total")
plt.legend()
plt.show()

#fig = plt.figure()
#ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
#ax.grid()

#line, = ax.plot([], [], 'o-', lw=2)
#time_template = 'time = %.1fs'
#time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


#def init():
    #line.set_data([], [])
    #time_text.set_text('')
    #return line, time_text


#def animate(i):
    #thisx = [0, x1[i], x2[i]]
    #thisy = [0, y1[i], y2[i]]

    #line.set_data(thisx, thisy)
    #time_text.set_text(time_template % (i*dt))
    #return line, time_text

#ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
                              #interval=25, blit=True, init_func=init)

## ani.save('double_pendulum.mp4', fps=15)
#plt.show()
