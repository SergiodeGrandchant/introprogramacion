import pygame, sys
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((500,400))
pygame.display.set_caption("Color de FONDO, Paleta de COLORES y FORMAS GEOMÉTRICAS")

#colores basicos
blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)

#naranja
HC74225 = (199,66,37)
#verde claro
H61CD35 = (97,205,53)

#poner fondo
pantalla.fill(blanco)

#figuras geometricas
#los pixeles vas de (x , y)

#rectangulo
rectangulo = pygame.draw.rect(pantalla,rojo,(100, 50, 100, 50))
print(rectangulo)

#lineas
pygame.draw.line(pantalla , verde, (100,104),(199,104),10)

#circulos
pygame.draw.circle(pantalla , negro, (122,250), 20, 0)

#ellipse
#uso de superposicion
pygame.draw.ellipse(pantalla, HC74225, (275, 200, 40, 80), 0)
pygame.draw.ellipse(pantalla, H61CD35, (275, 200, 40, 80), 10)

#poligonos
puntos = [(100, 300), (100, 100), (150, 100)]
pygame.draw.polygon(pantalla, (0, 150, 255), puntos, 8)

#bucle del juego
#Este while simpre se mantendra en true y solo tiene la posibilidad de salir con el if
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

#aaaaa concha culo ufffff el sergio es gay y bien loca -ñlfddahhh  el sergi es misdffsfdf