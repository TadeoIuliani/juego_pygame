import pygame, sys
from class_Player import *
from class_enemigo import *
from class_item import *
from class_Piso import *
from class_sapo import Sapo
from main_cronometro import Cronometro
from class_Nivel import *
from config import *
from imagenes import *
from config import *

class Nivel3(Nivel):
    def __init__(self, fondo_path, plataformas, cajas) -> None:
        super().__init__(fondo_path, plataformas, cajas)
        self.boss = Boss("images\boss_sprites\sprites_boss_1-removebg-preview.png", (150, 130), 4, imagenes_boss)
        self.lista_enemigos.append(self.boss)
    