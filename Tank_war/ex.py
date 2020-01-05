import cv2
import pygame


img = cv2.imread('images/player1.bmp')

#输出的顺序的是高度、宽度、通道数(32, 224, 3)
print(img.shape)

img[0:32,0:32]

image = pygame.image.load('images/瓷砖tile.bmp').convert()
print(image)
