import time

import matplotlib.pyplot as plt

from lib import parallel

#nCore = multiprocessing.cpu_count()

nCore = [1, 2, 3, 4, 5, 6, 7]
nTask = [1 + i ** 2 * 1000 for i in range(1, 20)]
nTime = [[] for i in range(0, len(nCore) + 1)]

print(nTime)


for iReal in nTask:
    print('TaskSize', iReal)
    start = time.time()
    rez = parallel.serial_series((parallel.numeric_time_killer1, 1, iReal))
    end = time.time()
    nTime[0].append(end - start)
    #print('Serial Result', rez)


    for iCore in range(0, len(nCore)):
        start = time.time()
        rez = parallel.parallel_series((parallel.numeric_time_killer1, 1, iReal, nCore[iCore]))
        end = time.time()
        nTime[iCore + 1].append(end - start)
        #print('NCore', nCore[iCore], 'Result', rez)

    #print(nTime[0])

for iCore in range(0, len(nCore) + 1):
    plt.plot(nTask, nTime[iCore])

plt.legend(['serial'] + [str(i) for i in nCore])
plt.show()