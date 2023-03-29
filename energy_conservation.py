import numpy as np
import matplotlib.pyplot as plt
from Box import Box


time_increment = 1e-3  # time increment for each iteration
iterations = 1000  # number of iterations
times = []  # list of time values
energies = []  # list of total energy values

"""
create an instance of the Box class with time increment, number of particles, and box dimensions
"""

box = Box(time_increment, 100, 2, 2)
box.random_pos(300)  

"""
using a temeprature of 300K we are randomly settiong the initial
positions of the particles inside the box and setting their velocities 
to be in the maxwell boltzmann distribution

"""

for i in range(iterations):
    box.update_pos()  # update the positions of the particles in the box
    times.append(time_increment * i)  # add current time value to the list
    energies.append(box.total_energy())  # add current total energy value to the list

"""
plot the graph of total energy vs time
"""

plt.scatter(times, energies)
plt.xlabel("Time (s)")
plt.ylabel("Total Energy (J)")
plt.xlim(0,1)
plt.title("Total Energy vs Time at 300K for 100 Particles")
plt.show()
