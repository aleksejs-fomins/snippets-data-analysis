import numpy as np
import matplotlib.pyplot as plt

def cluster_centroids(data, labels, k):
    """Return centroids of clusters in data.

    data is an array of observations with shape (A, B, ...).

    labels is an array of integers of shape (A,) giving the index
    (from 0 to k-1) of the cluster to which each observation belongs.
    The clusters must all be non-empty.

    k is the number of clusters.

    The result is an array of shape (k, B, ...) containing the
    centroid of each cluster.
    """
    result = np.empty(shape=(k,) + data.shape[1:])
    for i in range(k):
        np.mean(data[labels == i], axis=0, out=result[i])
    return result

def kmeans(data, initial_centroids, steps=20):
    """Divide the observations in data into clusters using the k-means
    algorithm, and return an array of integers assigning each data
    point to one of the clusters.

    """
    centroids = initial_centroids
    k = len(initial_centroids)
    for _ in range(steps):
        # Squared distances between each point and each centroid.
        dists = np.zeros((k, data.shape[0]))
        for c, centroid in enumerate(centroids):
            dists[c, :] = np.sqrt(np.sum((data - centroid)**2, axis=1))

        # Index of the closest centroid to each data point.
        clusters = np.argmin(dists, axis=0)

        new_centroids = cluster_centroids(data, clusters, k)

        centroids = new_centroids

    return clusters, centroids

def evaluate(data, labels, initial_centroids, steps=20, plot=False):
    """
    Use the k-means algorithm to cluster the given labeled data, using
    the provided centroids in the first step.
    
    Returns the fraction of correctly classified points. Optionally
    plots the data and clustering (should only be used for small data
    sets).
    """
    clusters, centroids = kmeans(data, initial_centroids, steps=steps)
    assert len(clusters) == len(labels)
    correct = np.sum(clusters == labels) / (1.0*len(clusters))
    if plot:
        plt.scatter(data[:, 0], data[:, 1], c=labels)
        plt.plot(centroids[:, 0], centroids[:, 1], 'rx', ms=10, mew=2)
        if correct < 1:
            # show wrongly classified points
            wrong_points = data[clusters != labels, :]
            plt.scatter(wrong_points[:, 0], wrong_points[:, 1], marker='o',
                        facecolor='none', edgecolors='red', linewidths=1)
    return correct
