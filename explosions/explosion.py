import pygame
from aliens.alien import Alien


class Explosion(Alien):
    def __init__(self, ai_settings, alien, screen):
        super(Explosion, self).__init__(ai_settings, screen)
        self.image = pygame.image.load('images/green_explosion.png')
        # The explosion should be the same height and width as the alien
        self.image = pygame.transform.scale(self.image, (ai_settings.explosion_width, ai_settings.explosion_height))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.center = alien.rect.center
        self.last_update = pygame.time.get_ticks()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update >= 100:
            # To look like an animated explosion
            # change the size of the image at different time intervals
            self.last_update = now
            self.kill()
            print("It came here!")
