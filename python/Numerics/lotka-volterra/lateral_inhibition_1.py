'''
   Simulate 4 diff equations with 4 unknowns
'''

import numpy as np
import matplotlib.pyplot as plt
import copy


def update(D, N):
    Dnew = copy.deepcopy(D)
    Nnew = copy.deepcopy(N)

    Dk = [D[0] ** p['k'], D[1] ** p['k']]
    Nh = [N[0] ** p['h'], N[1] ** p['h']]

    Dnew[0] += p['dt'] * (1.0 / (1.0 + p['b'] * Nh[0]) - D[0])
    Dnew[1] += p['dt'] * (1.0 / (1.0 + p['b'] * Nh[1]) - D[1])
    Nnew[0] += p['dt'] * (Dk[1] / (p['a'] + Dk[1]) - N[0])
    Nnew[1] += p['dt'] * (Dk[0] / (p['a'] + Dk[0]) - N[1])

    return Dnew, Nnew

# Init vars
D = np.array([0.99, 1.0])
N = np.array([1.0, 1.0])
p = {
    'a' : 0.01,
    'b' : 100,
    'k' : 2,
    'h' : 2,
    'dt' : 0.01}

# Perform simulation
T = 50
tlist = np.linspace(0, T, T / p['dt'])

Dlist = [D]
Nlist = [N]
for t in range(len(tlist)-1):
    D, N = update(D, N)
    Dlist.append(D)
    Nlist.append(N)

print("Final concentration of D = ", Dlist[len(Dlist) - 1])
print("Final concentration of N = ", Nlist[len(Nlist) - 1])

plt.plot(tlist, np.array([d[0] for d in Dlist]))
plt.plot(tlist, np.array([d[1] for d in Dlist]))
plt.plot(tlist, np.array([n[0] for n in Nlist]))
plt.plot(tlist, np.array([n[1] for n in Nlist]))
plt.legend(['D1', 'D2', 'N1', 'N2'])
plt.show()

