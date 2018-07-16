import numpy as np
import random
import matplotlib.pyplot as plt


from python.aux import randstat, discretemath, machinelearning


randstat.init()

N_POINT = 100
COLORS = ['red', 'green']

x = [random.uniform(-1, 1) for i in range(0, N_POINT)]
y = [random.uniform(-1, 1) for i in range(0, N_POINT)]
t = [COLORS[random.randint(0,1)] for i in range(0, N_POINT)]
vList = discretemath.listzip(x,y)
p = [0.5, 0.3]

machinelearning.knn(vList, t, p, 1)
machinelearning.knn(vList, t, p, 2)
machinelearning.knn(vList, t, p, 3)
machinelearning.knn(vList, t, p, 4)
machinelearning.knn(vList, t, p, 5)
machinelearning.maxEField(vList, t, p)

plt.scatter(x,y, color=t)
plt.show()

