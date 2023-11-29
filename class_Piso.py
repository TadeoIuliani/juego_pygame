import pygame


class Piso(pygame.sprite.Sprite):
    def __init__(self, image, tamaño, ubicacion):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, tamaño)
        self.rect = self.image.get_rect()
        self.rect.topleft = ubicacion
        self.lados = self.obtener_rectangulos()

    def obtener_rectangulos(self):
        diccionario = {}
        principal = self.rect
        diccionario["main"] = principal
        diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 8, principal.width, 8)
        diccionario["right"] = pygame.Rect(principal.right - 8, principal.top, 8, principal.height)
        diccionario["left"] = pygame.Rect(principal.left, principal.top, 8, principal.height)
        diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 8)
        return diccionario

    def update(self, pantalla) -> None:
        pass
