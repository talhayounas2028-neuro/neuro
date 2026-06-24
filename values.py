from brian2 import *

NUM_TRIALS = 1
sweep_values = [0.165]
coh = 15

gEEN = 0.165 * nS / 1600 * 1600
gEIN = 0.130 * nS / 1600 * 1600

N = 2000
gIE = 1.3 * nS / 400 * 400

Jp = 1.7
