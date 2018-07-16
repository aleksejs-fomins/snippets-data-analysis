def avg(v):
    return sum(v) / len(v)

def sig2(v, v0):
    return sum((v-v0)**2) / (len(v)-1)
