import pygame


class Personaje(pygame.sprite.Sprite):
    def __init__(self, tamaño, coor, imagen, velocidad, animaciones: dict) -> None:
        super().__init__()
        self.image = pygame.image.load(imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, tamaño)
        self.rect = self.image.get_rect()
        self.rect.center = coor
        self.lados = self.obtener_rectangulos()
        # ---------------------------------------------------
        self.contador_pasos = 0
        self.estado = "quieto"
        self.animaciones = animaciones
        self.velocidad = velocidad
        # ----------------------------------------------------
        self.gravedad = 1.2
        self.potencia_salto = -14
        self.limite_velocidad_caidad = 14
        self.esta_saltando = True
        self.desplazamiento_y = 0

    def obtener_rectangulos(self):
        diccionario = {}
        principal = self.rect
        diccionario["main"] = principal
        diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 8, principal.width, 8)
        diccionario["right"] = pygame.Rect(principal.right - 8, principal.top, 8, principal.height)
        diccionario["left"] = pygame.Rect(principal.left, principal.top, 8, principal.height)
        diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 8)
        return diccionario

    def animar_player(self, pantalla: pygame.surface.Surface):
        if self.contador_pasos >= len(self.animaciones[self.estado]):
            self.contador_pasos = 0
        pantalla.blit(self.animaciones[self.estado][self.contador_pasos], self.rect)
        self.contador_pasos += 1

    def mover(self):
        if self.estado == "derecha":
            for lado in self.lados:
                self.lados[lado].x += self.velocidad

        elif self.estado == "izquierda":
            for lado in self.lados:
                self.lados[lado].x += self.velocidad * -1

    def update(self, pantalla):
        match self.estado:
            case "derecha":
                if not self.esta_saltando:
                    self.animar_player(pantalla)
                self.mover()
            case "izquierda":
                if not self.esta_saltando:
                    self.animar_player(pantalla)
                self.mover()
            case "quieto":
                if not self.esta_saltando:
                    self.animar_player(pantalla)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "girar":
                if not self.esta_saltando:
                    self.animar_player(pantalla)

        self.aplicar_gravedad(pantalla)

    def aplicar_gravedad(self, pantalla):
        # salto
        if self.esta_saltando:
            self.animar_player(pantalla)
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caidad:
                self.desplazamiento_y += self.gravedad
