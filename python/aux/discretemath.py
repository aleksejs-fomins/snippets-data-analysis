# Determine the smallest argument and value by value
def argmin(x, y):
    rez = [x[0], y[0]]
    for i in range(1, len(x)):
        if y[i] < rez[1]:
            rez = [x[i], y[i]]

    return rez


def list_progressive_accumulate(lst, init):
    rez = [init]
    for i in range(0, len(lst)):
        rez.append(rez[i] + lst[i])
    return rez