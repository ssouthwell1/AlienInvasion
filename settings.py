import pygame


class Settings:
    YELLOW = (241, 255, 0)

    def __init__(self):
        self.screenwidth = 1200
        self.screenheight = 800
        self.bg_color = (0, 0, 0)
        self.bg_image = pygame.image.load('images/background.png')
        # self.ship_width = 150
        # self.ship_height = 150
        self.ship_speed_factor = 10

        # Bullet settings
        self.bullet_speed_factor = 50
        self.bullet_width = 3
        self.bullet_height = 15
        # self.bullet_color = 241, 255, 0
        self.bullet_color = 237, 28, 36
        self.bullets_allowed = 3

        # Sound settings
        # refactor later self.sounds = ["shoot", "invaderkilled" "explosion"]
        # put them in a list and format the file type
        self.sound_shoot = pygame.mixer.Sound('sounds/shoot.wav')
        self.sound_invader_killed = pygame.mixer.Sound('sounds/invaderkilled.wav')
        self.sound_explosion = pygame.mixer.Sound('sounds/explosion.wav')

        # Alien settings
