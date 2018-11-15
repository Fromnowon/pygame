import pygame
import os

pygame.init()
screen = pygame.display.set_mode((480, 852))
bg = pygame.image.load('./Assert/images/background.png')
screen.blit(bg, (0, 0))
pygame.display.update()
os.system("pause")
# if input():
#     pygame.quit()
