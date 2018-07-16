import numpy as np

def shannonEntropy1Dbin(pdfWidth, pdfHeight):
    rez = 0
    for w,h in zip(pdfWidth, pdfHeight):
        if h > 0:
            rez -= w * h * np.log2(h)

    return rez

