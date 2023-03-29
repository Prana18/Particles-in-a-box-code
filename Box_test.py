import unittest
import numpy as np
from Box import Box
from Particle import Particle


class TestBox(unittest.TestCase):

    def setUp(self):
        self.box = Box(time_increment=1e-5, number_of_particles=10, width=5, height=5)
        self.box.random_pos()

    def test_wall_collisions_top_wall(self):
        for particle in self.box.particles:
            # Set particle position to the centre-top of the box
            particle.setPosition(0, self.box.height)
            # Set particle velocity to point towards the wall
            particle.setVelocity(0, 1)

        self.box.wall_collisions()

        # Check that particle velocity is reversed in the correct direction
        for particle in self.box.particles:
            np.testing.assert_array_equal(particle.velocity, np.array([0, -1]))

    def test_wall_collisions_bottom_wall(self):
        for particle in self.box.particles:
            # Set particle position to the centre-bottom of the box
            particle.setPosition(0, -self.box.height)
            # Set particle velocity to point towards the wall
            particle.setVelocity(0, -1)

        self.box.wall_collisions()

        # Check that particle velocity is reversed in the correct direction
        for particle in self.box.particles:
            np.testing.assert_array_equal(particle.velocity, np.array([0, 1]))

    def test_wall_collisions_left_wall(self):
        for particle in self.box.particles:
            # Set particle position to the centre-left of the box
            particle.setPosition(-self.box.width, 0)
            # Set particle velocity to point towards the wall
            particle.setVelocity(-1,0)

        self.box.wall_collisions()

        # Check that particle velocity is reversed in the correct direction
        for particle in self.box.particles:
            np.testing.assert_array_equal(particle.velocity, np.array([1, 0]))

    def test_wall_collisions_right_wall(self):
        for particle in self.box.particles:
            # Set particle position to the centre-right of the box
            particle.setPosition(self.box.width, 0)
            # Set particle velocity to point towards the wall
            particle.setVelocity(1,0)

        self.box.wall_collisions()

        # Check that particle velocity is reversed in the correct direction
        for particle in self.box.particles:
            np.testing.assert_array_equal(particle.velocity, np.array([-1, 0]))

    def test_wall_collisions_diagonal_TR(self):
        for particle in self.box.particles:
            # Set particle position to the TR corner of the box
            particle.setPosition(self.box.width, self.box.height)
        
            particle.setVelocity(1, 1)
        
        self.box.wall_collisions()
        # Check that particle velocity is reversed in the correct direction
        
        for particle in self.box.particles:
            np.testing.assert_array_equal(particle.velocity, np.array([-1, -1]))

    def test_wall_collisions_diagonal_TL(self):

        for particle in self.box.particles:
            # Set particle position to the corner of the box
            particle.setPosition(-self.box.width, self.box.height)
         
           
            particle.setVelocity(-1, 1)
       
        self.box.wall_collisions()
        # Check that particle velocity is reversed in the correct direction
        for particle in self.box.particles:
            np.testing.assert_array_equal(particle.velocity, np.array([1, -1]))

    def test_wall_collisions_diagonal_BR(self):
        for particle in self.box.particles:
            # Set particle position to the corner of the box
            particle.setPosition(self.box.width, self.box.height)
    
            particle.setVelocity(1, -1)
        self.box.wall_collisions()
        # Check that particle velocity is reversed in the correct direction
        for particle in self.box.particles:
            np.testing.assert_array_equal(particle.velocity, np.array([-1, 1]))

    def test_wall_collisions_diagonal_BL(self):
        for particle in self.box.particles:
            # Set particle position to the corner of the box
            particle.setPosition(self.box.width, self.box.height)
            # Set particle velocity to point towards the wall
            particle.setVelocity(-1, -1)
        self.box.wall_collisions()
        # Check that particle velocity is reversed in the correct direction
        for particle in self.box.particles:
            np.testing.assert_array_equal(particle.velocity, np.array([1, 1]))

    def test_particle_collisions(self):
        # Create two particles with initial positions and velocities that will cause them to collide
        particle1 = Particle(position=np.array([0, 0], dtype=float), velocity=np.array([1, 0], dtype=float))
        particle2 = Particle(position=np.array([1, 0], dtype=float), velocity=np.array([-1, 0], dtype=float))
        particle1.radius = 0.5
        particle2.radius = 0.5
        particle1.mass = 1.0
        particle2.mass = 1.0
        # Add particles to box
        self.box = Box(time_increment=1e-5, number_of_particles=2, width=5, height=5)
        self.box.particles = [particle1, particle2]
        # Call particle_collisions function
        self.box.particle_collisions()
        # Check that velocities have been updated correctly
        np.testing.assert_allclose(particle1.velocity, np.array([-1, 0]))
        np.testing.assert_allclose(particle2.velocity, np.array([1, 0]))


if __name__ == '__main__':
    unittest.main()
