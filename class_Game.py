import pygame, sys
from class_Nivel import *
from config import *

class Game():
    def __init__(self) -> None:
        self.nivel = Nivel()
        # game play()
        self.sprites = imagenes_menu
        self.pantalla = pygame.display.set_mode(TAM_PANTALLA)
        #Botones y portada de nieveles
        # self.fondo = menu['BG']
        # self.game_levels = Options((self.WIDTH // 2, 383),self.sprites['GAME_LEVELS'])
        # self.escape = Options((self.WIDTH // 2, 457),self.sprites['QUIT'])
        # self.level_1_portada =  Options((self.WIDTH // 2, 450),self.sprites['PORTADA_1'])
        # self.level_2_portada =  Options((self.WIDTH // 2, 680),self.sprites['PORTADA_2'])
        # self.go_back =  Options((50, 715),self.sprites['ARROW'])
    def run(self):
        while True:
            reloj = pygame.time.Clock()
            reloj.tick(FPS)
            self.leer_inputs()
    
    def leer_inputs(self):
        eventos = pygame.event.get()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if boton_inicio.draw(pantalla):
            nivel_actual = juego
            break
        if boton_opciones.draw(pantalla):
            nivel_actual = juego
            break
    
        if boton_exit.draw(pantalla):
            pygame.quit()
            sys.exit()
    
    def update(self):
        #fondo
        self.pantalla.blit(self.fo)