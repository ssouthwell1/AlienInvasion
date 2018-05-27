import pygame

from pygame.sprite import Sprite

from alien import Alien


class BlueAlien(Alien):
    def __init__(self, ai_settings, screen):
        super(BlueAlien, self).__init__(ai_settings, screen)
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/blue_alien.png')
        self.image = pygame.transform.scale(self.image, (ai_settings.alien_width, ai_settings.alien_height))
