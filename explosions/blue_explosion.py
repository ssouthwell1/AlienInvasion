from explosions.explosion import Explosion
import pygame


class BlueExplosion(Explosion):
    def __init__(self, ai_settings, screen):
        super(BlueExplosion).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = ai_settings.blue_explosion_image
        self.image = pygame.transform.scale(self.image, (ai_settings.alien_width, ai_settings.alien_height))
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
