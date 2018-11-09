import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def polar(phi):
    return np.array([np.sin(phi), np.cos(phi)])

def wavePacket(SAMPLING_RATE, TIME, FREQ_RANGE, FREQ_STEP):
    # Discretize time
    TIME_SAMPLE_COUNT = int(TIME * SAMPLING_RATE)
    t = np.linspace(0, TIME, TIME_SAMPLE_COUNT)

    # Discretize frequency
    FREQ_SAMPLE_COUNT = int((FREQ_RANGE[1] - FREQ_RANGE[0])/FREQ_STEP)
    f_lst = np.linspace(FREQ_RANGE[0], FREQ_RANGE[1], FREQ_SAMPLE_COUNT)
    
    # Sample frequencies with gaussian weights in freq-space
    w_lst = gaussian(f_lst, (FREQ_RANGE[1]+FREQ_RANGE[0])/2, (FREQ_RANGE[1]-FREQ_RANGE[0])/5)

    x = np.zeros(len(t))

    # Sample frequencies with random phase
    for f,w in zip(f_lst, w_lst):
        phase = np.random.uniform(0, 2*np.pi)
        r = w*polar(phase)
        x += r.dot(polar(2 * np.pi * f * t))
        
    return t,x