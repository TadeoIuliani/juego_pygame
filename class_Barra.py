import pygame, sys
from config import *

class Barra():
    def __init__(self, x, y , ancho, largo, color_fondo, color_carga, segundos, total) -> None:
        self.ancho = ancho
        self.largo = largo
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.largo)
        self.segundos = segundos
        self.total = total
        self.carga_porcentaje = int((self.segundos / self.total) * 100)
        self.calculo_barra = int((self.carga_porcentaje * self.ancho) / 100)
        self.color_fondo = color_fondo
        self.color_carga = color_carga
        self.rect_carga = pygame.Rect(self.x, self.y, self.calculo_barra, self.largo)
    
    def actualizar(self, pantalla, segundos):
        self.carga_porcentaje = int((segundos / self.total) * 100)
        self.calculo_barra = int((self.carga_porcentaje * self.ancho) / 100)
        self.rect_carga = pygame.Rect(self.x, self.y, self.calculo_barra, self.largo)
        pygame.draw.rect(pantalla, self.color_fondo, self.rect, 3)
        pygame.draw.rect(pantalla, self.color_carga, self.rect_carga)
