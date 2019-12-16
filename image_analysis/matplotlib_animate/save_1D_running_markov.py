import numpy as np
from save_plot_anim import save1Dwindow

N = 300
window = 100

x1D = np.linspace(0, 10, N)
y1D = np.zeros(N)
for i in range(1, N):
    y1D[i] = y1D[i-1] + np.random.normal(0, 0.02)
    
save1Dwindow('runningMarkov.mp4', x1D, y1D, [-1, 1], window)
