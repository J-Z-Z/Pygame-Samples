import pygame

class Home():
    '''设置home类'''

    def __init__(self,screen,tk_settings):
        '''初始化 并设置其初始位置'''
        self.screen = screen
        self.tk_settings = tk_settings

        # 加载home主体图像并截图后获取其外接矩形
        self.image = pygame.image.load('images/瓷砖tile.bmp')

        # 用subsurface剪切读入的图片pygame.Rect( left , top, width, height )高度、宽度、通道数(32, 224, 3)
        self.image_home_rect = pygame.Rect(160,0,32,32)
        self.image_home = self.image.subsurface(self.image_home_rect)

        self.rect = self.image_home.get_rect()
        self.screen_rect = screen.get_rect()

        # 将主体放在屏幕的底部中央的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''指定位置绘制主体'''
        self.screen.blit(self.image_home, self.rect)
