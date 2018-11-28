import numpy as np
import matplotlib.pyplot as plt
from kuramoto_lib import KuramotoOscillator


N_STEPS = 10000
N_OSC = 20
COUPLING_STRENGTH = 5

ko1 = KuramotoOscillator(0.01, N_OSC, COUPLING_STRENGTH)

rez = ko1.run(N_STEPS)

plt.ion()
fig, ax = plt.subplots()
line1, = ax.plot(np.cos(rez[0, :]), np.sin(rez[0, :]), 'o')
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])
plt.show()


for i in range(1, N_STEPS):
    line1.set_xdata(np.cos(rez[i, :]))
    line1.set_ydata(np.sin(rez[i, :]))
    fig.canvas.draw()
    fig.canvas.flush_events()
    

    
