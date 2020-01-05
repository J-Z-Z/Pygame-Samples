import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''对于子弹进行管理的类'''

    def __init__(self,ai_settings,screen,ship):
        '''在飞船所在处创建一个子弹'''
        super(Bullet,self).__init__()
        self.screen = screen


        #加载子弹的图片
        self.image = pygame.image.load('image/bullet.png')
        self.rect = self.image.get_rect()

        #再设置它的到飞船的位置上去
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储用小数表示的子弹位置
        self.bullety = float(self.rect.y)

        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        #更新表示子弹的小数值
        self.bullety -= self.speed_factor

        #更新子弹的rect的位置
        self.rect.y = self.bullety


    def blitme(self):
        '''指定位置绘制子弹'''
        self.screen.blit(self.image,self.rect)


