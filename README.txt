Particle.py
This file contains the Particle class used in the main simulation in order for the simulation to work this file must be 
kept in the same folder as the Box.py file and the main.py file.

Box.py
This file contains the Box class which includes generating random positions for the particle within the parameters of the Box and 
contains all of the equations coded wioth algorithms used to simulate physics. Including the velocity of the particles based on
Maxwell Boltzmann distributions, total energy of the system, total momemntum and the collision detection algorithms.

Box_test.py
This is a unit test file that contains tests for all the algorithms in the Box.py file

Particle_test.py
This is a unit test file that contains tests for all the algorithms in the Particle.py file

energy_conservation.py
This file contains the graphing code to create a plot of total energy of the system over the run time of the simulation 

velocity_distribution.py
This file contains the graphing code to create a histogram of velocities for a specific temperature to model the Maxwell-Bolzmann distribution

momentum_conservation.py
This file contains the graphing code to create a plot of the total momentum of the system over the run time of the simulation

main.py 
This file will allow the user to run an animation of the simulation in real time. You can adjust the number of particles in the simulation
and the temperature of the environment.