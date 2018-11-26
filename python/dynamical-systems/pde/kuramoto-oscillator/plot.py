import matplotlib.pyplot as plt
from kuramoto_lib import KuramotoOscillator            

ko1 = KuramotoOscillator(0.01, 5, 1)
rez = ko1.run(1000)

plt.figure()
plt.plot(rez)
plt.show()
