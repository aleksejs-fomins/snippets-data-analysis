class TreeOfTrees():
    def __init__(self):
        self.tree = {}

    def add(self, seq):
        current_leaf = self.tree
        for char in seq:
            if char in current_leaf.keys():
                ref = current_leaf[char]
                ref[0] += 1
                current_leaf = ref[1]  # TODO: Make sure this is a reference-copy
            else:
                current_leaf[char] = [1, {}]
                current_leaf = current_leaf[char][1]  # TODO: Make sure this is a reference-copy

    def get_node(self, seq):
        current_leaf = self.tree
        for char in seq:
            if char in current_leaf.keys():
                current_leaf = current_leaf[char][1]  # TODO: Make sure this is a reference-copy
            else:
                raise ValueError("Failed sequence", seq, "on char", char)

    def sub_dict(self, lvl, subdict):
        if lvl == 0:
            return {key:val[0] for key,val in subdict.items()}
        else:
            rezdict = {}
            for key, val in subdict.items():
                nextsubdict = self.sub_dict(lvl-1, val[1])
                rezdict = {**rezdict, **nextsubdict} ## Merge two dicts

            return rezdict


import numpy as np
from datetime import datetime

# Init Random Seed
import random
random.seed(datetime.now())
np.random.seed(datetime.now().toordinal())

# Initialize Constants
SOURCE_TEXT_FILE = '/home/aleksejs/Downloads/aliceW.txt'
CORRELATION_ORDER_START = 1
CORRELATION_ORDER_END = 6
OUTPUT_TEXT_LENGTH_CHAR = 500


# OPTIONAL: Calculate Shannon entropy of a discrete probability distribution
def shannonEntropy1Dbin(pdfWidth, pdfHeight):
    rez = 0
    for w,h in zip(pdfWidth, pdfHeight):
        if h > 0:
            rez -= w * h * np.log2(h)

    return rez


print('==================================================================')
print('...Performing text frequency analysis of character order up to', CORRELATION_ORDER_END)

# Add a new character to the statistics
# Must add characters in correct sequence, since
# higher order predictive relationships are calculated
Tree1 = TreeOfTrees()
text_window = ""
for line in open(SOURCE_TEXT_FILE):
    for newchar in line:
        # Add the new character at the end of the window
        # and subtract the first character in the window,
        # if there is already enough characters
        if len(text_window) < CORRELATION_ORDER_END:
            text_window += newchar
        else:
            text_window = text_window[1:] + newchar

        # If there is enough characters in the current window,
        # increase the counter for this pattern, or start a
        # new counter
        if len(text_window) == CORRELATION_ORDER_END:
            Tree1.add(text_window)


# Loop over different correlation orders
for ord in range(CORRELATION_ORDER_START, CORRELATION_ORDER_END+1):
    # Normalize dictionary values to get frequency of each pattern
    statdict = Tree1.sub_dict(ord, Tree1.tree)
    nChars = sum(statdict.values())
    nPatterns = len(statdict.values())
    statdict = {key: float(value) / nChars for key, value in statdict.items()}

    # Get list of pairs pattern:frequency, sorted by frequency in descending order
    stattuplelist = sorted(statdict.items(), key=lambda x: x[1], reverse=True)

    print(Tree1.tree)

    # OPTIONAL: Calculate Shannon Entropy of the entire language represented by the provided text
    entropy = shannonEntropy1Dbin([1] * nPatterns, [it[1] for it in stattuplelist])

    print("Finished: at character order", ord, "the number of patterns is", nPatterns, ". The Shannon entropy of language (per character) is", entropy / ord)
    print('------ Composer', ord, 'will now write text of', OUTPUT_TEXT_LENGTH_CHAR, 'characters below -----')


    # Initialise composed text using any randomly selected available pattern
    thisText = stattuplelist[int(np.random.uniform(1, nPatterns-1))][0]
    text_window = thisText

    # Generate each new character randomly by analysing pattern frequencies
    for i in range(1, OUTPUT_TEXT_LENGTH_CHAR):
        # Make a sub-dictionary of all entries that start with preText and normalize it
        subKey = []
        subVal = []
        for item in stattuplelist:
            # If the end of textwindow matches the beginning of this pattern
            # Then add the last letter of this pattern as candidate
            if item[0][:-1] == text_window[1:]:
                subKey.append(item[0][ord-1])
                subVal.append(item[1])

        # Check if there is at least one candidate, otherwise crash
        if len(subVal) == 0:
            raise ValueError("No ways to continue the current text window '", text_window, "' found :(")

        # Normalize the frequencies of sub-selected patterns
        norm = sum(subVal)
        subVal = [it / float(norm) for it in subVal]

        # Select a random pattern from those available for sub-selection
        # Note that the probabilities of patterns are not equal
        # Thus, we have to roll a random number, and add probabilities of patterns until we have more than the rolled number
        # For more info, google "Non-uniform random numbers using Cumulative Distribution Function"
        r1 = np.random.uniform(0.0, 1.0)
        j = 0
        while r1 > 0.0:
            r1 -= subVal[j]
            j += 1

        thisText += subKey[j-1]
        text_window = text_window[1:] + subKey[j-1]

    print(thisText)

