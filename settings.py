class Settings:
    YELLOW = (241, 255, 0)

    def __init__(self):
        self.screenwidth = 1200
        self.screenheight = 800
        self.bg_color = (0, 0, 0)
        # self.ship_width = 150
        # self.ship_height = 150
        self.ship_speed_factor = 10

        # Bullet settings
        self.bullet_speed_factor = 20
        self.bullet_width = 3
        self.bullet_height = 15
        # self.bullet_color = 241, 255, 0
        self.bullet_color = 237, 28, 36
        self.bullets_allowed = 2
