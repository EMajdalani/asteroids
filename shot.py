from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius=SHOT_RADIUS)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
