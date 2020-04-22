import pygame

class Play():
    def __init__(self,screen):
        '''初始化位置'''
        self.screen = screen

        # 加载像素鸟图片
        self.image = pygame.image.load("pic/play.png")
        # 获取图片的外接矩形
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 初始化位置
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery




