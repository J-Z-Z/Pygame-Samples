import sys
import pygame
from building import Building


def check_events(bird):
    '''响应键盘和鼠标事件的功能函数集合'''
    for event in pygame.event.get():
        # 关于退出
        if event.type == pygame.QUIT:
            sys.exit()

        #关于使用 按键按下DOWN的情况
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.moving = True

        # 关于使用 按键抬起UP的情况
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird.moving = False


def update_screen(screen,g_settings,bird,building,building1,building2,building3,building4):
    '''更新屏幕的相关函数'''
    # 重绘游戏背景
    screen.blit(g_settings.background, (0, 0))

    # 重绘主体图片
    bird.blitme()
    building.blitme()
    building1.blitme()
    building2.blitme()
    building3.blitme()
    building4.blitme()

    # 更新主体自动下落
    bird.update()
    building.update()
    building1.update()
    building2.update()
    building3.update()
    building4.update()


    # 更新主体跳跃位置
    bird.move()

    # 让绘制的屏幕可见
    pygame.display.update()

