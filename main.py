import pygame
from logger import log_state

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            player.update(dt)
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        player.draw(screen)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
