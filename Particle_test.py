import unittest
import numpy as np
from Particle import Particle

class TestParticle(unittest.TestCase):

    def setUp(self):
        self.particle = Particle(
            id=1,
            position=np.array([0, 0], dtype=float),
            velocity=np.array([1, 1], dtype=float),
            radius=5E-2,
            mass=1.0,
            colour="red",
            gradient=1
        )

    def test_setVelocity(self):
        self.particle.setVelocity(2, 3)
        #check whether the class is Particle class is calling attributes correctly
        np.testing.assert_array_equal(self.particle.velocity, np.array([2, 3]))

    def test_setPosition(self):
        #check whether the Particle class is calling attributes correctly
        self.particle.setPosition(4, 5)
        np.testing.assert_array_equal(self.particle.position, np.array([4, 5]))




