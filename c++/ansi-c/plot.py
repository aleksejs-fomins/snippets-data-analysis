import numpy as np
import matplotlib.pyplot as plt

with open("log.txt", "r") as f:
    lines = f.readlines();

lines = [l.strip().split(' ') for l in lines]
data = [[float(d) for d in line] for line in lines]


plt.figure()

for i in range(len(data)):
    plt.hist(data[i], bins='auto', alpha=0.5, label=str(i+1))

plt.legend()
plt.show()
