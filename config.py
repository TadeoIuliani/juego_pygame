import pygame
#Pantalla-------------------
ANCHO = 900
ALTO = 600
COLOR_MENU = (9, 138, 211)
FPS = 40

#Colores--------------------
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
NARANJA = (255, 128, 0)
ROSA = (217, 74, 177)
AMARILLO = (255, 255, 0)
CELESTE = (0, 255, 255)

#Personaje--------
CENTER = (ANCHO // 10, ALTO - 200)
SPEED = 10

#Volumen-------
VOL_PREDETERMINADO = 0.5

#Tamaños----------
TAM_CRASH = (60, 80)
TAM_CANGRI = (50, 50)
TAM_ITEM = (30, 30)
TAM_PANTALLA = (ANCHO, ALTO)
TAM_SAPO = (40, 30)
TAM_BOSS = (150, 130)


#Ranking------------------------------------------------------------
UBICACION_PRIMER_PUESTO_LOGO = [300, 240]
UBICACION_SEGUNDO_PUESTO_LOGO = [300, 290]
UBICACION_TERCER_PUESTO_LOGO = [300, 340]
UBICACION_CUARTO_PUESTO_LOGO = [300, 390]
UBICACION_PRIMER_PUESTO_USER = pygame.rect.Rect(350, 240, 70, 35)
UBICACION_SEGUNDO_PUESTO_USER = pygame.rect.Rect(350, 290, 70, 35)
UBICACION_TERCER_PUESTO_USER = pygame.rect.Rect(350, 340, 70, 35)
UBICACION_CUARTO_PUESTO_USER = pygame.rect.Rect(350, 390, 70, 35)
COOR_BOSS = (700, 200)

#Nivel_1--------------------------------------------
PUNTAJE_FRUTA = 200
PUNTAJE_ENEMIGOS = 300
PUNTAJE_GANAR = 2500
ENEMIGOS_A_MATAR = 8
UBICACION_VIDA = (50, 20)
UBICACION_PUNTUACION = (200, 20)
UBICACION_TIEMPO = (500, 20)

#



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
#--------------------------------------------------------------------------------

def crear_objetos_random(clase, animaciones, imagen, tamaño, cantidad):
    lista = []
    for i in range(cantidad):
        objeto = clase(animaciones, imagen, tamaño)
        lista.append(objeto)
    return lista
#--------------------------------------------------------------------------------


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

#----------------------------------------------------------------------



def collision_player_caja(player, lista_caja):
    for caja in lista_caja:
        if player.lados["bottom"].colliderect(caja.lados["top"]):
            player.esta_saltando = False

def collision_enemigo_plataformas(enemigo, plataformas):
    for piso in plataformas:
        if enemigo.lados["bottom"].colliderect(piso.lados["top"]):
            enemigo.esta_cayendo = False
            enemigo.lados["bottom"].top = piso.lados["top"].top + 4
            if enemigo.rect.right >= piso.rect.right:
                enemigo.estado = "izquierda"
            elif enemigo.rect.left <= piso.rect.left:
                enemigo.estado = "derecha"

def collision_sapo_plataformas(sapo, plataformas):
    for plataforma in plataformas:
        if sapo.lados["bottom"].colliderect(plataforma.lados["top"]):
            sapo.esta_saltando = False
            if sapo.rect.right >= plataforma.rect.right:
                sapo.estado = "izquierda"
            elif sapo.rect.left <= plataforma.rect.left:
                sapo.estado = "derecha"

def collision_player_plataformas(player, plataformas):
    for plataforma in plataformas:
        if player.lados["bottom"].colliderect(plataforma.lados["top"]):
            player.esta_saltando = False
            break
        else:
            player.esta_saltando = True

def collision_bomba_plataformas(bomba, plataformas):
    for plataforma in plataformas:
        if bomba.rect.colliderect(plataforma.rect):
            bomba.esta_cayendo = False
            bomba.estado = "explosion"


def collision_objeto_plataforma(objetos, plataformas):
    from class_Personaje import Personaje
    from class_enemigo import Enemigo, Enemigo_2, Boss
    from class_sapo import Sapo
    from class_item import Bomba

    for objeto in objetos:
        if type(objeto) == Personaje:
            collision_player_plataformas(objeto, plataformas)
        elif type(objeto) == Sapo:
            collision_sapo_plataformas(objeto, plataformas)
        elif type(objeto) == Enemigo:
            collision_enemigo_plataformas(objeto, plataformas)
        elif type(objeto) == Enemigo_2:
            collision_enemigo_plataformas(objeto, plataformas)
        elif type(objeto) == Bomba:
            collision_bomba_plataformas(objeto, plataformas)
        elif type(objeto) == Boss:
            collision_player_plataformas(objeto, plataformas)




def agregar_lista_a_lista(lista_original : list, lista_agregar : list):
    for objeto in lista_agregar:
        lista_original.append(objeto)
    return lista_original


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
            

