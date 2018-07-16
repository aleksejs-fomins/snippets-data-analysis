import numpy as np

def Hstep(x):
    return 1.0 * (x >= 0)

# INTEGRATE AND FIRE NEURON IMPLEMENTATION
class IFNeuron:
    def __init__(self, R, C, Vinit, V0, VT, VE, T0, DT, AX_DT, AX_TAU_M, AX_TAU_N):
        self.MEMBRANE_R = R
        self.MEMBRANE_C = C
        self.MEMBRANE_V0 = V0
        self.MEMBRANE_VT = VT
        self.MEMBRANE_VE = VE
        self.MEMBRANE_TAU = R*C

        self.AXON_DT = AX_DT
        self.AXON_TAU_M = AX_TAU_M
        self.AXON_TAU_N = AX_TAU_N
        self.AXON_V_MAX = \
            np.power(AX_TAU_M / AX_TAU_N, -AX_TAU_N / (AX_TAU_M - AX_TAU_N)) - \
            np.power(AX_TAU_M / AX_TAU_N, -AX_TAU_M / (AX_TAU_M - AX_TAU_N))

        self.DT = DT

        self.T = T0
        self.V = Vinit
        self.T_Last_Spike = None

    def step(self, I):
        self.T += self.DT
        self.V += self.DT * (I / self.MEMBRANE_C
                             - (self.V + self.MEMBRANE_VE) / self.MEMBRANE_TAU)

        # If spike happens
        if self.V > self.MEMBRANE_VT:
            self.V = self.MEMBRANE_V0
            self.T_Last_Spike = self.T - self.DT

    def post_synaptic_I(self):
        if self.T_Last_Spike == None:
            return 0.0
        else:
            t_delay = self.T - self.T_Last_Spike + self.AXON_DT
            return 1.0 / self.AXON_V_MAX * \
                (np.exp(-t_delay / self.AXON_TAU_M)
                    - np.exp(-t_delay / self.AXON_TAU_N)) * Hstep(t_delay)

