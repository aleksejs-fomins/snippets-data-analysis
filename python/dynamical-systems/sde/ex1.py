import numpy as np
import sdeint
import matplotlib.pyplot as plt

a = 1.0
b = 0.8
tspan = np.linspace(0.0, 5.0, 5001)
x0 = 0.1

def f(x, t):
    return -(a + x*b**2)*(1 - x**2)

def g(x, t):
    return b*(1 - x**2)

# Try computing solution 5 times
result = [sdeint.itoint(f, g, x0, tspan) for i in range(5)]

# Plot all solutions
plt.figure()
for res in result:
  plt.plot(res)
plt.show()
