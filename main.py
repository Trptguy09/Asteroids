import pygame
from player import *
from constants import *

def main():

    pygame.init()
    running = True
    black = (0,0,0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ASTEROIDS")
    clock = pygame.time.Clock()
    dt = 0
    Player.__init__(x,y)
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black, rect=None, special_flags=0)
        Player.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
