'''
子弹向下的集合的类
'''
import pygame
from pygame.sprite import Sprite


class Bullet3(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self, tk_settings, screen, ship):

        super(Bullet3, self).__init__()

        self.screen = screen
        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, tk_settings.bullet_width,tk_settings.bullet_height)

        # 当图片是image_play1_down的时候 设置枪口位置
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.bottom

        #self.y = float(self.rect.y)
        # 存储用小数表示的子弹位置 self.y = float(self.rect.y)
        self.color = tk_settings.bullet_color
        self.speed_factor = tk_settings.bullet_speed_factor

    def update(self):
        #self.rect.y

        self.rect.y += self.speed_factor

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)