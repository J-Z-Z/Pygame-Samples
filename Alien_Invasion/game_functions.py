import sys
import pygame
from bullet import Bullet
from bullet1 import Bullet1
from bullet2 import Bullet2

def check_events(ai_settings,screen,ship,bullets,bullets1,bullets2):
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()

        elif even.type == pygame.KEYDOWN:
            if even.key == pygame.K_LEFT:
                ship.moving_left = True
            elif even.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif even.key == pygame.K_UP:
                ship.moving_up = True
            elif even.key == pygame.K_DOWN:
                ship.moving_down = True

            #开火
            elif even.key == pygame.K_SPACE:
                new_bullet = Bullet(ai_settings,screen,ship)
                bullets.add(new_bullet)
                new_bullet1 = Bullet1(ai_settings, screen, ship)
                bullets1.add(new_bullet1)
                new_bullet2 = Bullet2(ai_settings, screen, ship)
                bullets2.add(new_bullet2)

        elif even.type == pygame.KEYUP:
            if even.key == pygame.K_LEFT:
                ship.moving_left = False
            elif even.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif even.key == pygame.K_UP:
                ship.moving_up = False
            elif even.key == pygame.K_DOWN:
                ship.moving_down = False



def update_screen(ai_settings,screen,ship,bullets,bullets1,bullets2):
    screen.fill(ai_settings.bg_color)
    
    for i in bullets.sprites():
        i.draw_bullet()

    for j in bullets1.sprites():
        j.draw_bullet()

    for k in bullets2.sprites():
        k.draw_bullet()

    ship.blitme()
    pygame.display.flip()

def update_bullets(bullets,bullets1,bullets2):
    bullets.update()

    bullets1.update()

    bullets2.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    for bullet in bullets1.copy():
        if bullet.rect.bottom <= 0:
            bullets1.remove(bullet)
    for bullet in bullets2.copy():
        if bullet.rect.bottom <= 0:
            bullets2.remove(bullet)