import pygame
from settings import Settings
import game_functions as gf
from bird import Bird
from building import Building
from pygame.sprite import Group

def run_game():
    #游戏初始化，创建一个屏幕对象
    pygame.init()

    g_settings = Settings()

    screen = pygame.display.set_mode((g_settings.screen_width,g_settings.screen_height),pygame.RESIZABLE)
    pygame.display.set_caption("Flappy Bird")

    bird = Bird(g_settings,screen)

    building = Building(g_settings, screen)


    while True:
        # 监测键盘事件和鼠标事件
        gf.check_events(bird)

        #屏幕刷新相关函数
        gf.update_screen(screen,g_settings,bird,building)



run_game()

