import sys
import pygame
from bullet import Bullet

def check_events(tk_settings, screen, play1,bullets):
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

            # 开火
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(tk_settings, screen, play1)
                bullets.add(new_bullet)


    #------------------

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                play1.moving_up = False

            elif event.key == pygame.K_RIGHT:
                play1.moving_right = False

            elif event.key == pygame.K_DOWN:
                play1.moving_down = False

            elif event.key == pygame.K_LEFT:
                play1.moving_left = False



def update_screen(screen,tk_settings,home,map,play1,bullets):
    # 背景颜色刷新
    screen.fill(tk_settings.screen_color)

    home.blitme()
    map.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    play1.blitme()
    play1.update()
    # 显示屏幕
    pygame.display.flip()