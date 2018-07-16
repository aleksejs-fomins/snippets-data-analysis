import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

v0 = np.array([1, 0])
v1 = np.array([0, 1])
v2 = np.array([-0.6, -0.8])

def min3d(Xm, Ym):
    def diff2(x1, y1, x2, y2):
        return (x1 - x2)**2 + (y1-y2)**2

    return np.sqrt(diff2(Xm, Ym, v0[0], v0[1]) * diff2(Xm, Ym, v1[0], v1[1]) * diff2(Xm, Ym, v2[0], v2[1]))


fig = plt.figure()
ax = fig.gca()
#ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-2, 2, 0.01)
Y = np.arange(-2, 2, 0.01)
Xm, Ym = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
Z = min3d(Xm, Ym)
print(Z.shape)


# Plot the surface.
#surf = ax.plot_surface(Xm, Ym, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
surf = ax.imshow(Z, cmap='jet', interpolation='nearest')

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()




