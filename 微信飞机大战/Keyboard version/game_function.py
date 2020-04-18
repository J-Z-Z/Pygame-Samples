import pygame
#from pygame.locals import *
import sys
from  bullet import Bullet


def check_events(screen,py_settings,ship1,bullets):                   #监测键盘按键和鼠标等事件的函数
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出pygame
            pygame.quit()
            # 退出系统
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship1.moving_right = True

            if event.key == pygame.K_LEFT:
                ship1.moving_left = True

            if event.key == pygame.K_DOWN:
                ship1.moving_down = True

            if event.key == pygame.K_UP:
                ship1.moving_up = True

            if event.key == pygame.K_SPACE:
                #bullet.fire = True
                new_bullet = Bullet(screen,py_settings,ship1)
                bullets.add(new_bullet)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship1.moving_right = False

            if event.key == pygame.K_LEFT:
                ship1.moving_left = False

            if event.key == pygame.K_DOWN:
                ship1.moving_down = False

            if event.key == pygame.K_UP:
                ship1.moving_up = False



        # 监测鼠标操作
        '''
        if event.type == MOUSEMOTION:
            ship1.rect = event.pos
        '''


def update_screen(screen,py_settings,ship1,enemy1,bullets):
    screen.blit(py_settings.bg_image, (0, 0))
    ship1.blitme()
    enemy1.blitme()
    ship1.update(py_settings)
    #绘画每一颗子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet(screen)
    #bullets.draw_bullet()

def update_bullet(bullets):
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))

    pygame.display.flip()