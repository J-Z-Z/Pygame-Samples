import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,py_settings,ship1):
        #声明编组
        super(Bullet,self).__init__()

        self.screen = screen

        self.bullet_image = pygame.image.load("bullet.png")
        self.bullet_image2 = pygame.image.load("bullet.png")


        #加载子弹外接矩形
        self.rect = self.bullet_image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = ship1.rect.centerx - 15
        self.rect.top = ship1.rect.top -10
#__________________________________________________________
        self.rect2 = self.bullet_image2.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect2.centerx = ship1.rect.centerx + 15
        self.rect2.top = ship1.rect.top - 10
        #初始化位置（0,0）点
        #self.rect = pygame.Rect(0,0,py_settings.bullet_width,py_settings.bullet_height)

        #self.rect.centerx = ship1.rect.centerx
        #self.rect.top = ship1.rect.top
        #self.color = py_settings.bullet_color
        self.speed = py_settings.bullet_speed

        #self.fire = False

    def update(self):
        '''不断向上移动的子弹'''
        #if self.fire == True:
        self.rect.y -= self.speed
        self.rect2.y -= self.speed

    def draw_bullet(self,screen):
        screen.blit(self.bullet_image,self.rect)
        screen.blit(self.bullet_image2, self.rect2)
        #pygame.draw.rect(self.screen,self.color,self.rect)
