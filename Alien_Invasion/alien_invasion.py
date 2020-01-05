import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group

def run_game():
    #游戏初始化，创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien_Invasion')

    #创建一个飞船
    ship = Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    #创建一个外星人
    #alien = Alien(ai_settings,screen)

    # 创建一个用于存储外星人的编组
    aliens = Group()

    gf.create_fleet(ai_settings,screen,ship,aliens)


    #设置背景色
    bg_color = (ai_settings.bg_color)

    #开始游戏主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets,aliens,ai_settings,screen,ship)
        gf.update_aliens(ai_settings,ship,aliens)
        # print(len(bullets))检测当前子弹的数量
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)

run_game()