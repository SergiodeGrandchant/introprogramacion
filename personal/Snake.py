import turtle
import pygame
import sys
from pygame.locals import *

ventana = pygame.display.set_mode((600, 500))
pluma = turtle.Turtle()

pluma.speed(5)
for i in range(0, 4):
    pluma.forward(100)
    pluma.left(90)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()