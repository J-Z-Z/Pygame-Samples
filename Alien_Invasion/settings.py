class Settings():
    '''存储游戏的所有设置的类'''

    def __init__(self):
        ''''初始化游戏的设置'''
        #屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (250,250,250)
        self.ship_speed_factor = 10



        #子弹设置
        self.bullet_speed_factor = 10
        #self.bullet_width = 3
        #self.bullet_height = 15
        #self.bullet_color = (60,60,60)
        self.bullets_allowed = 10


        #外星人设置
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 3
        self.fleet_direction = 1

