'''pygame.transform.rotate(Surface, angle) (旋转)

     angle : 旋转角度

     returnSurface
'''

import pygame

class Head():
    def __init__(self, screen,body):
        self.screen = screen
        self.body = body

        # 加载图片
        self.img = pygame.image.load('image/head.png')
        self.rect = self.img.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.img_down = pygame.transform.rotate(self.img, 90)
        self.img_up = pygame.transform.rotate(self.img, -90)
        self.img_left = pygame.transform.rotate(self.img, 0)
        self.img_right = pygame.transform.rotate(self.img,180)


        # 位置
        self.rect.centerx = self.body.rect.centerx-65
        self.rect.centery = self.body.rect.centery

        #移动标志
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down= False

        #初始化的位置 朝左1 上2 右3 下 4
        self.moving_size = 1

    def blit_head(self):
        self.screen.blit(self.img,self.rect)

    def update(self):
        if self.moving_size == 1:
            self.rect.x -= 1
            if self.moving_up:
                self.img = self.img_up
                self.moving_size = 2
                self.rect.centerx = self.body.rect.centerx - 10
                self.rect.centery = self.body.rect.centery - 60
            if self.moving_down:
                self.img = self.img_down
                self.moving_size = 4
                self.rect.centerx = self.body.rect.centerx - 5
                self.rect.centery = self.body.rect.centery + 70

        elif self.moving_size == 2:
            self.rect.y -= 1
            if self.moving_right:
                self.img = self.img_right
                self.moving_size = 3
                self.rect.centerx = self.body.rect.centerx + 65
                self.rect.centery = self.body.rect.centery
            if self.moving_left:
                self.img = self.img_left
                self.moving_size = 1
                self.rect.centerx = self.body.rect.centerx-65
                self.rect.centery = self.body.rect.centery

        elif self.moving_size == 3:
            self.rect.x += 1
            if self.moving_down:
                self.img = self.img_down
                self.moving_size = 4
                self.rect.centerx = self.body.rect.centerx - 5
                self.rect.centery = self.body.rect.centery + 70
            if self.moving_up:
                self.img = self.img_up
                self.moving_size = 2
                self.rect.centerx = self.body.rect.centerx - 10
                self.rect.centery = self.body.rect.centery - 60

        else:
            self.rect.y += 1
            if self.moving_left:
                self.img = self.img_left
                self.moving_size = 1
                self.rect.centerx = self.body.rect.centerx - 65
                self.rect.centery = self.body.rect.centery
            if self.moving_right:
                self.img = self.img_right
                self.moving_size = 3
                self.rect.centerx = self.body.rect.centerx + 65
                self.rect.centery = self.body.rect.centery

