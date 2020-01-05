import sys
import pygame

def check_events(play1):
    # 监测键盘鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                play1.moving_up = True

            elif event.key == pygame.K_RIGHT:
                play1.moving_right = True

            elif event.key == pygame.K_DOWN:
                play1.moving_down = True

            elif event.key == pygame.K_LEFT:
                play1.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                play1.moving_up = False

            elif event.key == pygame.K_RIGHT:
                play1.moving_right = False

            elif event.key == pygame.K_DOWN:
                play1.moving_down = False

            elif event.key == pygame.K_LEFT:
                play1.moving_left = False



def update_screen(screen,tk_settings,home,map,play1):
    # 背景颜色刷新
    screen.fill(tk_settings.screen_color)

    home.blitme()
    map.blitme()
    play1.blitme()
    play1.update()
    # 显示屏幕
    pygame.display.flip()