from typing import Any
import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, imagen, coor, direccion = True):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
        self.rect.center = coor
        self.direccion = direccion

    def mover(self):
        if self.direccion:
            self.rect.x += 20
        else:
            self.rect.x -= 20

    def update(self, pantalla) -> None:
        self.mover()
        pantalla.blit(self.image, self.rect)
