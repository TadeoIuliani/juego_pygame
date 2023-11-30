import pygame
from class_Player import *
from class_item import *

ANCHO = 900
ALTO = 600

ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
NARANJA = (255, 128, 0)
ROSA = (217, 74, 177)
AMARILLO = (255, 255, 0)
CELESTE = (0, 255, 255)

color_random = []
color_random.append(ROJO)
color_random.append(VERDE)
color_random.append(AZUL)
color_random.append(BLANCO)
color_random.append(NARANJA)
color_random.append(ROSA)
color_random.append(CELESTE)
color_random.append(AMARILLO)

FPS = 40
SPEED = 10

CENTER = (ANCHO // 10, ALTO - 200)


TAM_CRASH = (60, 80)
TAM_CANGRI = (50, 50)
TAM_ITEM = (30, 30)
TAM_PANTALLA = (ANCHO, ALTO)

def reescalar_imagenes(lista_image, tamaño):
    import pygame

    for i in range(len(lista_image)):
        lista_image[i] = pygame.transform.scale(lista_image[i], tamaño)
    return lista_image


def rotar_imagen(lista_original, flip_x, flip_y):
    lista_nueva = []
    for imagen in lista_original:
        lista_nueva.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_nueva


def crear_objetos_random(clase, animaciones, imagen, tamaño, cantidad):
    lista = []
    for i in range(cantidad):
        objeto = clase(animaciones, imagen, tamaño)
        lista.append(objeto)
    return lista


def colision_fruta_otro_objeto(fruta, objeto):
    if objeto.rect.colliderect(fruta.rect):
        return True
    else:
        return False


def colision_fruta_plataforma(fruta, plataformas):
    for piso in plataformas:
        if fruta.rect.colliderect(piso.rect):
            return True
    return False

class GenearadorEnemigos():
    def __init__(self, image, tamaño, speed, animaciones) -> None:
        self.image = image
        self.tamaño = tamaño
        self.speed = speed
        self.animaciones = animaciones

    def generar_enemigos(self, clase, cantidad):
        lista = []
        for i in range(cantidad):
            object = clase(self.image, self.tamaño, self.speed, self.animaciones)
            lista.append(object)
        return lista

def collision_player_plataformas(player, lista_plataformas):
    for plataforma in lista_plataformas:
        if player.lados["bottom"].colliderect(plataforma.lados["top"]):
            player.esta_saltando = False
            break
        else:
            player.esta_saltando = True
        

def collision_player_caja(player, lista_caja):
    for caja in lista_caja:
        if player.lados["bottom"].colliderect(caja.lados["top"]):
            player.esta_saltando = False

def collision_enemigos_plataformas(enemigos, plataformas):
    for enemigo in enemigos:
        for piso in plataformas:
            if enemigo.lados["bottom"].colliderect(piso.lados["top"]):
                enemigo.esta_cayendo = False
                enemigo.lados["bottom"].top = piso.lados["top"].top + 4
                if enemigo.rect.right >= piso.rect.right:
                    enemigo.estado = "izquierda"
                elif enemigo.rect.left <= piso.rect.left:
                    enemigo.estado = "derecha"
            # else:
            #     enemigo.esta_cayendo = True

def collision_sapo_plataformas(sapos, plataformas):
    for sapo in sapos:
        for plataforma in plataformas:
            if sapo.lados["bottom"].colliderect(plataforma.lados["top"]):
                sapo.esta_saltando = False
                if sapo.rect.right >= plataforma.rect.right:
                    sapo.estado = "izquierda"
                elif sapo.rect.left <= plataforma.rect.left:
                    sapo.estado = "derecha"



