import pygame
class Pipe():
    def __init__(self):
        self.pipe_1 = pygame.image.load("pic/pipe.png")
        self.pipe_2 = pygame.image.load("pic/pipe.png")

        #外接矩形rect
        self.rect_1 = self.pipe_1.get_rect()
        self.rect_2 = self.pipe_2.get_rect()

        #初始化pipe的位置
        self.rect_1.x = 500
        self.rect_1.y = 300
        self.rect_2.x = 500
        self.rect_2.y = -500

    def update(self):
        self.rect_1.x -= 1
        self.rect_2.x -= 1