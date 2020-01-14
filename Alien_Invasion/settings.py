class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (187,255,255)

        self.bullet_speed_factor = 20
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        self.alien_speed_factor = 20
        self.fleet_drop_speed = 5
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1



