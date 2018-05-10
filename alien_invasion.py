
import pygame

from settings import Settings

from ship import Ship

import game_functions as gf


def run_game():
    # Initailize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screenwidth, ai_settings.screenheight))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    while True:
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        gf.check_events()
        pygame.display.flip()


run_game()
