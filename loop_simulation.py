
import numpy as np
from crossover_logic import crossover_point, quantum_choice

def normal_loop(t, R=1.0, H=0.5, phi_offset=0):
    x = R * np.cos(t)
    y = R * np.sin(t)
    z = H * t
    w = phi_offset + np.sin(t)
    return x, y, z, w

def mirror_loop(t, R=1.0, H=0.5, phi_offset=0):
    x = R * np.cos(-t)
    y = R * np.sin(-t)
    z = H * (-t)
    w = phi_offset + np.sin(-t)
    return x, y, z, w

def simulate_big_loop(timesteps=1000):
    path = []
    for t in np.linspace(0, 2 * np.pi, timesteps):
        if crossover_point(t):
            decision = quantum_choice()
            path.append(("Crossover", t, decision))
        else:
            path.append(("Normal Progress", t))
    return path

if __name__ == "__main__":
    result = simulate_big_loop()
    for event in result:
        print(event)
