import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        '''初始化飞船 并设置其初始位置'''
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放在屏幕的底部中央的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom



        #移动标志
        self.moving_right = False

        self.moving_left = False

        self.moving_up = False

        self.moving_down = False

        #在飞船的center属性储存小数值
        self.center = float(self.rect.centerx)
        self.shipy = float(self.rect.y)

    def update(self):
        '''根据移动标志来调整飞船的位置
           更新飞船的center值 因为rect只能是整数，像素只能是整数
        '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.y >0:
            self.shipy -= self.ai_settings.ship_speed_factor
            #print(self.shipy)
        if self.moving_down and self.rect.y<(self.screen_rect.bottom - 80):
            self.shipy += self.ai_settings.ship_speed_factor
            #print(self.shipy)

        #根据cente的更新更新rect
        self.rect.centerx = self.center
        self.rect.y = self.shipy


    def blitme(self):
        '''指定位置绘制飞创'''
        self.screen.blit(self.image,self.rect)