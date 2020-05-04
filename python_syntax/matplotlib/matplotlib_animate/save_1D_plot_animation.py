import numpy as np
from lib.plot.save_plot_anim import save1D

NX = 1000
NT = 200
x1D = np.linspace(0, 10, NX)
y2D = np.zeros((NT, NX))
for i in range(NT):
    y2D[i] = np.sin(x1D + 0.05 * i)
    
save1D('fancySine.mp4', x1D, y2D, [0, 10], [-1, 1])
