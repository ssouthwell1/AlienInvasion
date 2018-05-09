import pygame


class Ship():

    def __init__(self, screen):
        # Initialize the ship and set its starting position
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/spaceship.png')
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
