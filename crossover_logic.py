
import numpy as np
import random

from loop_simulation import normal_loop, mirror_loop

def crossover_point(t, threshold=0.1):
    x1, y1, z1, w1 = normal_loop(t)
    x2, y2, z2, w2 = mirror_loop(t)
    distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2 + (w1 - w2)**2)
    return distance < threshold

def quantum_choice():
    return random.choice(["forward", "backward", "mirror_jump"])
