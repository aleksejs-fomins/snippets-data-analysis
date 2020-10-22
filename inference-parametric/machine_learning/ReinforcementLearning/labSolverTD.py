import numpy as np

class LabyrinthSolverTD:
    def __init__(self, labClass, alpha = 0.1, R0 = 1, gamma = 0.9):
        '''
        lab    : labyrinth class
        alpha  : Learning rate
        R0     : Max reward
        gamma  : Discount factor
        '''
        
        self.labClass = labClass
        self.alpha = alpha
        self.R0 = R0
        self.gamma = gamma

        # Value function - determines how good it is to be in each state
        self.value = np.zeros(labClass.lab.shape)

        # Counts the number of steps necessary to reach goal for each trial
        self.rewardTimes = []

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
    
    def solve(self, maxMoves=50000):
        p0, pf = self.labClass.p0, self.labClass.pf
        
        pold, p = p0, pf
        self.rewardTimes = []
        for iStep in range(maxMoves):
            pnew = self.policy_move(p, pold)
            rewardThis = self.R0 * int(p == pf)
            self.value[p] += self.alpha*(rewardThis + self.gamma * self.value[pnew] - self.value[p])
            if rewardThis > 0:
                self.rewardTimes += [iStep]
                pold, p = p0, p0
            else:
                pold, p = p, pnew
        return self.value, self.rewardTimes
