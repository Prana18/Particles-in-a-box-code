import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Box import Box
from Particle import Particle

"""
Simulating particles moving in a box using the Box and Particle and the animation feature of Matplotlib.

Classes:
    Box: Represents the box containing the particles.
    Particle: Represents a single particle in the box.
"""


box = Box(1e-3, 10, 2, 2) 
box.random_pos()
box.maxwell_boltzmann_velocities(50)

"""
a box is created with the parameters listed above and the particles
are all given a random position within the box and all given 
Maxwell-Boltzmann velocities
"""

fig, axis = plt.subplots()

x=[]
y=[]
colors=[]
for i in range(box.number_of_particles):
    x.append(box.particles[i].position[0])
    y.append(box.particles[i].position[1])
    if i == 0:  # set the color of the first particle to green
        colors.append('green')
    else:
        colors.append('red')

scatter = axis.scatter(x, y, s=35, c=colors)

"""
x is a list containing the x-coordinates of the particles' positions.
y is a list containing the y-coordinates of the particles' positions.
colors is a list containing the colors of the particles in the scatter plot
"""

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-box.width, box.width)
plt.ylim(-box.height, box.height)
plt.title("Particles in a Box Simulation")

def plot(frame): #Updates the positions of the particles and updates the scatter plot accordingly.
    for i in range(1):
        box.update_pos()
    positions=[]
    for i in range(box.number_of_particles):
        positions.append(box.particles[i].position)
    scatter.set_offsets(positions)
    # set the color of the first particle to green
    colors[0] = 'green'
    scatter.set_color(colors)

animation = FuncAnimation(fig, func=plot, interval=10, frames=1000)

"""
The animation feature of matplotlib simulates the particles moving in real time

"""
plt.show()











