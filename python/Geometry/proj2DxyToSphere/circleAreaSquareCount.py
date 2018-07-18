import numpy as np
import matplotlib.pyplot as plt
from noRoundoffSum import msum


# Check if point projects or misses
def is2DinR(R, p2D):
    return p2D[0] ** 2 + p2D[1] ** 2 <= R

R = 1.0
realAreaRatio = np.pi * R**2 / (4 * R**2)

nPoint1DList = list(range(20, 2000, 200))
circleSizeRelError = []

for nPoint1D in nPoint1DList:
    print(nPoint1D)

    dl = 2 * R / (nPoint1D - 1)
    mesh1D = np.arange(-R, R, dl)

    inCount = 0
    totCount = len(mesh1D)**2

    for x in mesh1D:
        for y in mesh1D:

            # Take this point on the mesh and other 3 points that make a square
            points2D = [
                np.array([x, y]),
                np.array([x, y + dl]),
                np.array([x + dl, y]),
                np.array([x + dl, y + dl])
            ]

            # All points that are on the sphere are projected on it
            inCountLocal = 0
            for p2D in points2D:
                if is2DinR(R, p2D):
                    inCountLocal+=1

            if inCountLocal == 3:
                inCount += 1
            elif inCountLocal == 4:
                inCount += 2

    circleSizeRelError.append(inCount/totCount/2/realAreaRatio - 1)

plt.semilogy(nPoint1DList, np.fabs(np.array(circleSizeRelError)))
plt.show()
