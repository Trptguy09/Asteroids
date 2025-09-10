import pygame
from constants import *
from player import Player

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ASTEROIDS")
    clock = pygame.time.Clock()

    
    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()


    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        updateable.update(dt)
        screen.fill("black")
        
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        

        dt = clock.tick(60)/100

if __name__ == "__main__":
    main()
