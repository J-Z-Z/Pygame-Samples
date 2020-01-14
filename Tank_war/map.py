import pygame
import random

class Map():
    '''定义一个地图类'''

    #首先加载各种瓷砖tile贴图
    def __init__(self,screen,tk_settings):
        self.screen = screen
        self.tk_settings = tk_settings

        # 加载map各种图像并截图后获取其外接矩形
        self.image = pygame.image.load('images/瓷砖tile.bmp')

        self.image_map0_rect = pygame.Rect(0, 0, 32, 32)
        self.image_map1_rect = pygame.Rect(32, 0, 32, 32)
        self.image_map2_rect = pygame.Rect(64, 0, 32, 32)
        self.image_map3_rect = pygame.Rect(96, 0, 32, 32)
        self.image_map4_rect = pygame.Rect(128, 0, 32, 32)

        self.image_map0 = self.image.subsurface(self.image_map0_rect)
        self.image_map1 = self.image.subsurface(self.image_map1_rect)
        self.image_map2 = self.image.subsurface(self.image_map2_rect)
        self.image_map3 = self.image.subsurface(self.image_map3_rect)
        self.image_map4 = self.image.subsurface(self.image_map4_rect)

        self.rect_map0 = self.image_map0.get_rect()
        self.rect_map1 = self.image_map1.get_rect()
        self.rect_map2 = self.image_map2.get_rect()
        self.rect_map3 = self.image_map3.get_rect()
        self.rect_map4 = self.image_map4.get_rect()




        self.screen_rect = screen.get_rect()

        self.rect_map0.centerx = self.screen_rect.centerx - 32
        self.rect_map0.bottom = self.screen_rect.bottom

        self.rect_map1.centerx = self.screen_rect.centerx + 32
        self.rect_map1.bottom = self.screen_rect.bottom

        self.rect_map2.centerx = self.screen_rect.centerx
        self.rect_map2.bottom = self.screen_rect.bottom - 32

        self.rect_map3.centerx = self.screen_rect.centerx + 32
        self.rect_map3.bottom = self.screen_rect.bottom - 32

        self.rect_map4.centerx = self.screen_rect.centerx - 32
        self.rect_map4.bottom = self.screen_rect.bottom - 32

        # 其他位置上的砖块位置，使用random库实现随机位置
        self.mapnumber = random.randint(90, 100)
        self.rect_list = []
        for i in range(self.mapnumber):
            self.mapnumber_x = random.randrange(100, 700,32)
            self.mapnumber_y = random.randrange(100, 500,32)
            self.rect_list.append((self.mapnumber_x,self.mapnumber_y))


    def blitme(self):
        '''指定位置绘制主体'''
        self.screen.blit(self.image_map0, self.rect_map0)

        self.screen.blit(self.image_map1, self.rect_map1)

        self.screen.blit(self.image_map2, self.rect_map2)

        self.screen.blit(self.image_map3, self.rect_map3)

        self.screen.blit(self.image_map4, self.rect_map4)

        for i in self.rect_list:
            self.screen.blit(self.image_map0, i)
