import pygame
#from pygame.locals import *
import sys
import random
from  bullet import Bullet
from enemy import Enemy



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

def creat_enemy(screen,enemys):
    new_enemy = Enemy(screen)
    new_enemy.rect.x = random.randint(50,350)
    new_enemy.rect.y = -(random.randint(20,1000))
    enemys.add(new_enemy)


def update_screen(screen,py_settings,ship1,enemys,bullets):
    screen.blit(py_settings.bg_image, (0, 0))
    ship1.blitme()
    #enemy1.blitme()
    ship1.update(py_settings)

    #绘制所有的敌机
    for enemy in enemys.sprites():
        enemy.blitme()

    #绘画每一颗子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet(screen)
    #bullets.draw_bullet()

    enemys.update(py_settings)

    pygame.display.flip()



def update_bullet(bullets,enemys):

    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))

    #检查子弹是否击中机
    collisions = pygame.sprite.groupcollide(bullets,enemys,True,True)
    #print(collisions)

def check(ship1,enemys):
    if pygame.sprite.spritecollideany(ship1,enemys):
        print("game over")
        ship1.image = pygame.image.load("boom.png")