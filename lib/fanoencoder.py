import copy
import numpy as np


class fanoEncoder():
    def __init__(self, order):
        self.order = order
        self.tmpmem = ""
        self.statdict = dict()

    # Add a new character to the statistics
    # Must add characters in correct sequence, since
    # higher order predictive relationships are calculated
    def addchar(self, newchar):

        # Add the new character at the end of the window
        # and subtract the first character in the window,
        # if there is already enough characters
        self.tmpmem += newchar
        if len(self.tmpmem) > self.order:
            self.tmpmem = self.tmpmem[1:]

        # If there is enough characters in the current window,
        # increase the counter for this pattern, or start a
        # new counter
        if len(self.tmpmem) == self.order:
            if self.tmpmem in self.statdict:
                self.statdict[self.tmpmem] += 1
            else:
                self.statdict[self.tmpmem] = 1

    # Create a dictionary of occurance rates for all sequences
    def getstat(self):
        nChar = sum(self.statdict.values())
        rezdict =  {key: float(value) / nChar for key, value in self.statdict.items()}
        return sorted(rezdict.items(), key=lambda x: x[1], reverse=True)


class fanoGuesser():
    def __init__(self, order, stat):
        self.order = order
        self.stat = stat


    def guessNext(self, thisText):
        # Extract text with 1 less characters than the pretext
        preText = thisText[len(thisText) - self.order + 1:]

        # Make a sub-dictionary of all entries that start with preText and normalize it
        subKey = []
        subVal = []
        for item in self.stat:
            if item[0][:self.order-1] == preText:
                subKey.append(item[0][self.order-1])
                subVal.append(item[1])

        if len(subVal) == 0:
            raise ValueError("No keys for pretext ", preText, " found :(")

        norm = sum(subVal)
        subVal = [it / float(norm) for it in subVal]

        # Sample a random value from the sub-dict
        r1 = np.random.uniform(0.0, 1.0)
        for k,v in zip(subKey, subVal):
            r1 -= v
            if r1 <= 0.0:
                return k

        raise ValueError('WTF??')







