def list_progressive_accumulate(lst, init):
    rez = [init]
    for i in range(0, len(lst)):
        rez.append(rez[i] + lst[i])
    return rez

