import pygame
import random
#from pygame.sprite import Sprite

class Building():
    def __init__(self, g_settings, screen):
        '''初始化'''
        #super(Building, self).__init__()

        self.screen = screen
        self.ai_settings = g_settings

        # 加载图像并获取其外接矩形
        self.image1 = pygame.image.load('images/building.png')
        self.rect1 = self.image1.get_rect()

        self.image2 = pygame.image.load('images/building.png')
        self.rect2 = self.image2.get_rect()

        self.screen_rect = screen.get_rect()

        self.number = random.randint(200,500)

        # 设置上部分Building最初位置设置
        self.rect1.x = self.screen_rect.right
        #print(self.rect.x)
        self.rect1.y = self.number - 1.6 * g_settings.screen_height
        #print(self.rect.y)

        # 设置下部分Building最初位置设置
        self.rect2.x = self.screen_rect.right
        self.rect2.y = self.number


    def blitme(self):
        '''绘制Building'''
        self.screen.blit(self.image1,self.rect1)
        self.screen.blit(self.image2, self.rect2)

    def update(self):
        '''自动更新Building的位置'''
        if self.rect1.x > -60:
            self.rect1.x -= 3
            self.rect2.x -= 3
