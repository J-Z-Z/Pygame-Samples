import sys
import pygame
from bullet import Bullet
from alien import  Alien

def check_events(ai_settings,screen,ship,bullets):
    '''响应键盘鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #关于使用键盘方向键控制飞船
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        # 检测到键盘按下飞船右移标志变成1
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 检测到键盘按下飞船左移标志变成1
        ship.moving_left = True

    elif event.key == pygame.K_UP:
        # 检测到键盘按下飞船上移标志变成1
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # 检测到键盘按下飞船下移标志变成1
        ship.moving_down = True


    #空格键    子弹的相关设置å
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    '''如果没有达到限制，发射子弹'''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        # 监测到键盘弹起飞船右移标志变成0
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 监测到键盘弹起飞船左移标志变成0
        ship.moving_left = False

    elif event.key == pygame.K_UP:
        # 监测到键盘弹起飞船上移标志变成0
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        # 监测到键盘弹起飞船下移标志变成0
        ship.moving_down = False

def update_screen(ai_settings,screen,ship,bullets,aliens):
    '''更新屏幕上的图像，并刷新到新屏幕'''

    #每次循环时重绘屏幕
    screen.fill(ai_settings.bg_color)

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.blitme()

    ship.blitme()
    aliens.draw(screen)


    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets,aliens,ai_settings,screen,ship):
    '''更新子弹的位置，并删除已经消失的子弹'''
    #更新子弹的位置
    bullets.update()

    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisons(bullets,aliens,ai_settings,screen,ship)




def check_bullet_alien_collisons(bullets,aliens,ai_settings,screen,ship):
    #-----------------------------------
    #检查是否有子弹击中了外星人
    #如果存在子弹击中外星人，那么删除子弹和该外星人
    #------------------------------------
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    #外星人清除干净后生成新的外星人
    if len(aliens) == 0:
        #删除现有的子弹，并且新建一群外星人
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)



def create_fleet(ai_settings,screen,ship,aliens):
    '''创建外星人群'''
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

#创建一行外星人，计算一行可以容纳几个外星人
#外星人间距为外星人宽度
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

#创建一个外星人并加入当前行
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

#计算屏幕可以容纳多少行外星人
def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return  number_rows



def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边缘采取的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    '''将外星人整体往下一个单位，并改变它们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,ship,aliens):
    #检查是否有外星人接触边缘
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #------------
    #检测外星人和飞船之间的碰触
    #------------

    if pygame.sprite.spritecollideany(ship,aliens):
        print('飞船已撞毁!!!')



