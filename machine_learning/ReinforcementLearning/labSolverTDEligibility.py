import numpy as np

class LabyrinthSolverTDEligibility:
    def __init__(self, labClass, alpha = 0.1, R0 = 1, gammaET = 0.5):
        '''
        lab    : labyrinth class
        alpha  : Learning rate
        R0     : Max reward
        gammaET  : Discount factor for eligibility trace
        '''
        
        self.labClass = labClass
        self.labShape = labClass.lab.shape
        self.alpha = alpha
        self.R0 = R0
        self.gammaET = gammaET

        # Value function - determines how good it is to be in each state
        self.value = np.zeros(self.labShape)

        # Counts the number of steps necessary to reach goal for each trial
        self.rewardTimes = []

        # Track how long ago we were in each state
        self.eligibilityTrace = np.zeros(self.labShape)

    # Policy - determines probability of choosing this state, given its value
    def calc_p_move(self, pnew, p, pold):
        if not self.labClass.is_move_valid(pnew):
            return 0

        valueGain = self.value[pnew] - self.value[p]
        if pnew == pold:
            return np.exp(valueGain)  # Strongly disincentivize walking backwards
        else:
            return np.exp(10*valueGain)

    # choose direction by softmax of values
    def policy_move(self, p, pold):
        moves = [self.labClass.make_move(p, step) for step in self.labClass.allowedMoves]
        prob = np.array([self.calc_p_move(pnew, p, pold) for pnew in moves])
        prob /= np.sum(prob)
        moveidx = np.random.choice(4, p=prob)
        return moves[moveidx]
    
    def solve(self, maxMoves=50000, updateVisited=True):
        p0, pf = self.labClass.p0, self.labClass.pf
        
        pold, p = p0, pf
        self.rewardTimes = []
        for iStep in range(maxMoves):
            pnew = self.policy_move(p, pold)

            rewardThis = self.R0 * int(p == pf)
            if rewardThis > 0:
                # Update only the cells that we have visited this run
                if updateVisited:
                    idxUpdate = self.eligibilityTrace > 0
                else:
                    idxUpdate = np.ones(len(self.value)).astype(bool)
                
                idxVisited = self.eligibilityTrace > 0
                self.value[idxUpdate] = (1 - self.alpha) * self.value[idxUpdate] \
                                           + self.alpha * rewardThis * self.eligibilityTrace[idxUpdate]

                # Reset trace for each trial
                self.eligibilityTrace = np.zeros(self.labShape)
                self.rewardTimes += [iStep]
                pold, p = p0, p0
            else:
                # Update eligibility trace afterwards, so we don't assign value to the goal state
                self.eligibilityTrace *= self.gammaET
                self.eligibilityTrace[pnew] = 1

                pold, p = p, pnew
        return self.value, self.rewardTimes
