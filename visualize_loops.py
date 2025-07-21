
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from loop_simulation import normal_loop, mirror_loop

timesteps = 500
t_values = np.linspace(0, 2 * np.pi, timesteps)

normal_coords = [normal_loop(t) for t in t_values]
mirror_coords = [mirror_loop(t) for t in t_values]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot Normal Loop
x, y, z, _ = zip(*normal_coords)
ax.plot(x, y, z, label="Normal Loop", color="blue")

# Plot Mirror Loop
x_m, y_m, z_m, _ = zip(*mirror_coords)
ax.plot(x_m, y_m, z_m, label="Mirror Loop", color="red")

ax.legend()
plt.show()
