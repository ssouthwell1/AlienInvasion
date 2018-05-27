import pygame

from alien import Alien


class GreenAlien(Alien):
    def __init__(self, ai_settings, screen):
        super(GreenAlien, self).__init__(ai_settings, screen)
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/green_alien.png')
        self.image = pygame.transform.scale(self.image, (ai_settings.alien_width, ai_settings.alien_height))
