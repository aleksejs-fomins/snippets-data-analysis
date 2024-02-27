import numpy as np
from lib.stat import infotheory_sample, randstat
from lib.machine_learning import fanoencoder

randstat.init()

for ord in range(1, 7):
    FEC = fanoencoder.fanoEncoder(ord)

    for line in open('/home/aleksejs/Downloads/aliceW.txt'):
        for ch in line:
            FEC.addchar(ch)

    stat = FEC.getstat()
    entropy = infotheory_sample.shannonEntropy1Dbin([1] * len(stat), [it[1] for it in stat])

    print(len(stat), entropy)

    #print(stat[0], stat[1], stat[2])

    FG = fanoencoder.fanoGuesser(ord, stat)
    thisText = stat[int(np.random.uniform(1, len(stat)-1))][0]

    for i in range(0, 500):
        thisText += FG.guessNext(thisText)

    print('Composer', ord, 'wrote::: ', thisText)
    print('=====================================')
