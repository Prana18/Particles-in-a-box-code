import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from Box import Box
from Particle import Particle

box = Box(1e-3, 300, 2, 2) 
box.random_pos()

# Set initial temperature and define Boltzmann constant
initial_temperature = 30
boltzmann_constant = 1.380649e-23  # J/K

# Set velocities using Maxwell-Boltzmann distribution for the initial temperature
box.maxwell_boltzmann_velocities(initial_temperature)

# Plot velocity distribution
fig, ax = plt.subplots()
speeds = box.velocity_distribution()
ax.hist(speeds, bins=50, alpha=0.5, color = 'blue', label=f'T = {initial_temperature} K')
ax.set_xlabel('Particle Speed (m/s)')
ax.set_ylabel('Frequency')
plt.xlim(0,500)
ax.set_title('Velocity Distribution at T = 30 K')
ax.legend()

"""
Plotting a histogram of particle velocities at a specific temperature

"""

plt.show()




