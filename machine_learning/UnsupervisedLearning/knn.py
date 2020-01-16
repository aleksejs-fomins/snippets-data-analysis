import random

import matplotlib.pyplot as plt

from lib.machine_learning import knn
from lib.stat import randstat


# Zip to list of lists
def listzip(x, y):
    return [list(it) for it in zip(x, y)]

randstat.init()
N_POINT = 100
COLORS = ['red', 'green']

x = [random.uniform(-1, 1) for i in range(0, N_POINT)]
y = [random.uniform(-1, 1) for i in range(0, N_POINT)]
t = [COLORS[random.randint(0,1)] for i in range(0, N_POINT)]
vList = listzip(x,y)
p = [0.5, 0.3]

knn.knn(vList, t, p, 1)
knn.knn(vList, t, p, 2)
knn.knn(vList, t, p, 3)
knn.knn(vList, t, p, 4)
knn.knn(vList, t, p, 5)
knn.maxEField(vList, t, p)

plt.scatter(x,y, color=t)
plt.show()

