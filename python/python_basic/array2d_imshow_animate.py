import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

np.random.seed(int(time.time()))

fig, axes = plt.subplots(ncols=1, nrows=1, figsize=[100, 100], squeeze=True)

# Remove ticks
axes.set_xticks([])
axes.set_yticks([])




# line, = ax.plot(np.random.rand(10))
# ax.set_ylim(0, 1)


def update(data, im):
    # c = plt.Circle((0, 5), radius=5, label='patch')
    # axes.add_patch(c)
    #return ax.imshow(data, interpolation='none'),
    return im.set_data(data),

def rands():
    return np.random.random_sample(size=(20, 100))

def data_gen():
    while True:
        yield rands()

im = axes.imshow(rands(), interpolation='none')
ani = animation.FuncAnimation(fig, lambda data: update(data, im), data_gen, interval=100)
plt.show()





