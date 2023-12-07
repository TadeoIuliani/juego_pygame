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


pygame.init()

reloj = pygame.time.Clock()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Practica")
path_caja = caja["imagen"]

piso = Piso("images\pisos\piso.png", (ANCHO, 80), (0, 525))
plataforma_1 = Piso("images\pisos\piso.png", (600, 60), (120, 432))
plataforma_2 = Piso("images\pisos\piso.png", (450, 60), (280, 330))
plataforma_3 = Piso("images\pisos\piso.png", (400, 60), (120, 220))
plataforma_4 = Piso("images\pisos\piso.png", (380, 60), (300, 120))
caja = Piso(path_caja, (80, 80), (120, 354))
caja_2 = Piso(path_caja, (80, 80), (640, 250))
caja_3 = Piso(path_caja, (80, 80), (120, 145))
cajas = [caja, caja_2, caja_3]
plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4]
Fuente = pygame.font.SysFont("Segoe Print", 30)
juego = Nivel(r"images\Fondos de juego\fondo_juego.jpg", plataformas, cajas)

boton_inicio = Bottom(r"images\BOTONES\play.png", 350, 200, (200, 80))
boton_ranking = Bottom(r"images\BOTONES\ranking.png", 350, 400, (200, 80))
mostrar = False
while True:
    mensaje = None
    reloj.tick(27)  
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    boton_inicio.draw(pantalla)
    boton_ranking.draw(pantalla)
    if boton_inicio.is_clicked() == True:
        mensaje = "toco"
        mostrar = True

    if mostrar:
        print(mensaje)
        mostrar = not mostrar
    pygame.display.flip()


