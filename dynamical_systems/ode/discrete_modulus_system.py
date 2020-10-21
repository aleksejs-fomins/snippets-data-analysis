import numpy as np
import matplotlib.pyplot as plt



base = 20
step = 11


def update(v, inc, N):
    return (v + inc) % N**2


v = 0
x = [0]
y = [0]

for i in range(200):
    v = update(v, step, base)
    x += [v // base]
    y += [v % base]

plt.figure()
plt.plot(x[:-1], y[1:])
plt.show()