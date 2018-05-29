import pygame

from pygame.sprite import Sprite


# Refactor the alien images and properties later
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien images and set its rect attributes

        # Add logic for different aliens later

        self.image = None
        self.images = []
        self.load_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.time = pygame.time.get_ticks()

        # load each for each alien type
        # self.blue_alien = pygame.image.load('images/blue_alien.png')
        #  self.green_alien = pygame.image.load('images/green_alien.png')
        #  self.red_alien = pygame.image.load('images/red_alien.png')
        #  self.orange_alien = pygame.image.load('images/orange_alien.png')

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def load_images(self):

        self.image = pygame.image.load('images/aliens/blue_alien.png')

        self.images.append(
            pygame.transform.scale(self.image, (self.ai_settings.alien_width, self.ai_settings.alien_height)))

    def check_edges(self):
        """Return true if alien is at the edge of screen"""
        if self.rect.right >= self.screen.get_rect().right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
