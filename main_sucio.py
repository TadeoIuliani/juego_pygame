import pygame, sys
import pygame
from class_Player import *
from config import *
from class_Piso import *
from class_enemigo import *
from imagenes import *
from class_sapo import Sapo
from class_Plataforma import Plataforma
from class_Bottom import *
from class_Nivel import *
from class_Nivel2 import Nivel_2
from class_Nivel3 import *


pygame.init()

reloj = pygame.time.Clock()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Practica")

path_caja = caja["imagen"]
path_caja = "images\cajas\caja_nivel2.png"

piso = Piso("images\pisos\piso_3.png", (ANCHO, 70), (0, 530))

plataforma_1 = Piso("images\pisos\piso_3.png", (400, 60), (100, 430))
plataforma_2 = Piso("images\pisos\piso_3.png", (400, 60), (0, 340))

plataforma_3 = Piso("images\pisos\piso_3.png", (400, 60), (100, 240))

plataforma_4 = Piso("images\pisos\piso_3.png", (400, 60), (0, 140))

plataforma_5 = Piso("images\pisos\piso_3.png", (300, 75), ((ANCHO - 300), 340))

cajas = []
plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4, plataforma_5]

Fuente = pygame.font.SysFont("Segoe Print", 30)


juego = Nivel3(r"images\Fondos de juego\vecteezy_alien-planet-game-background_6316482.jpg", plataformas, cajas)

fondo = pygame.image.load(r"images\Fondos de juego\47792.jpg")
fondo = pygame.transform.scale(fondo, (TAM_PANTALLA))

mostrar = False

bala = None
vida_bala = False

while True:
    reloj.tick(30)  
    eventos = pygame.event.get()
    mouse = pygame.mouse.get_pos()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    juego.play(eventos)
    pygame.display.flip()


