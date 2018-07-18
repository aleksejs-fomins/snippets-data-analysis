import numpy as np
import random

# Return velocity of object A
# Object A will chase object B
def chase(posA, posB, speed):
    diff = posB - posA
    nrm = np.linalg.norm(diff)
    return speed * diff / nrm if nrm != 0 else np.array([0,0])

def drunkChase(posA, posB, speed):
    return chase(posA, posB, speed) + np.random.uniform(-5.0, 5.0, 2)

def veryDrunkChase(posA, posB, speed):
    r = random.uniform(0, 1)
    return chase(posA, posB, speed) if r>0.9 else np.random.uniform(-5.0, 5.0, 2)
