import numpy as np


def sample_metropolis_hastings(f, p, x0, N):
    '''

    :param f:   Probability distribution to sample
    :param p:   Sampling function which generates next random sampling point based on previous
    :param x0:  Starting position
    :param N:   Number of samples
    :return:    Markov chain: a tuple of sampled coordinates and function values
    '''

    x_arr = np.zeros((N, len(x0)))
    y_arr = np.zeros(N)
    x_arr[0] = x0
    y_arr[0] = f(x0)
    for i in range(1, N):
        x_arr[i] = p(x_arr[i-1])
        y_arr[i] = f(x_arr[i])
        alpha = y_arr[i] / y_arr[i-1]
        if (alpha < 1) and (np.random.uniform(0, 1) > alpha):
            x_arr[i] = x_arr[i-1]
            y_arr[i] = y_arr[i-1]
    return x_arr, y_arr