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


pygame.init()

reloj = pygame.time.Clock()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Practica")

path_caja = caja["imagen"]
path_caja = "images\cajas\caja_nivel2.png"

piso = Piso("images\pisos\piso_2.png", (ANCHO, 70), (0, 525))

plataforma_1 = Piso("images\pisos\piso_2.png", (230, 60), (0, 430))
plataforma_2 = Piso("images\pisos\piso_2.png", (230, 60), (335, 430))
plataforma_3 = Piso("images\pisos\piso_2.png", (230, 60), (670, 430))

plataforma_4 = Piso("images\pisos\piso_2.png", (580, 60), (160, 340))
plataforma_5 = Piso("images\pisos\piso_2.png", (300, 60), (0, 250))
plataforma_6 = Piso("images\pisos\piso_2.png", (300, 60), (600, 250))

caja = Piso(path_caja, (90, 90), (370, 200))
caja_2 = Piso(path_caja, (90, 90), (370+90, 200))
cajas = [caja, caja_2]
plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4, plataforma_5, plataforma_6]

Fuente = pygame.font.SysFont("Segoe Print", 30)


juego = Nivel_2(r"images\Fondos de juego\47792.jpg", plataformas, cajas)

boton_inicio = Bottom(r"images\BOTONES\play.png", 350, 200, (200, 80))
boton_ranking = Bottom(r"images\BOTONES\ranking.png", 350, 400, (200, 80))
mostrar = False


while True:
    reloj.tick(30)  
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    juego.play(eventos)
    pygame.display.flip()


