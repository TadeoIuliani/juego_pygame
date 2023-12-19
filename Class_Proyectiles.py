from typing import Any
import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, imagen, coor, velocidad, direccion = True):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
        self.rect.center = coor
        self.direccion = direccion
        self.velocidad = velocidad

    def mover(self):
        if self.direccion:
            self.rect.x += self.velocidad
        else:
            self.rect.x -= self.velocidad

    def update(self, pantalla) -> None:
        self.mover()
        pantalla.blit(self.image, self.rect)
