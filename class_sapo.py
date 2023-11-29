import pygame
from config import *
import random

class Sapo(pygame.sprite.Sprite):
    def __init__(self, image, tamaño, SPEED, animaciones) -> None:
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image ,tamaño)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, ANCHO)
        self.rect.y = random.randint(-100, ALTO - 100)
        self.lados = self.obtener_rectangulos()
        #animaciones
        self.contador_pasos = 0
        self.estado = "cayendo"
        self.animaciones = animaciones
        self.velocidad = SPEED
        #gravedad
        self.gravedad = 1
        self.potencia_salto = -12
        self.limite_velocidad_caidad = 12
        self.esta_saltando = True
        self.desplazamiento_y = 0

    def animar(self, pantalla):
        if self.contador_pasos >= len(self.animaciones[self.estado]):
            self.contador_pasos = 0
        pantalla.blit(self.animaciones[self.estado][self.contador_pasos], self.rect)
        self.contador_pasos += 1
    
    def mover(self):
                    
        if self.estado == "derecha":
            for key in self.lados:   
                self.lados[key].x += self.velocidad
            if self.rect.right >= ANCHO:
                self.rect.right = ANCHO
                self.estado = "izquierda"

        elif self.estado == "izquierda":
            for key in self.lados:   
                self.lados[key].x -= self.velocidad 
            if self.rect.x < 0:
                self.estado = "derecha"

        if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
        
        
    def obtener_rectangulos(self):
        diccionario = {}
        diccionario["main"] = self.rect
        diccionario["bottom"] = pygame.Rect(self.rect.left, self.rect.bottom -6, self.rect.width, 6)
        diccionario["right"] = pygame.Rect(self.rect.right -6, self.rect.top, 6, self.rect.height)
        diccionario["left"] = pygame.Rect(self.rect.left, self.rect.top, 6, self.rect.height)
        diccionario["top"] = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 6)
        return diccionario
    
    def update(self, pantalla): 
        match self.estado:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla)
                self.mover()
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla)
                self.mover()
            case "cayendo":
                if not self.esta_saltando:
                    self.esta_cayendo = True
                    self.estado = "izquierda"
            # case "salta":
            #     if not self.esta_saltando:
            #         self.esta_saltando = True
            #         self.desplazamiento_y = self.potencia_salto
        if self.esta_saltando:
            self.aplicar_gravedad(pantalla)
    
    def aplicar_gravedad(self, pantalla): 
        #caida
        if self.esta_saltando:
            self.animar(pantalla)
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caidad:
                self.desplazamiento_y += self.gravedad
