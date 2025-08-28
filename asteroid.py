import pygame
import random
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", tuple(map(int, self.position)), self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform (20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        self.radius -= ASTEROID_MIN_RADIUS
        newasteroid1 = Asteroid(int(self.position.x), int(self.position.y),self.radius)
        newasteroid1.velocity = (vector1 * 1.2)
        newasteroid2 = Asteroid(int(self.position.x), int(self.position.y),self.radius)
        newasteroid2.velocity = (vector2 *1.2)
        