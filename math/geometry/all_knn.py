import numpy as np
import matplotlib.pyplot as plt


# Order (N^2) algorithm
def all_knn_brutal(data, k):
    nPoint, nDim = data.shape

    M3D = np.einsum('i, jk', np.ones(nPoint), data)

    diff = M3D - M3D.transpose((1,0,2))
    dist = np.linalg.norm(diff, axis=2)
    rez = [np.sort(d)[1:k+1] for d in dist]
    return np.array(rez)




dataThis = np.random.uniform(0, 1, (1000, 3))

knn2 = all_knn_brutal(dataThis, 2)

plt.figure()
plt.hist(knn2[:, 0], bins="auto", alpha=0.5, label='1')
plt.hist(knn2[:, 1], bins="auto", alpha=0.5, label='2')
plt.legend()
plt.show()
