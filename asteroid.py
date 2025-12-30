from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

from logger import log_event
from random import uniform

import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        log_event("asteroid_split")
        split_degree = uniform(20, 50)

        first_asteroid_vector = self.velocity.rotate(split_degree)
        second_asteroid_vector = self.velocity.rotate(-split_degree)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        self.kill()

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        first_asteroid.velocity = first_asteroid_vector * 1.2
        second_asteroid.velocity = second_asteroid_vector * 1.2




