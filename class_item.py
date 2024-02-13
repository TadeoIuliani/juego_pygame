import pygame
from config import *
import random
from class_Player import *


class Item(pygame.sprite.Sprite):
    def __init__(self, animacion, imagen, tamaño) -> None:
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, tamaño)
        self.rect = self.image.get_rect()
        self.center = self.random_coor()
        self.lados = self.obtener_rectangulos()
        self.estado = "girando"
        ###
        self.animacion = animacion
        self.tamaño = tamaño
        self.contador_pasos = 0
        # gravedad
        self.gravedad = 1
        self.potencia_salto = -10
        self.limite_velocidad_caidad = 10
        self.esta_cayendo = True
        self.desplazamiento_y = 0

    def animar(self, pantalla: pygame.surface.Surface):
        if self.contador_pasos >= len(self.animacion[self.estado]):
            self.contador_pasos = 0
        pantalla.blit(self.animacion[self.estado][self.contador_pasos], self.rect)
        self.contador_pasos += 1

    def update(self, pantalla):
        if self.esta_cayendo:
            self.mover()
        self.animar(pantalla)

    def mover(self):
        if self.esta_cayendo:
            self.desplazamiento_y = self.potencia_salto
            for lado in self.lados:
                self.lados[lado].y -= self.desplazamiento_y

    def obtener_rectangulos(self):
        diccionario = {}
        principal = self.rect
        diccionario["main"] = principal
        diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 9, principal.width, 9)
        diccionario["right"] = pygame.Rect(principal.right - 4, principal.top, 4, principal.height)
        diccionario["left"] = pygame.Rect(principal.left, principal.top, 4, principal.height)
        diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 9)
        return diccionario

    def random_coor(self):
        x = random.randint(10, 790)
        self.rect.x = x
        y = random.randint(-400, 500)
        self.rect.y = y
        return x, y

class Bomba(Item):
    def __init__(self, animacion, imagen, tamaño) -> None:
        super().__init__(animacion, imagen, tamaño)
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, tamaño)
        self.estado = "cayendo"
        self.explosion = False
        self.potencia_salto = -5
    
    def animar(self, pantalla: pygame.surface.Surface):
        if self.contador_pasos >= len(self.animacion[self.estado]): 
            self.contador_pasos = 0
            if self.estado == "explosion":
                self.explosion = True
    
        pantalla.blit(self.animacion[self.estado][self.contador_pasos], self.rect)
        self.contador_pasos += 1
    
    def get_explosion(self):
        return self.explosion
    
    def update(self, pantalla):
        if self.esta_cayendo:
            self.mover()
        self.animar(pantalla)

