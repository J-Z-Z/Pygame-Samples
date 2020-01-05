import sys
import pygame
from settings import Settings
from home import Home
from map import Map
from tank import Tank
import game_functions as gf

def run_game():
    #游戏初始化，创建一个屏幕对象
    pygame.init()

    tk_settings = Settings()
    screen = pygame.display.set_mode((tk_settings.screen_width,tk_settings.screen_height))
    pygame.display.set_caption("Tank War")

    home = Home(screen,tk_settings)

    map = Map(screen,tk_settings)

    play1 = Tank(screen,tk_settings)

    while True:
        # 监测键盘鼠标事件
        gf.check_events(play1)

        #有关屏幕刷新相关
        gf.update_screen(screen,tk_settings,home,map,play1)

run_game()
