import pygame
import time
from pygame.sprite import Group
#from pygame.locals import *
from settings import Settings
from ship import Ship
from enemy import Enemy
import game_function as gf



def run_game():
    # pygame初始化
    pygame.init()
    #设置对象初始化
    py_settings = Settings()



    # 设置窗口大小
    screen = pygame.display.set_mode((py_settings.screen_width, py_settings.screen_height))
    # 设置标题
    pygame.display.set_caption("飞机大战")
    #创建一个飞船
    ship1 = Ship(screen)
    #创建一个敌机
    #enemy1 = Enemy(screen)

    # 创建一群敌机
    enemys = Group()

    #创建一个子弹编组
    bullets = Group()

    for i in range(py_settings.enemy_number):
        gf.creat_enemy(screen, enemys)

    # 程序主循环
    while True:
        gf.check_events(screen,py_settings,ship1,bullets)
        gf.update_screen(screen,py_settings,ship1,enemys,bullets)
        gf.update_bullet(bullets,enemys)
        gf.check(ship1,enemys)


if __name__ =="__main__":
    run_game()