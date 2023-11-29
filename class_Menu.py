import pygame
from config import *
import pygame, sys
import pygame
from class_Player import *
from config import *
from class_Piso import *
from class_enemigo import *
from imagenes_sapo import *
from imagenes import *
from class_sapo import Sapo
from class_Plataforma import Plataforma
from class_Bottom import *

class Juego():
    def __init__(self, lista_eventos):
        self.pantalla = pygame.display.set_mode(TAM_PANTALLA)
        self.menu = True
        self.is_running = False
        self.is_game_over = False
        self.options = False
        self.eventos = lista_eventos
        self.boton_play = Bottom(r"images\BOTONES\boton_play.png", 350, 200, (200, 60))
        self.boton_opciones = Bottom(r"images\BOTONES\boton_option.png", 350, 300, (200, 60))
        self.boton_exit = Bottom(r"images\BOTONES\boton_exit.png", 350, 400, (200, 60))

    def run(self):
        self.main()
        self.update()

    def update(self):
        pass
    def main(self):
        if self.menu:
            if self.boton_play.draw(self.pantalla):
                self.menu = not self.menu
            if self.boton_opciones.draw(self.pantalla):
                self.menu = not self.menu
            if self.boton_exit.draw(self.pantalla):
                self.menu = not self.menu

    def leer_inputs(self):
