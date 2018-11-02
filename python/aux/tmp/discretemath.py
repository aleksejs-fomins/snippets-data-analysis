# Determine the smallest argument and value by value
def argmin(x, y):
    rez = [x[0], y[0]]
    for i in range(1, len(x)):
        if y[i] < rez[1]:
            rez = [x[i], y[i]]

    return rez


def argmax(x, y):

    print(x, y)
    rez = [x[0], y[0]]
    for i in range(1, len(x)):
        if y[i] > rez[1]:
            rez = [x[i], y[i]]

    return rez



def list_progressive_accumulate(lst, init):
    rez = [init]
    for i in range(0, len(lst)):
        rez.append(rez[i] + lst[i])
    return rez


# Zip to list of lists
def listzip(x, y):
    return [list(it) for it in zip(x, y)]


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
