import numpy as np
from collections import deque

class Labyrinth2D:
    def __init__(self, labShape=(20, 10), probwall=0.3):
        ###########################
        # Generate Labyrinth
        ###########################
        self.lab = np.random.uniform(0, 1, labShape) < probwall
        self.p0 = (
            np.random.randint(0, labShape[0]),
            np.random.randint(0, labShape[1]))
        self.pf = (
            np.random.randint(0, labShape[0]),
            np.random.randint(0, labShape[1]))

        # Source and target may not be walls
        self.lab[self.p0] = 0
        self.lab[self.pf] = 0

        # shortest distance from source
        self.distance = np.nan * np.ones(self.lab.shape)

        self.allowedMoves = [
            np.array([-1, 0]),
            np.array([1, 0]),
            np.array([0, -1]),
            np.array([0, 1])]
        
    def is_move_valid(self, p):
        left = p[0] >= 0
        top = p[1] >=0 
        right = p[0] < self.lab.shape[0]
        bottom = p[1] < self.lab.shape[1]
        return left and right and top and bottom and (self.lab[p] == 0)

    def make_move(self, p, step):
        return tuple(np.array(p) + step)
    
    # Check if target accessible using BFS
    def solve_bfs(self):
        self.distance = np.nan * np.ones(self.lab.shape)
        tasks = deque([(self.p0, 0)])

        while len(tasks) > 0:
            p,d = tasks.popleft()
            if self.is_move_valid(p) and np.isnan(self.distance[p]):
                self.distance[p] = d
                for step in self.allowedMoves:
                    tasks.append((self.make_move(p, step), d+1))

        if np.isnan(self.distance[self.pf]):
            print("Target inaccessible from source")
        else:
            print("Target accessible using at least", self.distance[self.pf], "steps")

    def plot_value(self, ax, density=None):
        if density is None:
            density = self.distance
            ax.imshow(self.lab, cmap='jet')
            title = "Red is wall. White dot start. White cross finish. Blue inaccessible. Shade of yellow determines distance"
        else:
            title = "Value function"

        ax.set_title(title)
        ax.imshow(density)
        ax.plot([self.p0[1]], [self.p0[0]], 'o', color='white')
        ax.plot([self.pf[1]], [self.pf[0]], 'x', color='white')

    def plot_result(self, ax, rewardTimes):
        rewardDelta = [rewardTimes[i] - rewardTimes[i - 1] for i in range(1, len(rewardTimes))]
        ax.loglog(np.arange(1, len(rewardDelta) + 1), rewardDelta)
        ax.set_ylim([1, 1.1 * np.max(rewardDelta)])
        ax.set_title("Moves to goal")
        ax.set_xlabel("Trial number")
