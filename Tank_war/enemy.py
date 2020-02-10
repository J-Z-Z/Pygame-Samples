import pygame
import random


class Enemy():
    '''定义一个enemy类'''

    def __init__(self, screen, tk_settings):
        '''初始化 并设置其初始位置'''
        self.screen = screen
        self.tk_settings = tk_settings

        # 加载home主体图像并截图后获取其外接矩形
        self.image = pygame.image.load('images/enemy.bmp')

        # 用subsurface剪切读入的图片pygame.Rect( left , top, width, height )高度、宽度、通道数(28x8, 28X8, 3)
        self.image_enemy_up_rect = pygame.Rect(0, 0, 28, 28)
        self.image_enemy_right_rect = pygame.Rect(0, 28, 28, 28)
        self.image_enemy_down_rect = pygame.Rect(0,56, 28, 28)
        self.image_enemy_left_rect = pygame.Rect(0,84, 28, 28)

        self.image_enemy_up = self.image.subsurface(self.image_enemy_up_rect)
        self.image_enemy_right = self.image.subsurface(self.image_enemy_right_rect)
        self.image_enemy_down = self.image.subsurface(self.image_enemy_down_rect)
        self.image_enemy_left = self.image.subsurface(self.image_enemy_left_rect)

        # 选择初始加载图片
        self.image_enemy = self.image_enemy_down

        # 初始位置
        self.rect = self.image_enemy.get_rect()
        self.screen_rect = screen.get_rect()

        # 将主体放在屏幕的底部中央靠右64像素的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

        # 移动标志
        self.moving_up = False
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False

    def update(self):

        '''根据移动标志来调整enemy的位置'''
        if random.randint(0,2) and self.rect.x < self.screen_rect.right - 28:
            self.image_enemy = self.image_enemy_right
            self.rect.x += 10

        if random.randint(0,2) and self.rect.x > 7:
            self.image_enemy = self.image_enemy_left
            self.rect.x -= 10

        if random.randint(0,2) and self.rect.y > 7:
            self.image_enemy = self.image_enemy_up
            self.rect.y -= 10

        if random.randint(0,2) and self.rect.y<(self.screen_rect.bottom - 28):
            self.image_enemy = self.image_enemy_down
            self.rect.y += 10



    def blitme(self):
        self.screen.blit(self.image_enemy, self.rect)

