import numpy as np

class BasicHippoCycle():

    def __init__(self, n):
        self.mat = np.zeros((n,n), dtype=np.float)


    def learn(self, v):
        if (len(v.shape) != 1) and (v.shape[0] != self.mat.shape[0]):
            raise ValueError("Unexpected input vector shape", v.shape)




# aaa = BasicHippoCycle(3)
# aaa.learn(1)