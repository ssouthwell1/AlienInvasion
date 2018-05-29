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
        self.bullets_allowed = 2

        # Sound settings
        # refactor later self.sounds = ["shoot", "invaderkilled" "explosion"]
        # put them in a list and format the file type
        self.sound_shoot = pygame.mixer.Sound('sounds/shoot.wav')
        self.sound_invader_killed = pygame.mixer.Sound('sounds/invaderkilled.wav')
        self.sound_explosion = pygame.mixer.Sound('sounds/explosion.wav')

        # Alien settings
        self.alien_width = 55
        self.alien_height = 65
        self.available_space_x = self.screenwidth - (4 * self.alien_width)
        # See about changing the amount of space between each alien later
        self.number_aliens_x = self.available_space_x - (2 * self.alien_width)
        self.alien_rows = 4
        self.alien_columns = 10
        self.alien_row_x = 200
        self.alien_row_y = 65
        self.alien_column_x = 80
        self.alien_column_y = 65
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        self.blue_explosion_image = pygame.image.load('images/blue_explosion.png')
        self.red_explosion_image = pygame.image.load('images/red_explosion.png')
        self.green_explosion_image = pygame.image.load('images/blue_explosion.png')

        # Explosion settings
        self.explosion_width = 40
        self.explosion_height = 50
