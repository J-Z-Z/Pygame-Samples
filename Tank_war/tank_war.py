import pygame
from pygame.sprite import Group
from settings import Settings
from home import Home
from map import Map
from tank import Tank
from enemy import Enemy
import game_functions as gf

def run_game():
    #游戏初始化，创建一个屏幕对象
    pygame.init()

    tk_settings = Settings()
    screen = pygame.display.set_mode((tk_settings.screen_width,tk_settings.screen_height))
    pygame.display.set_caption("Tank War")

    home = Home(screen,tk_settings)

    map = Map(screen,tk_settings)
    #maps = Group()

    play1 = Tank(screen,tk_settings)
    enemy = Enemy(screen,tk_settings)
    enemy1 = Enemy(screen, tk_settings)
    enemy1.rect.centerx = 100
    enemy2 = Enemy(screen, tk_settings)
    enemy2.rect.centerx = 700
    bullets = Group()
    bullets1 = Group()
    bullets2 = Group()
    bullets3 = Group()

    while True:
        # 监测键盘鼠标事件
        gf.check_events(tk_settings, screen, play1,bullets,bullets1,bullets2,bullets3)

        #有关子弹刷新相关
        gf.update_bullets(tk_settings, bullets, bullets1, bullets2, bullets3)

        #有关屏幕刷新相关
        gf.update_screen(screen,tk_settings,home,map,play1,enemy,enemy1,enemy2,bullets,bullets1,bullets2,bullets3)

run_game()
