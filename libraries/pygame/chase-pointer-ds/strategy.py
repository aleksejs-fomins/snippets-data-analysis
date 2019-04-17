import numpy as np
import random

# Return velocity of object A
# Object A will chase object B

# x2'' = w2 * (x1 - x2)
def update(x1, x2, p):
  k,m,dt = p['k'], p['m'], p['dt']
  w2 = k / m
  alpha = w2 * dt**2
  return 2*x2[-1] - x2[-2] + alpha * (x1[-1] - x2[-1])
   
# x2'' = w2 * (x1 - x2) - g * w * x2'
def update2(x1, x2, p):
  k,m,g,dt = p['k'], p['m'], p['g'], p['dt']
  w2 = k / m
  w = np.sqrt(w2)
  alpha = w2 * dt**2
  beta = g * w * dt / 2
  return (2*x2[-1] - x2[-2] - beta*x2[-2] + alpha * (x1[-1] - x2[-1])) / (1 - beta)

# x2'' = w2 * (x1 - x2) - g * w * x2' + w * x1'
def update3(x1, x2, p):
  k,m,g,dt = p['k'], p['m'], p['g'], p['dt']
  w2 = k / m
  w = np.sqrt(w2)
  alpha = w2 * dt**2
  beta = g * w * dt / 2
  gamma = w * dt
  return (2*x2[-1] - x2[-2] - beta*x2[-2] + alpha * (x1[-1] - x2[-1]) + gamma*(x1[-1] - x1[-2])) / (1 - beta)


# x2'' = x1'' + w2 * (x1 - x2) - g * w * x2'
def update4(x1, x2, p):
  k,m,g,dt = p['k'], p['m'], p['g'], p['dt']
  w2 = k / m
  w = np.sqrt(w2)
  alpha = w2 * dt**2
  beta = g * w * dt / 2
  ddx1 = x1[-1] - 2*x1[-2] + x1[-3]
  return (2*x2[-1] - x2[-2] + ddx1 - beta*x2[-2] + alpha * (x1[-2] - x2[-1])) / (1 - beta)
