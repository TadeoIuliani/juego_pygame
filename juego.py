import pygame, sys
import pygame
from class_Player import *
from config import *
from class_Piso import *
from class_enemigo import *
from class_Nivel import *
from class_Bottom import *
from class_Plataforma import *
from imagenes import *

pygame.init()
reloj = pygame.time.Clock()

pantalla = pygame.display.set_mode(TAM_PANTALLA)

fondo_menu = pygame.image.load("images\pisos\menu juego.png")
# fondo_menu = pygame.transform.scale(fondo_menu, TAM_PANTALLA)

player = Player(TAM_CRASH, CENTER, "Crash\Crash Quieto\Crash Style_1 (1).png", 7, imagenes_player, 3)
fruta = Item(imagenes_fruta, r"images\frutitas\0.png", TAM_ITEM)

plataforma_principal = Piso("images\pisos\piso.png", (ANCHO, 100), (0, 550))
piso_izquierda = Piso("images\pisos\piso.png", (250, 50), (0, 450))
piso_derecha = Piso("images\pisos\piso.png", (250, 50), ((ANCHO - 250), 450))
plataformas = [plataforma_principal, piso_izquierda, piso_derecha]

enemigo = Enemigo(r"images\cangrejos\0.png", TAM_CANGRI, (ANCHO / 2, ALTO / 2), 7, imagenes_cangrejos)   

juego = Nivel(pantalla, player, fruta, enemigo, plataformas, juego["fondo"])

boton_inicio = Bottom(r"images\BOTONES\boton_play.png", 350, 200, (200, 60))
boton_opciones = Bottom(r"images\BOTONES\boton_option.png", 350, 300, (200, 60))
boton_exit = Bottom(r"images\BOTONES\boton_exit.png", 350, 400, (200, 60))



while True:
    pantalla.fill(BLANCO, pantalla.get_rect())
    pantalla.blit(fondo_menu, (300, 100))

    if boton_inicio.draw(pantalla):
        nivel_actual = juego
        break
    if boton_opciones.draw(pantalla):
        nivel_actual = juego
        break
    
    if boton_exit.draw(pantalla):
        pygame.quit()
        sys.exit()
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

while True:
    reloj.tick(27)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    juego.update(eventos)

    pygame.display.flip()
