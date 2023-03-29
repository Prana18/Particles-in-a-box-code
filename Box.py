import numpy as np
from Particle import Particle
import math

class Box:
    """
    A class representing a box containing particles.
    """
    def __init__(
        self,
        time_increment = 1e-5,
        number_of_particles = 10,
        width = 5,
        height = 5,
        initial_temperature = 200
    ):
        """
        A standard box when called on will use these predefined parameters
        listed above unless explicitly given new parameters.

        """
        self.time_increment = time_increment
        self.number_of_particles = number_of_particles
        self.width = width
        self.height = height
        self.initial_temperature = initial_temperature
        self.particles = [Particle(i) for i in range(self.number_of_particles)]

    def random_pos(self):
        """
        Assign random positions to all particles in the box.
        """
        for i in range(self.number_of_particles):
            self.particles[i].position[0] = np.random.uniform(-self.width / 2, self.width / 2)
            self.particles[i].position[1] = np.random.uniform(-self.height / 2, self.height / 2)

    def random_vel(self):
        """
        Assign random velocities to all particles in the box.
        """
        for i in range(self.number_of_particles):
            self.particles[i].velocity = 20 * np.random.uniform(-1, 1, 2)

    def maxwell_boltzmann_velocities(self, temperature):
        """
        Assign velocities to particles in the box according to the Maxwell-Boltzmann distribution.

        """
        kB = 1.380649e-23
        for i in range(self.number_of_particles):
            # self.particles[i].velocity = 20 * np.random.uniform(0, np.sqrt((kB * temperature) / 5e-26), 2)
            self.particles[i].velocity = np.random.uniform(0, np.sqrt((kB * temperature) / 5e-26), 2)

    def update_pos(self):

       """
       Update the position of all particles in the box.
       Check for wall and particle collisions and update velocities accordingly.
       """

       for particle in self.particles:
        new_x = particle.position[0] + (self.time_increment * particle.velocity[0])
        new_y = particle.position[1] + (self.time_increment * particle.velocity[1])
        wall_offset = particle.radius

        if new_x <= -self.width:
            particle.setVelocity(particle.velocity[0] * -1, particle.velocity[1])
            new_x = -self.width + wall_offset
        elif new_x >= self.width:
            particle.setVelocity(particle.velocity[0] * -1, particle.velocity[1])
            new_x = self.width - wall_offset

        if new_y <= -self.height:
            particle.setVelocity(particle.velocity[0], particle.velocity[1] * -1)
            new_y = -self.height + wall_offset
        elif new_y >= self.height:
            particle.setVelocity(particle.velocity[0], particle.velocity[1] * -1)
            new_y = self.height - wall_offset

        particle.setPosition(new_x, new_y) 

        self.particle_collisions()  # Check for particle collisions after updating positions

   
    def particle_collisions(self):
        """
        Detect particle collisions and update their velocities accordingly.
        """
        for i, particle1 in enumerate(self.particles):
            for particle2 in self.particles[i+1 :]:
                dist = np.linalg.norm(particle1.position - particle2.position)
                if dist <= 1* (particle1.radius + particle2.radius):
                    # calculate new velocities
                    v1, v2 = particle1.velocity, particle2.velocity
                    m1, m2 = particle1.mass, particle2.mass
                    x1, x2 = particle1.position, particle2.position
                    v1_new = v1 - 2 * m2 / (m1 + m2) * np.dot(v1 - v2, x1 - x2) / np.linalg.norm(x1 - x2)**2 * (x1 - x2)
                    v2_new = v2 - 2 * m1 / (m1 + m2) * np.dot(v2 - v1, x2 - x1) / np.linalg.norm(x2 - x1)**2 * (x2 - x1)
                    particle1.setVelocity(v1_new[0], v1_new[1])
                    particle2.setVelocity(v2_new[0], v2_new[1])
              
                  

                    #translating particles outside of the other particle
                    vectordiff = x1 - x2
                    x1_new = x1 + vectordiff/5
                    x2_new = x2 - vectordiff/5
                    particle1.setPosition(x1_new[0],x1_new[1])
                    particle2.setPosition(x2_new[0],x2_new[1])

    def wall_collisions(self):
        """
        Detect wall collisions and update particle velocities accordingly.
        """
        for particle in self.particles:
            new_x = particle.position[0] + (self.time_increment * particle.velocity[0])
            new_y = particle.position[1] + (self.time_increment * particle.velocity[1])

            if (particle.position[0] < -self.width + particle.radius)  or (particle.position[0] > self.width - particle.radius):
                particle.setVelocity((particle.velocity[0] * -1), particle.velocity[1])

            if (particle.position[1] < -self.height + particle.radius)  or (particle.position[1] > self.height - particle.radius):
                particle.setVelocity(particle.velocity[0], (particle.velocity[1] * -1))

            particle.setPosition(new_x, new_y)
   

    def total_energy(self):
        """
        Calculate the total kinetic energy of all particles in the box.
        """
        total = 0
        for particle in self.particles:
            speed = np.linalg.norm(particle.velocity)
            ke = 0.5 * particle.mass * speed**2
            total = total + ke
        return total
    
    def total_momentum(self):
        """
        Calculate the total momentum of all particles in the box.
        """

        total = 0
        for particle in self.particles:
            speed = np.linalg.norm(particle.velocity)
            m = particle.mass * speed
            total = total + m
        return total
    
    def velocity_distribution(self):
        """
        Calculate the velocity distribution of particles in the box.
        """
        speeds = []  # Create a list of particle speeds
        for particle in self.particles:
            speed = np.linalg.norm(particle.velocity)
            speeds.append(speed)
        return speeds
    
    def calculate_temperature(self):
        """
        Calculate the temperature of the box using the kinetic energy of the particles.

        """
        boltzmann_constant = 1.380649e-23  # J/K
        total_kinetic_energy = self.total_energy()
        temperature = (2 / 3) * (total_kinetic_energy / (self.number_of_particles * boltzmann_constant))
        return temperature

    def total_collisions(self):
        """
        Calculate the total number of collisions that have occurred in the simulation.
        """
        particle_collisions = sum(particle.collisions for particle in self.particles)
        wall_collisions = sum(particle.wall_collisions for particle in self.particles)
        return particle_collisions + wall_collisions






     

    





