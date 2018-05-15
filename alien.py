import pygame

from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien images and set its rect attributes
        self.blue_alien = pygame.image.load('images/blue_alien.png')
        # self.green_alien = pygame.image.load('images/green_alien.png')
        # self.red_alien = pygame.image.load('images/red_alien.png')
        self.blue_alien = pygame.transform.scale(self.blue_alien, (75, 85))
        # self.green_alien = pygame.transform.scale(self.green_alien, (130, 130))
        # self.red_alien = pygame.transform.scale(self.red_alien, (130, 130))
        # self.images = [self.blue_alien, self.green_alien, self.red_alien]
        # self.index = 0
        # self.image = self.images[self.index]
        self.rect = self.blue_alien.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.blue_alien, self.rect)
