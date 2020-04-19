import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, screen):
        # 声明编组
        super(Enemy, self).__init__()

        '''初始化和其位置'''
        self.screen = screen

        # 加载图片
        self.image = pygame.image.load("enemy.png")
        # 获取图片的外接矩形
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 初始化飞船位置
        self.rect.x = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top



    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, py_settings):
        self.rect.y += py_settings.enemy_speed

