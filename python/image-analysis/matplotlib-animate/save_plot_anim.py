import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_y(iY, y2D, line):
    print(iY)
    line.set_ydata(y2D[iY])
    return line,

def update_window(i, x1D, y1D, window, line):
    print(i)
    if i < window:
        plt.xlim(x1D[0], x1D[window])
    else:
        plt.xlim(x1D[i-window], x1D[i])
        
    iLeft = max(i-window, 0)
    line.set_data([x1D[iLeft:i], y1D[iLeft:i]])
    return line,

def save1D(outFile, x1D, y2D, xlim, ylim, fps=30):
    # Set up formatting for the movie files
    writer = animation.writers['ffmpeg'](fps=fps, metadata=dict(artist='Me'))
    
    # Creating a placeholder figure
    fig1 = plt.figure()
    #line1, = plt.plot([], [], 'r-')
    line1, = plt.plot(x1D, y2D[0], 'r-')
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    #line1.set_xdata(x1D)
    
    # Creating and saving an animation
    nStep = y2D.shape[0]
    line_ani = animation.FuncAnimation(fig1, update_y, nStep, fargs=(y2D, line1), repeat=False, blit=True)
    line_ani.save(outFile, writer=writer)

    
def save1Dwindow(outFile, x1D, y1D, ylim, window, fps=30):
    # Set up formatting for the movie files
    writer = animation.writers['ffmpeg'](fps=fps, metadata=dict(artist='Me'))
    
    # Creating a placeholder figure
    fig1 = plt.figure()
    line1, = plt.plot([], [], 'r-')
    plt.ylim(ylim[0], ylim[1])
    
    # Creating and saving an animation
    nStep = len(x1D)
    line_ani = animation.FuncAnimation(fig1, update_window, nStep, fargs=(x1D, y1D, window, line1), repeat=False, blit=True)
    line_ani.save(outFile, writer=writer)







