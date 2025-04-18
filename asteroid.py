from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector_one = pygame.math.Vector2.rotate(self.velocity, random_angle)
        vector_two = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        ast_one = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
        ast_two = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
        ast_one.velocity = vector_one * 1.2
        ast_two.velocity = vector_two * 1.2


