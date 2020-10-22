import pygame
import sys

game_over = False

#Constantes
ANCHO = 800
ALTO = 600

#Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
# naranja
HC74225 = (199, 66, 37)
# verde claro
H61CD35 = (97, 205, 53)

#Jugador
jugador_pos = [400, 400]
jugador_talla = 50

#dimenciones de la pantalla
ventana = pygame.display.set_mode((ANCHO, ALTO))


#Dibujo del pesonaje
pygame.draw.rect(ventana, rojo, (jugador_pos[0], jugador_pos[1], jugador_talla, jugador_talla ))
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        #con un print event es como un mapeo de la pantalla a usasr
        # print(event)

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass

