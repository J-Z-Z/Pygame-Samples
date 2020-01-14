import pygame


class Ship():

    def __init__(self,screen):
        #初始化ship的初始位置
        self.screen = screen

        #加载图片
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #移动标签
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 20
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 20
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 20
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 20


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom