import pygame

class Body():
    def __init__(self, screen):
        self.screen = screen

        # 加载图片
        self.img = pygame.image.load('image/body.png')
        self.rect = self.img.get_rect()
        self.screen_rect = self.screen.get_rect()


        # 位置
        self.rect.x = 1000
        self.rect.y = 300

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        # 初始化的位置 朝左1 上2 右3 下 4
        self.moving_size = 1

    def blit_body(self):
        self.screen.blit(self.img,self.rect)

    def update(self):
        if self.moving_size == 1:
            self.rect.x -= 1
            if self.moving_up:
                self.moving_size = 2

            if self.moving_down:
                self.moving_size = 4

        elif self.moving_size == 2:
            self.rect.y -= 1
            if self.moving_right:
                self.moving_size = 3

            if self.moving_left:
                self.moving_size = 1

        elif self.moving_size == 3:
            self.rect.x += 1
            if self.moving_down:
                self.moving_size = 4
            if self.moving_up:
                self.moving_size = 2

        else:
            self.rect.y += 1
            if self.moving_left:
                self.moving_size = 1
            if self.moving_right:
                self.moving_size = 3
