from lib.numerics import metrics


# Enumerate to list of lists
def listenum(x):
    return [list(it) for it in enumerate(x)]

# Determine the key and value of dict element with largest value
def dictMax(d):
    maxk = 0
    maxv = 0
    for key, val in d.items():
        if val > maxv:
            maxk = key
            maxv = val

    return maxk, maxv


# The k-nearest-neighbor algorithm
# Find n nearest neighbors of point p from vList
# and do a majority vote on color of p based on neighbor colors
def knn(vList, colors, p, n):
    # Find the sorted list of distances from point p to all other vertices
    dListEnumerated = listenum(metrics.dist_l2_mat_vec(vList, p))
    dSort = sorted(dListEnumerated, key=lambda x: x[1])

    # Find the n nearest neighbor colors, disregarding actual distances
    cList = [colors[it[0]] for it in dSort[:n]]

    # Determine the number of votes for each color by constructing a dict
    d = {}
    for c in cList:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1

    # Determine the majority vote color
    maxk, maxv = dictMax(d)
    print('Color ', maxk, ' wins with', maxv, 'votes')

    return maxk


# Potential field classifier
# Find distances to all points, and compute average electric field
# a set of unit charges of each color would exhibit on the test unit charge
# Choose the one with greatest field
def maxEField(vList, colors, p):
    # Find the sorted list of distances from point p to all other vertices
    dListEnumerated = listenum(metrics.dist_l2_mat_vec(vList, p))
    dListColored = [[colors[it[0]], it[1]] for it in dListEnumerated]


    # Find the n nearest neighbor colors, disregarding actual distances
    d = {}
    for it in dListColored:
        Ethis = 1.0 / (it[1] ** 2)

        if it[0] in d:
            d[it[0]][0] += 1
            d[it[0]][1] += Ethis
        else:
            d[it[0]] = [1, Ethis]

    dNormKey = list(d.keys())
    dNormVal = [val[1] / val[0] for val in d.values()]

    # Determine the majority vote color
    maxk, maxv = argmax(dNormKey, dNormVal)
    print('Color ', maxk, ' wins with', maxv, 'field magnitude')

    return maxk



