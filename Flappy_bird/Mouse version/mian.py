import pygame,sys
from settings import Settings
from pygame.locals import *
from play import Play
from pipe import Pipe

pygame.init()
py_setings = Settings()

screen = pygame.display.set_mode((py_setings.screen_width,py_setings.screen_height))

# 设置标题
pygame.display.set_caption("FlyBird")

#生成一个像素鸟对象
play = Play(screen)

#生成一组管道对象
pipe = Pipe()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type == MOUSEMOTION:
        play.rect = event.pos




    screen.blit(py_setings.bg_image_0,(0,0))

    screen.blit(pipe.pipe_1, pipe.rect_1)
    screen.blit(pipe.pipe_2, pipe.rect_2)

    screen.blit(py_setings.g_image, (0, 400))
    screen.blit(play.image,play.rect)

    pipe.update()

    pygame.display.flip()
