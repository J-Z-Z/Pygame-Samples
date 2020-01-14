import pygame
from pygame.sprite import Sprite

class Ufo(Sprite):

    def __init__(self,ai_settings,screen):

        super(Ufo,self).__init__()

        #初始化ufo的初始位置
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载图片
        self.image = pygame.image.load("images/ufo1.png")
        self.rect = self.image.get_rect()

        #初始位置左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #精确化储存ufo位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''绘制ufo图象'''
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        '''如果外星人位于屏幕边缘，就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左或向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x