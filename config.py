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

COLOR_MENU = (9, 138, 211)

FPS = 40
SPEED = 10

CENTER = (ANCHO // 10, ALTO - 200)

VOL_PREDETERMINADO = 0.5
TAM_CRASH = (60, 80)
TAM_CANGRI = (50, 50)
TAM_ITEM = (30, 30)
TAM_PANTALLA = (ANCHO, ALTO)

UBICACION_PRIMER_PUESTO_LOGO = [300, 240]
UBICACION_SEGUNDO_PUESTO_LOGO = [300, 290]
UBICACION_TERCER_PUESTO_LOGO = [300, 340]
UBICACION_CUARTO_PUESTO_LOGO = [300, 390]
UBICACION_PRIMER_PUESTO_USER = pygame.rect.Rect(350, 240, 70, 35)
UBICACION_SEGUNDO_PUESTO_USER = pygame.rect.Rect(350, 290, 70, 35)
UBICACION_TERCER_PUESTO_USER = pygame.rect.Rect(350, 340, 70, 35)
UBICACION_CUARTO_PUESTO_USER = pygame.rect.Rect(350, 390, 70, 35)



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

class GenearadorEnemigos_2(GenearadorEnemigos):
    def __init__(self, image, tamaño, speed, animaciones, ubicacion) -> None:
        super().__init__(image, tamaño, speed, animaciones)
        self.ubicacion = ubicacion

    def generar_enemigos(self, clase, cantidad):
        lista = []
        for i in range(cantidad):
            object = clase(self.image, self.tamaño, self.speed, self.animaciones, self.ubicacion)
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

def collision_sapo_plataformas(sapos, plataformas):
    for sapo in sapos:
        for plataforma in plataformas:
            if sapo.lados["bottom"].colliderect(plataforma.lados["top"]):
                sapo.esta_saltando = False
                if sapo.rect.right >= plataforma.rect.right:
                    sapo.estado = "izquierda"
                elif sapo.rect.left <= plataforma.rect.left:
                    sapo.estado = "derecha"



