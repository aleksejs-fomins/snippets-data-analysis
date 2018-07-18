import numpy as np
import matplotlib.pyplot as plt

pold = {
    'G' : 0.05,
    'H' : 0.0002,
    'N' : 0.0001,
    'S' : 0.1,
    'T' : 200,
    'X' : 1000,
    'Y' : 100
}

p = {
    'k' : pold['S'] / pold['G'],
    't' : pold['G'] * pold['T'],
    'x' : pold['N'] / pold['G'] * pold['X'],
    'y' : pold['H'] / pold['G'] * pold['Y'],
    'dt' : 0.01
}

print(p)


tlist = np.linspace(0, p['t'], p['t'] / p['dt'])

xy = [p['k'], 0.5]
xylist = [xy]
for t in range(len(tlist)-1):
    xy = [
        xy[0] + p['dt'] * (xy[0] - xy[0] * xy[1]),
        xy[1] + p['dt'] * (xy[0] * xy[1] - p['k'] * xy[1])
    ]
    xylist.append(xy)

plt.plot(tlist, np.array([it[0] for it in xylist]))
plt.plot(tlist, np.array([it[1] for it in xylist]))
plt.legend(['x', 'y'])
plt.show()


