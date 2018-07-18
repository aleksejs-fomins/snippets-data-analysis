import numpy as np
import matplotlib.pyplot as plt
from noRoundoffSum import msum

# Check if point projects or misses
def is2DinR(R, p2D):
    return p2D[0]**2 + p2D[1]**2 <= R

def project2DtoSphere(R, p2D):
    return np.array([p2D[0], p2D[1], np.sqrt(R**2 - p2D[0]**2 - p2D[1]**2)])

# Calculate area of 3D triangle using vector multiplication
def triangleArea3D(plist3D):
    v1 = plist3D[1] - plist3D[0]
    v2 = plist3D[2] - plist3D[0]

    rez = np.linalg.norm(np.array([
                v1[1] * v2[2] - v1[2] * v2[1],
                v1[2] * v2[0] - v1[0] * v2[2],
                v1[0] * v2[1] - v1[1] * v2[0],
            ]
        )
    ) / 2.0

    return rez


R = 1.0
realHemisphereArea = (4 * np.pi * R**2) / 2

nPoint1DList = list(range(20, 2000, 200))
relErrorSquares = []
relErrorTriangles = []

for nPoint1D in nPoint1DList:
    dl = 2*R / (nPoint1D-1)
    mesh1D = np.arange(-R, R, dl)

    partialAreasTriangles = []
    partialAreasSquares = []
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
            points3D = [project2DtoSphere(R, p2D) for p2D in points2D if is2DinR(R, p2D)]

            if len(points3D) == 3:
                thisArea = triangleArea3D(points3D)
                partialAreasTriangles.append(thisArea)
            elif len(points3D) == 4:
                thisArea = triangleArea3D(points3D[0:3]) + triangleArea3D(points3D[1:4])
                partialAreasTriangles.append(thisArea)
                partialAreasSquares.append(thisArea)

    relErrorSquares.append(np.fabs(msum(partialAreasSquares) / realHemisphereArea - 1))
    relErrorTriangles.append(np.fabs(msum(partialAreasTriangles) / realHemisphereArea - 1))
    print(nPoint1D)

plt.semilogy(nPoint1DList, relErrorSquares, label="squares only")
plt.semilogy(nPoint1DList, relErrorTriangles, label="squares and triangles")
plt.legend()
plt.show()


