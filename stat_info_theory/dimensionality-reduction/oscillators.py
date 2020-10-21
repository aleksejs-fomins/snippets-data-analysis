import numpy as np


# Oscillators connected sequentially with same weights
def generate_oscillators_line(n, t):
    K = np.zeros((n,n))
    for i in range(1, n):
        K[i, i-1] = 1
    return generate_oscillators(n, t, K)
        
        
# All-to-all springs
def generate_oscillators_random(n, t):
    K = np.random.uniform(0, 1, (n,n))
    return generate_oscillators(n, t, K)


def generate_oscillators(n, t, K):
    dt = 0.01

    K = (K + K.T) / 2
    np.fill_diagonal(K, 0)
    np.fill_diagonal(K, -np.sum(K, axis=1))
    x = np.random.uniform(0, 1, (n, t))
    x[:, 0] -= np.mean(x[:, 0])
    x[:, 1] = x[:, 0] + np.random.uniform(-1, 1, n) * dt
    x[:, 1] -= np.mean(x[:, 1])
    for i in range(2, t):
        x[:, i] = 2*x[:, i-1] - x[:, i-2] + K.dot(x[:, i-1]) * dt**2
    return x