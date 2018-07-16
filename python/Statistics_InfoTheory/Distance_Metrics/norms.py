import matplotlib.pyplot as plt
import numpy as np

def normMin(x, y):
    return np.minimum(abs(x),abs(y))

def normMax(x, y):
    return np.maximum(abs(x),abs(y))

def norm_1(x, y):
    return 2 / (1/abs(x) + 1/abs(y))

def norm0(x, y):
    return np.sqrt(abs(x)*abs(y))

def norm05(x, y):
    return ((np.sqrt(abs(x)) + np.sqrt(abs(y)))/2)**2

def norm1(x, y):
    return (abs(x) + abs(y)) / 2

def norm2(x, y):
    return np.sqrt((x**2 + y**2) / 2)

x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
xx,yy = np.meshgrid(x, y)

zzMin = normMin(xx, yy)
zzMax = normMax(xx, yy)
zz_1 = norm_1(xx, yy)
zz05 = norm05(xx, yy)
zz0 = norm0(xx, yy)
zz1 = norm1(xx, yy)
zz2 = norm2(xx, yy)

plt.figure()

CSmin = plt.contour(xx, yy, zzMin, [1])
#plt.clabel(CSmin, inline=1, fontsize=10)

CSmax = plt.contour(xx, yy, zzMax, [1])
#plt.clabel(CSmax, inline=1, fontsize=10)

CS_1 = plt.contour(xx, yy, zz_1, [1])
#plt.clabel(CS_1, inline=1, fontsize=10)

CS05 = plt.contour(xx, yy, zz05, [1])
#plt.clabel(CS05, inline=1, fontsize=10)

CS0 = plt.contour(xx, yy, zz0, [1])
#plt.clabel(CS0, inline=1, fontsize=10)

CS1 = plt.contour(xx, yy, zz1, [1])
#plt.clabel(CS1, inline=1, fontsize=10)

CS2 = plt.contour(xx, yy, zz2, [1])
#plt.clabel(CS2, inline=1, fontsize=10)


#plt.legend()
plt.show()