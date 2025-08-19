import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position = self.position + ( self.velocity * dt )

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_direction = random.uniform(20,50)
            asteroid1_velocity = self.velocity.rotate(new_direction)
            asteroid2_velocity = self.velocity.rotate(-new_direction)

            asteroid_radius = self.radius- ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position[0],self.position[1],asteroid_radius)
            new_asteroid2 = Asteroid(self.position[0],self.position[1],asteroid_radius)

            new_asteroid1.velocity = asteroid1_velocity * 1.2
            new_asteroid2.velocity =asteroid2_velocity * 1.2