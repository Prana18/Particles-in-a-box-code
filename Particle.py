import numpy as np

"""
Creating a particles class with the listed
attributes above.

"""

class Particle:
    def __init__( 
            self,
            id=0,
            position=np.array([0, 0], dtype=float),
            velocity=np.array([0, 0], dtype=float),
            radius=5E-2,
            mass=5e-26,
            colour="red",
            gradient = 1
    ):
            self.id = id
            self.position = np.array(position, dtype=float)
            self.velocity = np.array(velocity, dtype=float)
            self.radius = radius
            self.mass = mass
            self.colour = colour
            self.gradient = gradient


    def setVelocity(self, x, y):
        self.velocity[0] = x
        self.velocity[1] = y
        pass

    def setPosition(self, x, y):
        self.position[0] = x
        self.position[1] = y
        pass


    