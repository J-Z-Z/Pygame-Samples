import sys
import pygame
from bullet import Bullet
from bullet1 import Bullet1
from bullet2 import Bullet2
from bullet3 import Bullet3

def check_events(tk_settings, screen, play1,bullets,bullets1,bullets2,bullets3):
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
                if play1.image_play1 == play1.image_play1_up:
                    new_bullet = Bullet(tk_settings, screen, play1)
                    bullets.add(new_bullet)
                elif play1.image_play1 == play1.image_play1_left:
                    new_bullet1 = Bullet1(tk_settings, screen, play1)
                    bullets1.add(new_bullet1)
                elif play1.image_play1 == play1.image_play1_right:
                    new_bullet2 = Bullet2(tk_settings, screen, play1)
                    bullets2.add(new_bullet2)
                elif play1.image_play1 == play1.image_play1_down:
                    new_bullet3 = Bullet3(tk_settings, screen, play1)
                    bullets3.add(new_bullet3)




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



def update_bullets(tk_settings,bullets,bullets1,bullets2,bullets3):
    #更新子单位制 并且 删除超过边界的子弹
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))

    bullets1.update()
    for bullet in bullets1.copy():
        if bullet.rect.right <= 0:
            bullets1.remove(bullet)
    # print(len(bullets1))

    bullets2.update()
    for bullet in bullets2.copy():
        if bullet.rect.left >= tk_settings.screen_width:
            bullets2.remove(bullet)
    # print(len(bullets2))

    bullets3.update()
    for bullet in bullets3.copy():
        if bullet.rect.top >= tk_settings.screen_height:
            bullets3.remove(bullet)
    # print(len(bullets3))



def update_screen(screen,tk_settings,home,map,play1,enemy,enemy1,enemy2,bullets,bullets1,bullets2,bullets3):
    # 背景颜色刷新
    screen.fill(tk_settings.screen_color)

    home.blitme()
    map.blitme()

    #for map in maps.sprites():map.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for bullet1 in bullets1.sprites():
        bullet1.draw_bullet()

    for bullet2 in bullets2.sprites():
        bullet2.draw_bullet()

    for bullet3 in bullets3.sprites():
        bullet3.draw_bullet()

    play1.blitme()
    enemy.blitme()
    enemy1.blitme()
    enemy2.blitme()
    play1.update()
    enemy.update()
    enemy1.update()
    enemy2.update()
    # 显示屏幕
    pygame.display.flip()