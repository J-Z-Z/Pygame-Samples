import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():

    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("飞船大战外星人")

    #创建一个Button
    play_button = Button(ai_settings, screen, "Play")

    #创建一个用于存储统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一个记分牌
    sb = Scoreboard(ai_settings, screen, stats)

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
        gf.check_events(ai_settings,screen,stats,play_button,ship,ufoes,bullets,bullets1,bullets2)

        if stats.game_active:

            ship.update()

            # 更新子弹相关
            gf.update_bullets(ai_settings, screen, stats,sb, ufoes,bullets,bullets1,bullets2)

            # 更新ufo相关
            gf.update_ufoes(ai_settings, stats, screen, ship, ufoes, bullets, bullets1, bullets2)

        # 更新屏幕相关内容
        gf.update_screen(ai_settings,screen,stats,sb,ship,ufoes,bullets,bullets1,bullets2,play_button)




run_game()