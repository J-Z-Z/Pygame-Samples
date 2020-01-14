import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("飞船大战外星人")


    #创建一个飞船对象
    ship = Ship(screen)

    '''
    #创建一个ufo对象
    ufo = Ufo(ai_settings,screen)
    '''


    ufoes = Group()

    bullets = Group()
    bullets1 = Group()
    bullets2 = Group()

    #创建ufo群
    gf.create_fleet(ai_settings,screen,ufoes)

    while True:
        #监测键盘鼠标事件的相关内容
        gf.check_events(ai_settings,screen,ship,bullets,bullets1,bullets2)

        ship.update()

        #更新子弹相关
        gf.update_bullets(ai_settings, screen, ship, ufoes,bullets,bullets1,bullets2)

        #更新ufo相关
        gf.update_ufoes(ai_settings, ufoes)

        #更新屏幕相关内容
        gf.update_screen(ai_settings,screen,ship,ufoes,bullets,bullets1,bullets2)



run_game()