import turtle
import pygame
import sys
from pygame.locals import *

ventana = pygame.display.set_mode((600, 600))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()