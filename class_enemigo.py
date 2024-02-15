import pygame
import random
from config import *
from class_Personaje import Personaje

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, image, tamaño, SPEED, animaciones) -> None:
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image ,tamaño)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, ANCHO)
        self.rect.y = random.randint(-100, 400)
        self.lados = self.obtener_rectangulos()
        self.toco = False
        #animaciones
        self.contador_pasos = 0
        self.estado = "cayendo"
        self.animaciones = animaciones
        self.velocidad = SPEED
        #gravedad
        self.gravedad = 1
        self.potencia_salto = -10
        self.limite_velocidad_caidad = 10
        self.esta_cayendo = True
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
                if not self.esta_cayendo:
                    self.animar(pantalla)
                self.mover()
            case "izquierda":
                if not self.esta_cayendo:
                    self.animar(pantalla)
                self.mover()
            case "cayendo":
                if not self.esta_cayendo:
                    self.esta_cayendo = True
                    self.estado = "derecha"
        if self.esta_cayendo:
            self.aplicar_gravedad(pantalla)
    
    def aplicar_gravedad(self, pantalla): 
        #caida
        if self.esta_cayendo:
            self.animar(pantalla)
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caidad:
                self.desplazamiento_y += self.gravedad




class Enemigo_2(Enemigo):
    def __init__(self, image, tamaño, SPEED, animaciones, ubicacion = None) -> None:
        super().__init__(image, tamaño, SPEED, animaciones)
        self.estado = "cayendo"
        if ubicacion == None:
            self.rect.x = random.randint(100, ANCHO)
            self.rect.y = random.randint(-100, 400)
        else:
            self.rect.x, self.rect.y = ubicacion
        self.lados = self.obtener_rectangulos()
        self.laser = None
        self.gravedad = 0.5
        self.rect_tiro = pygame.rect.Rect((0 ,self.rect.y), (ANCHO, 40))

    def aplicar_gravedad(self, pantalla):
        return super().aplicar_gravedad(pantalla)
    
    def animar(self, pantalla):
        return super().animar(pantalla)
    
    def update(self, pantalla):
        match self.estado:
            case "derecha":
                if not self.esta_cayendo:
                    self.animar(pantalla)
                self.mover()
            case "izquierda":
                if not self.esta_cayendo:
                    self.animar(pantalla)
                self.mover()
            case "cayendo":
                if not self.esta_cayendo:
                    self.esta_cayendo = True
                    self.estado = "derecha"
            case "atacar_derecha":
                if not self.esta_cayendo:
                    self.animar(pantalla)
                self.mover()
            case "atacar_izquierda":
                if not self.esta_cayendo:
                    self.animar(pantalla)
                self.mover()
        if self.esta_cayendo:
            self.aplicar_gravedad(pantalla)
        self.rect_tiro = pygame.rect.Rect((0 ,self.rect.y), (ANCHO, 40))

    
    def atacar(self, derecha: bool):
        if derecha:
            self.estado = "atacar_derecha"
        else:
            self.estado = "atacar_izquierda"


class Boss(Personaje):
    def __init__(self, tamaño, coor, imagen, velocidad, animaciones: dict) -> None:
        super().__init__(tamaño, coor, imagen, velocidad, animaciones)
        self.estado = "quieto"
    
    def animar(self, pantalla):
        return super().animar_player(pantalla)
    
    def atacar(self):
        self.estado = "atacar"
    
    def update(self, pantalla):
        match self.estado:
            case "quieto":
                if not self.esta_saltando:
                    self.animar(pantalla)
            case "muerto":
                if not self.esta_saltando:
                    self.animar(pantalla)
            case "atacar":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
        self.aplicar_gravedad(pantalla)
    
    def aplicar_gravedad(self, pantalla):
        return super().aplicar_gravedad(pantalla)
    def get_atacar(self):
        return self.estado == "atacar"