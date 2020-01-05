'''
创建外星人类
'''
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    '''表示单个外星人的类'''

    def __init__(self,ai_settings,screen):
        '''初始化起始位置'''
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图片 设置其rect属性
        self.image = pygame.image.load('image/alien.png')
        self.rect = self.image.get_rect()

        #每个外星人最初位置设置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''绘制外星人'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        #向右移动
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x =self.x

    #检测外星人是否撞到了屏幕边缘
    def check_edges(self):
        '''如果检测到了有外星人撞到屏幕边缘，那么修改update'''
        scrern_rect = self.screen.get_rect()
        if self.rect.right >= scrern_rect.right:
            return True
        elif self.rect.left <= 0 :
            return True