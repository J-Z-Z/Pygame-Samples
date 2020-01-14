import sys
#from time import sleep
import pygame
from bullet import Bullet
from bullet1 import Bullet1
from bullet2 import Bullet2
from ufo import Ufo

def check_events(ai_settings,screen,stats,play_button,ship,ufoes,bullets,bullets1,bullets2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True

            #开火
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(ai_settings,screen,ship)
                bullets.add(new_bullet)
                new_bullet1 = Bullet1(ai_settings, screen, ship)
                bullets1.add(new_bullet1)
                new_bullet2 = Bullet2(ai_settings, screen, ship)
                bullets2.add(new_bullet2)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,ufoes,bullets,bullets1,bullets2, mouse_x, mouse_y)

def check_play_button(ai_settings,screen,stats, play_button,ship,ufoes,bullets,bullets1,bullets2, mouse_x, mouse_y):
    #点击Play开始游戏
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        # 清空外星人列表和子弹列表 aliens.empty()
        bullets.empty()
        bullets1.empty()
        bullets2.empty()
        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ufoes)
        ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,ufoes,bullets,bullets1,bullets2,play_button):
    screen.fill(ai_settings.bg_color)

    for i in bullets.sprites():
        i.draw_bullet()

    for j in bullets1.sprites():
        j.draw_bullet()

    for k in bullets2.sprites():
        k.draw_bullet()


    ship.blitme()

    ufoes.draw(screen)

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()


    pygame.display.flip()




def update_bullets(ai_settings, screen, stats,sb, ufoes,bullets,bullets1,bullets2):
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

    if collisions or collisions1 or collisions2:
        stats.score += ai_settings.alien_points
        sb.prep_score()


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

def update_ufoes(ai_settings, stats, screen, ship, ufoes, bullets, bullets1, bullets2):
    #检查ufo信息
    check_fleet_edges(ai_settings, ufoes)
    # 更新ufo群位置
    ufoes.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, ufoes):
        #print("Ship hit!!!")
        ship_hit(ai_settings, stats, screen, ship, ufoes, bullets, bullets1, bullets2)
    check_aliens_bottom(ai_settings, stats, screen, ship, ufoes, bullets, bullets1, bullets2)

def ship_hit(ai_settings, stats, screen, ship, ufoes, bullets,bullets1,bullets2):

    if stats.ships_left > 0:

        stats.ships_left -= 1

        # 清空ufo列表和子弹列表
        ufoes.empty()
        bullets.empty()
        bullets1.empty()
        bullets2.empty()

        # 创建一群新的ufo，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ufoes)
        ship.center_ship()

        # 暂停
        #sleep(1)

    else:
        stats.game_active = False




def check_aliens_bottom(ai_settings, stats, screen, ship, ufoes, bullets, bullets1, bullets2):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for u in ufoes.sprites():
        if u.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, ufoes, bullets,bullets1,bullets2)
            break