import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from Box import Box


time_increment = 1e-3
iterations = 1000
times = []
momenta = []

box = Box(time_increment, 20, 2, 2)
box.random_pos(300)

for i in range(iterations):
    # box.update_pos()
    times.append(time_increment * i)
    momenta.append(box.total_momentum())


plt.scatter(times, momenta)
plt.xlabel("Time (s)")
plt.ylabel("Total Momentum (Kg*m*s^-2)")
plt.xlim(0,1)
plt.title("Total Momentum vs Time at 300K")
plt.show()