import pygame

class Ship():
    def __init__(self,screen):
        '''初始化飞船和其位置'''
        self.screen = screen

        #加载飞船图片
        self.image = pygame.image.load("hero.png")
        #获取图片的外接矩形
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #初始化飞船位置
        self.rect.x = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #移动标签
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False


    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def update(self,py_settings):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += py_settings.ship_speed

        if self.moving_left  and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= py_settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += py_settings.ship_speed

        if self.moving_up  and self.rect.top > 0:
            self.rect.y -= py_settings.ship_speed