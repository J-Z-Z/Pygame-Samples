import pygame
import sys

from head import Head
from end import End
from body import Body

pygame.init()
FPS=60

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('贪吃蛇')



body = Body(screen)
head = Head(screen,body)
end = End(screen,body)

while True:
    for event in pygame.event.get():
        # 判断事件是否为退出事件
        if event.type == pygame.QUIT:
            # 退出pygame
            pygame.quit()
            # 退出系统
            sys.exit()
        #写控制蛇移动的一些标记
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                head.moving_left = True
                body.moving_left = True
                end.moving_left = True

            if event.key == pygame.K_RIGHT:
                head.moving_right = True
                body.moving_right = True
                end.moving_right = True


            if event.key == pygame.K_UP:
                head.moving_up = True
                body.moving_up = True
                end.moving_up = True

            if event.key == pygame.K_DOWN:
                head.moving_down = True
                body.moving_down = True
                end.moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                head.moving_left = False
                body.moving_left = False
                end.moving_left = False

            if event.key == pygame.K_RIGHT:
                head.moving_right = False
                body.moving_right = False
                end.moving_right = False

            if event.key == pygame.K_UP:
                head.moving_up = False
                body.moving_up = False
                end.moving_up = False

            if event.key == pygame.K_DOWN:
                head.moving_down = False
                body.moving_down = False
                end.moving_down = False


    screen.fill((255,255,255))

    head.update()
    body.update()
    end.update()

    head.blit_head()

    body.blit_body()

    end.blit_end()

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)