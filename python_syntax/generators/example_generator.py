
# Not allowed to touch this function
def myGen():
    for i in range(5):
        for j in range(5):
            yield i, j

# Not allowed to touch this function
sq = lambda i, j: i**2 + j**2

# Everything below here can be edited
proxy_sq = lambda t: sq(t[0], t[1])
m = map(proxy_sq, myGen())
print(list(m))