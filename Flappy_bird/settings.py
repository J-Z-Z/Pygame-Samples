import pygame

class Settings():
    '''存储游戏的所有设置的类'''

    def __init__(self):
        ''''初始化游戏的设置'''
        #屏幕设置
        self.screen_width = 300
        self.screen_height = 500
        self. background = pygame.transform.scale(pygame.image.load('images/background_0.png'), (self.screen_width,self.screen_height))

        # 设置背景图片
        #background = pygame.image.load('images/background_0.png')
        #background = pygame.transform.scale(background, (300, 500))