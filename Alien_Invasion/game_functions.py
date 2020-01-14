import sys
import pygame
from bullet import Bullet
from bullet1 import Bullet1
from bullet2 import Bullet2
from ufo import Ufo

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



def update_screen(ai_settings,screen,ship,ufoes,bullets,bullets1,bullets2):
    screen.fill(ai_settings.bg_color)

    for i in bullets.sprites():
        i.draw_bullet()

    for j in bullets1.sprites():
        j.draw_bullet()

    for k in bullets2.sprites():
        k.draw_bullet()


    ship.blitme()

    ufoes.draw(screen)

    pygame.display.flip()




def update_bullets(ai_settings, screen, ship, ufoes,bullets,bullets1,bullets2):
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

    #检查子弹和ufo是否接触
    collisions = pygame.sprite.groupcollide(bullets, ufoes, True, True)
    collisions1 = pygame.sprite.groupcollide(bullets1, ufoes, True, True)
    collisions2 = pygame.sprite.groupcollide(bullets2, ufoes, True, True)

    if len(ufoes) == 0:
        #删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings,screen,ufoes)

def create_fleet(ai_settings,screen,ufoes):
    ufo = Ufo(ai_settings, screen)
    ufo_width = ufo.rect.width
    #available_space_x = ai_settings.screen_width - 2 * ufo_width
    #number_x = int(available_space_x / (2 * ufo_width))

    for row in range(3):
        for u in range(10):
            ufo = Ufo(ai_settings, screen)

            ufo.x = ufo_width + 2 * ufo_width * u

            ufo.rect.x = ufo.x
            ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row

            ufoes.add(ufo)


def check_fleet_edges(ai_settings, ufoes):
    '''有ufo到达边缘时采取相应的措施'''
    for u in ufoes.sprites():
        if u.check_edges():
            change_fleet_direction(ai_settings, ufoes)

            break

def change_fleet_direction(ai_settings, ufoes):
    '''将整群下移，并改变它们的方向'''
    for u in ufoes.sprites():
        u.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_ufoes(ai_settings,ufoes):
    #检查ufo信息
    check_fleet_edges(ai_settings, ufoes)
    # 更新ufo群位置
    ufoes.update()
