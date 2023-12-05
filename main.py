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
#pantalla----------------------------------------------------------
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Practica")
fondo = pygame.image.load(r"images\Fondos de juego\fondo_juego.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

#player---------------------------------------------------------------------------------------------
player = Player(TAM_CRASH, CENTER, "Crash\Crash Quieto\Crash Style_1 (1).png", 7, imagenes_player, 3)

#plataformas---------------------------------------------------------------------------------------
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


fruta = Item(imagenes_fruta, r"images\frutitas\0.png", TAM_ITEM)

#generadorEnemigos----------------------------------------------------------------------------
generador_cangrejos = GenearadorEnemigos(r"images\cangrejos\0.png", TAM_CANGRI, 7, imagenes_cangrejos)
generador_sapos = GenearadorEnemigos(r"images\sapos\0.png", (40, 30), 5, animaciones_sapo)
lista_enemigos = generador_cangrejos.generar_enemigos(Enemigo, 2)
lista_sapos = generador_sapos.generar_enemigos(Sapo, 3)

#vidas----------------------------
vidas = 3
#puntuacion-----------------------
puntuacion = 0


Fuente = pygame.font.SysFont("Segoe Print", 30)
lista_frutas = [fruta]


#Menu--------------------------------------------------------------------
boton_inicio = Bottom(r"images\pisos\boton_play.png", 350, 200, (200, 80))
boton_opciones = Bottom(r"images\pisos\boton_opciones.png", 350, 300, (200, 80))
boton_exit = Bottom(r"images\pisos\boton_exit.png", 350, 400, (200, 80))
boton_musica = Bottom(r"images\BOTONES\MUSICA.png", 350, 400, (306, 123))
fondo_menu = pygame.image.load("images\pisos\menu juego.png")


#game_over----------------------------------------------------------------
imagen_game_over = pygame.image.load("images\pngegg.png")
imagen_game_over = pygame.transform.scale(imagen_game_over, (250, 150))
fondo_fin_juego = pygame.image.load("images\Fondos de juego\Fondo de juego.jpg")
fondo_fin_juego = pygame.transform.scale(fondo_fin_juego, (ANCHO, ALTO))

#banderas_secundarias---------------------------------------------
laser = None
bala_viva = False
rectangulos_prog = False
volumen = True
#banderas_claasGame--------------------------------------------------
on = True
menu = True
jugando = False
gano = False
pausa = False
config = False
ranking = False

#sound-------------------------------------------------------------------
# pygame.mixer.music.load("sounds\musica-espera-separador-musical-.mp3")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.3)


#Funciona
while on:
    # print(f"Menu {menu} / jugando {jugando} / config {config} / ranking {ranking}")
    eventos = pygame.event.get()
    if menu:
        print("Estoy en Menu")
        jugando = False
        config = False
        ranking = False
        pantalla.fill(NEGRO)
        pantalla.fill((45, 158, 196))
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if boton_inicio.draw(pantalla):
            juego = Nivel(r"images\Fondos de juego\fondo_juego.jpg", plataformas, cajas)
            menu = False
            jugando = True
        if boton_opciones.draw(pantalla):
            menu = False
            config = True
        if boton_exit.draw(pantalla):
            on = False
            pygame.quit()
            sys.exit()
        pygame.display.flip()
    elif jugando and config == False:
        reloj.tick(27)  
        eventos = pygame.event.get()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        juego.play(eventos)
        if juego.get_estado_juego():
            if juego.get_resultado() == False:
                gano = False
            else:
                gano = True
            jugando = False
        pygame.display.flip()

    elif config:
        print("Estoy en configuracion")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                menu = True
                config = False
        pantalla.fill(NEGRO)
        # if boton_musica.draw(pantalla): 
        #     volumen = not volumen
        # if volumen:
        #     pygame.mixer.music.set_volume(0.3)
        # else:
        #     pygame.mixer.music.set_volume(0.0)

        # pantalla.blit(Fuente.render("Opciones...", 0, VERDE), (300, 300))
        pygame.display.flip()


    else:
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pantalla.blit(fondo_fin_juego, (0, 0))
        pantalla.blit(imagen_game_over, (340, 90))
        if gano:
            pantalla.blit(Fuente.render(f"GANO!!!!! {juego.get_puntuacion()}", 0, VERDE), (300, 300))
        else:
            pantalla.blit(Fuente.render(f"Perdio {juego.get_puntuacion()}", 0, VERDE), (300, 300))
        pygame.display.flip()
