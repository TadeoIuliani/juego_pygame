import pygame, sys

from class_Player import *
from class_enemigo import *
from class_item import *
from class_Piso import *
from config import *
from imagenes import *
from config import *


class Nivel:
    def __init__(self, tamaño_pantalla, player : Player, item,
                enemigo, plataformas, fondo_pantalla) -> None:
        self.pantalla = tamaño_pantalla
        self.fondo = pygame.image.load(fondo_pantalla) 
        self.fondo = pygame.transform.scale(self.fondo, (ANCHO, ALTO))
        self.player = player
        self.plataformas = []
        self.plataformas = plataformas
        self.lista_items = []
        self.lista_items.append(item)
        self.enemigo = enemigo
        self.lista_enemigos = []
        self.lista_enemigos.append(enemigo)
        self.laser = None
        self.bala_viva = False
        self.puntuacion = 0
        self.Fuente = pygame.font.SysFont("Arial", 30)
        self.vidas = 3


    def update(self, lista_eventos):
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if self.bala_viva == False:
                        self.laser = Laser("images\disparo.png", self.player.rect.bottomright)
                        self.bala_viva = True
                elif event.key == pygame.K_z:
                    if self.bala_viva == False:
                        self.laser = Laser("images\disparo.png", self.player.rect.bottomleft, False)
                        self.bala_viva = True
        self.leer_inputs()
        self.collisiones()
        self.actualizar_pantalla()


    def leer_inputs(self):
        teclas_presionadas = pygame.key.get_pressed()
        if teclas_presionadas[pygame.K_LEFT] and self.player.rect.left > ANCHO / ANCHO + 7:
            self.player.estado = "izquierda"
        elif teclas_presionadas[pygame.K_RIGHT] and self.player.rect.right < ANCHO - SPEED:
            self.player.estado = "derecha"
        elif teclas_presionadas[pygame.K_SPACE]:
            self.player.estado = "salta"
        elif teclas_presionadas[pygame.K_x] or teclas_presionadas[pygame.K_z]:
            self.player.estado = "girar"
        else:
            self.player.estado = "quieto"

    def collisiones(self):
        for i in range(len(self.plataformas)):
            if self.player.lados["bottom"].colliderect(self.plataformas[i].lados["top"]):
                self.player.esta_saltando = False
                break
            self.player.esta_saltando = True
        
        for i in range(len(self.plataformas)):
            if self.enemigo.rect.colliderect(self.plataformas[i].rect):
                self.enemigo.esta_cayendo = False
                self.enemigo.lados["bottom"].top = self.plataformas[i].lados["top"].top + 4
        
        for i in range(len(self.plataformas)):
            plataforma_principal = self.plataformas[i]
            for i in range(len(self.lista_items)):
                if colision_fruta_plataforma(self.lista_items[i], plataforma_principal):
                    self.lista_items[i].esta_cayendo = False

        for i in range(len(self.lista_items)):
            if colision_fruta_player(self.lista_items[i], self.player):
                self.lista_items.remove(self.lista_items[i])
                self.puntuacion += 200


        if self.enemigo.rect.colliderect(self.player.rect):
            self.vidas -= 1


        if self.bala_viva:
            for i in range(len(self.lista_enemigos)):
                if self.lista_enemigos[i].rect.colliderect(self.laser.rect):
                    self.lista_enemigos.remove(self.lista_enemigos[i])
                    self.bala_viva = False
            
            if self.laser.rect.x < 0:
                self.bala_viva = False
        
            if self.laser.rect.x >= ANCHO:
                self.bala_viva = False

        if len(self.lista_items) == 0:
            self.lista_items = crear_objetos_random(Item, imagenes_fruta, r"images\frutitas\0.png", TAM_ITEM, 1)

        if len(self.lista_enemigos) == 0:
            self.enemigo = Enemigo(r"images\cangrejos\0.png", TAM_CANGRI, (ANCHO / 2, ALTO / 2), 7, imagenes_cangrejos)
            self.lista_enemigos.append(self.enemigo)


    def actualizar_pantalla(self):
        self.pantalla.blit(self.fondo, (0, 0))
        for i in range(len(self.plataformas)):
            self.pantalla.blit(self.plataformas[i].image, self.plataformas[i].rect)


        for i in range(len(self.lista_items)):
            self.lista_items[i].update(self.pantalla)
            
        for key in self.enemigo.lados:
            pygame.draw.rect(self.pantalla, AZUL, self.enemigo.lados[key], 2)

        self.pantalla.blit(self.Fuente.render(f"X{self.vidas}", 0, NEGRO), (50, 20))
        self.pantalla.blit(self.Fuente.render(f"Puntos: {self.puntuacion}", 0, NEGRO), (200, 20))

        for i in range(len(self.lista_enemigos)):
            self.lista_enemigos[i].update(self.pantalla)

        self.player.update(self.pantalla)
        if self.bala_viva:
            self.laser.update(self.pantalla)
        

