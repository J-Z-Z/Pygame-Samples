import pygame
from settings import Settings
import game_functions as gf
from bird import Bird
from building import Building

def run_game():
    #游戏初始化，创建一个屏幕对象
    pygame.init()

    g_settings = Settings()

    screen = pygame.display.set_mode((g_settings.screen_width,g_settings.screen_height),pygame.RESIZABLE)
    pygame.display.set_caption("Flappy Bird")

    bird = Bird(g_settings,screen)

    building = Building(g_settings, screen)

    building1 = Building(g_settings, screen)
    building1.rect1.x = building1.rect1.x + 200
    building1.rect2.x = building1.rect2.x + 200

    building2 = Building(g_settings, screen)
    building2.rect1.x = building1.rect1.x + 400
    building2.rect2.x = building1.rect2.x + 400

    building3 = Building(g_settings, screen)
    building3.rect1.x = building1.rect1.x + 600
    building3.rect2.x = building1.rect2.x + 600

    building4 = Building(g_settings, screen)
    building4.rect1.x = building1.rect1.x + 800
    building4.rect2.x = building1.rect2.x + 800


    while True:
        # 监测键盘事件和鼠标事件
        gf.check_events(bird)

        #屏幕刷新相关函数
        gf.update_screen(screen,g_settings,bird,building,building1,building2,building3,building4)



run_game()

