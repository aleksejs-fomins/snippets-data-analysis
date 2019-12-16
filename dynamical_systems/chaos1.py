import numpy as np
import matplotlib.pyplot as plt


def Rmat(th):
    c = np.cos(th)
    s = np.sin(th)
    return np.array([[c, s], [-s, c]])

x0 = np.array([0.1, 0.9])
b = np.array([-0.3, 0.3])
M = Rmat(np.pi / 18)


xn = [x0]
for i in range(0,100):
    #xn.append(b + (M*xn[i])[0])
    xn.append(b + np.dot(M,xn[i]))

print(xn)

x = [x for x,y in list(xn)]
y = [y for x,y in list(xn)]

plt.scatter(x, y)
plt.show()


