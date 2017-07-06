import numpy as np
from aan import multiarray1d

class AAN:
    def __init__(self, LList):
        self.nMat = len(LList) - 1
        self.marr = multiarray1d.multiarray1d(LList)

        # ASSUMPTION 1: In the initial state all connections have weight 1
        self.dof = [1.0] * self.marr.totalDof()

        # ASSUMPTION 2: The smoothness of the sigmoid function
        self.sigmoidEPS = 1.0

        # print(self.marr.getmatrix(self.dof, 0))
        # print(self.marr.getmatrix(self.dof, 1))
        # print(self.eval(self.dof, [2]))


    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-self.sigmoidEPS * x))


    # Propagate input through the network
    def eval(self, dofTmp, dataIn):
        stateThis = np.array(dataIn)
        for i in range(0, self.nMat):
            stateNext = self.marr.getmatrix(dofTmp, i).dot(stateThis)
            stateThis = self.sigmoid(stateNext) if i < self.nMat-1 else stateNext

        return stateThis


    # Evaluate the L2 error between propagated input data and expected output data
    def L2(self, dofTmp, dataIn, dataOut):
        return np.linalg.norm(dataOut - self.eval(dofTmp, dataIn))


    def L2deriv(self, dataIn, dataOut, dofTmp):
        print('impl me :)')

    def optimize(self, dataIn, dataOut):
        print('impl me :)')