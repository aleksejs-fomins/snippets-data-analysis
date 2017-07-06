import numpy as np


class multiarray1d:
    def __init__(self, LList):

        self.LList = LList
        self.nDofTot = 0  # Total number of degrees of freedom in all propagator matrices
        self.shiftDof = [0]  # Starting index of degrees of freedom of i-th matrix

        for i in range(0, len(self.LList) - 1):
            thisDof = self.LList[i] * self.LList[i + 1]
            self.nDofTot += thisDof
            self.shiftDof.append(self.shiftDof[i] + thisDof)

        self.shiftDof.pop()             # Remove last item because there is 1 less matrix than state


    def totalDof(self):
        return self.nDofTot

    # Construct a numpy matrix from i-th block from 1d list
    def getmatrix(self, arr1d, iMat):
        if iMat >= len(self.shiftDof):
            raise ValueError("Unexpected matrix", iMat, "requested, when total is", len(self.shiftDof))
        else:
            start = self.shiftDof[iMat]
            nRow = self.LList[iMat + 1]
            nCol = self.LList[iMat]

            return np.array([
                arr1d[
                start + nCol*it:
                start + nCol*(it+1)]
                for it in range(0, nRow)
            ])

