import pygame

class End():
    def __init__(self, screen , body):
        self.screen = screen

        self.body = body

        # 加载图片
        self.img = pygame.image.load('image/end.png')
        self.rect = self.img.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.img_down = pygame.transform.rotate(self.img, 90)
        self.img_up = pygame.transform.rotate(self.img, -90)
        self.img_left = pygame.transform.rotate(self.img, 0)
        self.img_right = pygame.transform.rotate(self.img, 180)

        # 位置
        self.rect.x = self.body.rect.x + 44
        self.rect.y = self.body.rect.y

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        # 初始化的位置 朝左1 上2 右3 下 4
        self.moving_size = 1


    def blit_end(self):
        self.screen.blit(self.img,self.rect)

    def update(self):
        if self.moving_size == 1:
            self.rect.x -= 1
            if self.moving_up:
                self.img = self.img_up
                self.moving_size = 2
                self.rect.x = self.body.rect.x
                self.rect.y = self.body.rect.y+44
            if self.moving_down:
                self.img = self.img_down
                self.moving_size = 4
                self.rect.x = self.body.rect.x
                self.rect.y = self.body.rect.y-44

        elif self.moving_size == 2:
            self.rect.y -= 1
            if self.moving_right:
                self.img = self.img_right
                self.moving_size = 3
                self.rect.x = self.body.rect.x - 44
                self.rect.y = self.body.rect.y
            if self.moving_left:
                self.img = self.img_left
                self.moving_size = 1
                self.rect.x = self.body.rect.x + 44
                self.rect.y = self.body.rect.y

        elif self.moving_size == 3:
            self.rect.x += 1
            if self.moving_down:
                self.img = self.img_down
                self.moving_size = 4
                self.rect.x = self.body.rect.x
                self.rect.y = self.body.rect.y - 44
            if self.moving_up:
                self.img = self.img_up
                self.moving_size = 2
                self.rect.x = self.body.rect.x
                self.rect.y = self.body.rect.y + 44

        else:
            self.rect.y += 1
            if self.moving_left:
                self.img = self.img_left
                self.moving_size = 1
                self.rect.x = self.body.rect.x + 44
                self.rect.y = self.body.rect.y
            if self.moving_right:
                self.img = self.img_right
                self.moving_size = 3
                self.rect.x = self.body.rect.x - 44
                self.rect.y = self.body.rect.y

