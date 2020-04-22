import pygame

class Settings():
    def __init__(self):

        self.screen_width = 280
        self.screen_height = 500

        self.bg_image_1 = pygame.image.load("pic/background_1.png")
        self.bg_image_0 = pygame.image.load("pic/background_0.png")
        self.g_image = pygame.image.load("pic/ground.png")
