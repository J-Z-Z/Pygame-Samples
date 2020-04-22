import pygame

class Bird():
    def __init__(self,g_settings,screen):
        '''初始化 并设置其初始位置'''
        self.screen = screen
        self.g_settings = g_settings

        #加载主体图像并获取其外接矩形
        self.image = pygame.image.load('images/bird.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将主体放在屏幕的中央部中央的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = 0.5 * self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.birdy = float(self.rect.y)

        #移动标识 用于持续移动
        self.moving = False



    def update(self):
        '''自动更新主体位置'''
        if self.rect.y < (self.screen_rect.bottom - 30):
            self.birdy += 10
        self.rect.centerx = self.center
        self.rect.y = self.birdy


    def move(self):
        '''根据标识符来改变主体的移动状态'''
        if self.moving and 0 < self.rect.y < (self.screen_rect.bottom):
            self.birdy -= 20
            self.rect.y = self.birdy



    def blitme(self):
        '''指定位置绘制主体'''
        self.screen.blit(self.image,self.rect)