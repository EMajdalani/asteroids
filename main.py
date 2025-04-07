import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import*
from asteroidfield import *
from shot import *

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, update_group, draw_group)
    Player.containers = (update_group, draw_group)
    AsteroidField.containers = (update_group)
    Shot.containers = (shots, update_group, draw_group)
    field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        update_group.update(dt)
        for object in draw_group:
            object.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                print("Game over!")
                pygame.QUIT
                return

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()