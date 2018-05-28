import pygame

from settings import Settings

from pygame.sprite import Group

from ship import Ship

import game_functions as gf


def run_game():
    # Initialize game and create a screen object

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screenwidth, ai_settings.screenheight))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # load background music
    pygame.mixer.music.load("sounds/spaceinvaders.ogg")
    pygame.mixer.music.play(-1, 0.0)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        # gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        bullets.update()
        # gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        # gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
