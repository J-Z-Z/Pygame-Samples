import pygame
class Settings():
    def __init__(self):
        #初始化游戏的设置
        self.screen_width = 400
        self.screen_height = 600
        self.bg_image = pygame.image.load("background.png")

        #设置飞船参数
        self.ship_speed = 1

        #设置子弹的参数
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
