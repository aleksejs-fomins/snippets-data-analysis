import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# RNG
np.random.seed(int(time.time()))

# CONSTANTS
CIRC_RAD = 1.0
X_RANGE = [0.0, 10.0]
Y_RANGE = [0.0, 20.0]
X_RANGE_ZEALOUS = [X_RANGE[0] + CIRC_RAD, X_RANGE[1] - CIRC_RAD]
Y_RANGE_ZEALOUS = [Y_RANGE[0] + CIRC_RAD, Y_RANGE[1] - CIRC_RAD]


# Figure setup
fig, axes = plt.subplots(ncols=1, nrows=1) #, figsize=[100, 100], squeeze=True)
axes.set_xlim(X_RANGE[0], X_RANGE[1])
axes.set_ylim(Y_RANGE[0], Y_RANGE[1])
axes.set_aspect('equal')

# Remove ticks
#axes.set_xticks([])
#axes.set_yticks([])

# Draw a circle
firstpos = np.array([
    np.random.uniform(X_RANGE_ZEALOUS[0], X_RANGE_ZEALOUS[1], 1)[0],
    np.random.uniform(Y_RANGE_ZEALOUS[0], Y_RANGE_ZEALOUS[1], 1)[0]])
c = plt.Circle(tuple(firstpos), radius=CIRC_RAD, label='patch')
axes.add_patch(c)


def update(data, circ):
    circ.center = tuple(data)

def data_gen(firstpos, dt, v):
    this_pos = firstpos
    this_v = np.array(v)

    while True:
        next_pos = this_pos + this_v * dt

        if (next_pos[0] < X_RANGE_ZEALOUS[0]) or (next_pos[0] > X_RANGE_ZEALOUS[1]):
            this_v[0] *= -1

        if (next_pos[1] < Y_RANGE_ZEALOUS[0]) or (next_pos[1] > Y_RANGE_ZEALOUS[1]):
            this_v[1] *= -1

        this_pos = this_pos + this_v * dt

        yield this_pos



# Animate
ani = animation.FuncAnimation(fig, lambda data: update(data, c),
                              lambda: data_gen(firstpos, 0.1, [1, 1]), interval=10)
plt.show()