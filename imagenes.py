import pygame 
from config import *

menu = {
    "nivel" : r"BOTONES\boton_play.png",
    "opciones" : r"BOTONES\boton_option.png",
    "exit" : r"BOTONES\boton_exit.png",
}

juego = {
    "fondo" : r"Fondos de juego\fondo_juego.jpg"
}

imagenes_cangrejos = {}
imagenes_cangrejos["derecha"] = [
    pygame.image.load(r"cangrejos\0.png"),
    pygame.image.load(r"cangrejos\1.png"),
    pygame.image.load(r"cangrejos\2.png"),
    pygame.image.load(r"cangrejos\2.png"),
]
imagenes_cangrejos["derecha"] = reescalar_imagenes(
    imagenes_cangrejos["derecha"], TAM_CANGRI
)

imagenes_cangrejos["izquierda"] = [
    pygame.image.load(r"cangrejos\0.png"),
    pygame.image.load(r"cangrejos\1.png"),
    pygame.image.load(r"cangrejos\2.png"),
    pygame.image.load(r"cangrejos\2.png"),
]
imagenes_cangrejos["izquierda"] = reescalar_imagenes(
    imagenes_cangrejos["izquierda"], TAM_CANGRI
)

imagenes_cangrejos["cayendo"] = [
    pygame.image.load(r"cangrejos\0.png"),
    pygame.image.load(r"cangrejos\1.png"),
    pygame.image.load(r"cangrejos\2.png"),
    pygame.image.load(r"cangrejos\2.png"),
]


imagenes_cangrejos["cayendo"] = reescalar_imagenes(
    imagenes_cangrejos["cayendo"], TAM_CANGRI
)

imagenes_cangrejos["quieto"] = imagenes_cangrejos["cayendo"]


imagenes_fruta = {}
imagenes_fruta["girando"] = [
    pygame.image.load(r"frutitas\0.png"),
    pygame.image.load(r"frutitas\1.png"),
    pygame.image.load(r"frutitas\2.png"),
    pygame.image.load(r"frutitas\2.png"),
    pygame.image.load(r"frutitas\3.png"),
    pygame.image.load(r"frutitas\4.png"),
    pygame.image.load(r"frutitas\5.png"),
    pygame.image.load(r"frutitas\6.png"),
    pygame.image.load(r"frutitas\7.png"),
    pygame.image.load(r"frutitas\8.png"),
    pygame.image.load(r"frutitas\9.png"),
    pygame.image.load(r"frutitas\10.png"),
    pygame.image.load(r"frutitas\11.png"),
    pygame.image.load(r"frutitas\12.png"),
    pygame.image.load(r"frutitas\13.png"),
    pygame.image.load(r"frutitas\14.png"),
]
imagenes_fruta["girando"] = reescalar_imagenes(imagenes_fruta["girando"], (35, 30))

imagenes_player = {}

quieto = [
    pygame.image.load("Crash\Crash Quieto\Crash Style_1 (1).png"),
    pygame.image.load("Crash\Crash Quieto\Crash Style_2 (1).png"),
    pygame.image.load("Crash\Crash Quieto\Crash Style_3 (1).png"),
    pygame.image.load("Crash\Crash Quieto\Crash Style_4.png"),
    pygame.image.load("Crash\Crash Quieto\Crash Style_5.png"),
]

imagenes_player["quieto"] = reescalar_imagenes(quieto, (TAM_CRASH))


imagenes_player["derecha"] = [
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_1.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_2.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_3.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_4.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_5.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_6.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_7.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_8.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_9.png"),
]
imagenes_player["derecha"] = reescalar_imagenes(imagenes_player["derecha"], (TAM_CRASH))

imagenes_player["izquierda"] = [
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_1.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_2.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_3.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_4.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_5.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_6.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_7.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_8.png"),
    pygame.image.load("Crash\Crash Trotar\Crash Trotar_9.png"),
]
lista_rotada_izquierda = rotar_imagen(imagenes_player["izquierda"], True, False)
imagenes_player["izquierda"] = reescalar_imagenes(lista_rotada_izquierda, (TAM_CRASH))


imagenes_player["salta"] = [
    pygame.image.load("Crash\Crash Saltar\Crash Salto_1.png"),
    pygame.image.load("Crash\Crash Saltar\Crash Salto_2.png"),
    pygame.image.load("Crash\Crash Saltar\Crash Salto_3.png"),
    pygame.image.load("Crash\Crash Saltar\Crash Salto_4.png"),
    pygame.image.load("Crash\Crash Saltar\Crash Salto_5.png"),
    pygame.image.load("Crash\Crash Saltar\Crash Salto_6.png"),
    pygame.image.load("Crash\Crash Saltar\Crash Salto_7.png"),
    pygame.image.load("Crash\Crash Saltar\Crash Salto_8.png"),
    pygame.image.load("Crash\Crash Saltar\Crash Salto_9.png"),
    pygame.image.load("Crash\Crash Saltar\Crash Salto_10.png"),
]
imagenes_player["salta"] = reescalar_imagenes(imagenes_player["salta"], (TAM_CRASH))

imagenes_player["girar"] = [
    pygame.image.load("Crash\Crash Girar\Crash Girar_1.png"),
    pygame.image.load("Crash\Crash Girar\Crash Girar_2.png"),
    pygame.image.load("Crash\Crash Girar\Crash Girar_3.png"),
    pygame.image.load("Crash\Crash Girar\Crash Girar_4.png"),
    pygame.image.load("Crash\Crash Girar\Crash Girar_5.png"),
    pygame.image.load("Crash\Crash Girar\Crash Girar_6.png"),
    pygame.image.load("Crash\Crash Girar\Crash Girar_7.png"),
    pygame.image.load("Crash\Crash Girar\Crash Girar_8.png"),
]
imagenes_player["girar"] = reescalar_imagenes(imagenes_player["girar"], (TAM_CRASH))


animaciones_sapo = {}

animaciones_sapo["izquierda"] =[
    pygame.image.load(r"sapos\0.png"),
    pygame.image.load(r"sapos\1.png"),
    pygame.image.load(r"sapos\2.png"),
    pygame.image.load(r"sapos\3.png")
]
lista_izquierda = rotar_imagen(animaciones_sapo["izquierda"], True, False) 
animaciones_sapo["izquierda"] = reescalar_imagenes(animaciones_sapo["izquierda"], (40, 30))

animaciones_sapo["derecha"] = lista_izquierda
animaciones_sapo["derecha"] = reescalar_imagenes(animaciones_sapo["derecha"], (40, 30))

animaciones_sapo["salta"] =[
    pygame.image.load(r"sapos\0.png"),
    pygame.image.load(r"sapos\1.png"),
    pygame.image.load(r"sapos\2.png"),
    pygame.image.load(r"sapos\3.png")
]
animaciones_sapo["salta"] = reescalar_imagenes(animaciones_sapo["salta"], (40, 30))

animaciones_sapo["cayendo"] = [
    pygame.image.load(r"sapos\0.png")
]

caja = {
    "imagen" : r"cajas\normal.png"
}

trampa = {}
trampa["on"] = [
    pygame.image.load(r"trampa\On_1.png"),
    pygame.image.load(r"trampa\On_2.png"),
    pygame.image.load(r"trampa\On_3.png"),
    pygame.image.load(r"trampa\On_4.png"),
    pygame.image.load(r"trampa\On_5.png"),
    pygame.image.load(r"trampa\On_6.png"),
    pygame.image.load(r"trampa\On_7.png"),
    pygame.image.load(r"trampa\On_8.png"),
]
trampa["off"] = [pygame.image.load(r"trampa\Off.png")]
trampa["on"] = reescalar_imagenes(trampa["on"], (30, 30))
trampa["off"] = reescalar_imagenes(trampa["off"], (30, 30))



camaleon = {}
camaleon["izquierda"] = [
    pygame.image.load(r"camaleon\camaleon_caminar_1.png"),
    pygame.image.load(r"camaleon\camaleon_caminar_2.png"),
    pygame.image.load(r"camaleon\camaleon_caminar_3.png"),
    pygame.image.load(r"camaleon\camaleon_caminar_4.png"),
    pygame.image.load(r"camaleon\camaleon_caminar_5.png"),
    pygame.image.load(r"camaleon\camaleon_caminar_6.png"),
    pygame.image.load(r"camaleon\camaleon_caminar_7.png"),
    pygame.image.load(r"camaleon\camaleon_caminar_8.png"),
]
camaleon["izquierda"] = reescalar_imagenes(camaleon["izquierda"], (80, 50))

camaleon["derecha"] = rotar_imagen(camaleon["izquierda"], True, False)

camaleon["cayendo"] = [
    pygame.image.load(r"camaleon\camaleon_caminar_4.png")
]
camaleon["cayendo"] = reescalar_imagenes(camaleon["cayendo"], (80, 50))

camaleon["atacar_izquierda"] = [
    pygame.image.load(r"camaleon\camaleon_ataque_1.png"),
    pygame.image.load(r"camaleon\camaleon_ataque_2.png"),
    pygame.image.load(r"camaleon\camaleon_ataque_3.png"),
    pygame.image.load(r"camaleon\camaleon_ataque_4.png"),
    pygame.image.load(r"camaleon\camaleon_ataque_5.png"),
    pygame.image.load(r"camaleon\camaleon_ataque_6.png"),
    pygame.image.load(r"camaleon\camaleon_ataque_7.png"),
    pygame.image.load(r"camaleon\camaleon_ataque_8.png"),
    pygame.image.load(r"camaleon\camaleon_ataque_9.png"),
    pygame.image.load(r"camaleon\camaleon_ataque_10.png"),
]
camaleon["atacar_izquierda"] = reescalar_imagenes(camaleon["atacar_izquierda"], (80, 50))

camaleon["atacar_derecha"] = rotar_imagen(camaleon["atacar_izquierda"], True, False)


imagenes_boss = {}
imagenes_boss["quieto"] = [
    pygame.image.load(r"boss_sprites\sprites_boss_3-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_3-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_3-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_2-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_2-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_2-removebg-preview.png")
]
imagenes_boss["atacar"] = [
    pygame.image.load(r"boss_sprites\sprites_boss_2-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_2-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_3-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_3-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_1-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_1-removebg-preview.png")
]

imagenes_boss["muerte"] = [
    pygame.image.load(r"boss_sprites\sprites_boss_1-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_1-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_2-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_2-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_3-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_3-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_4-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_4-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_5-removebg-preview.png"),
    pygame.image.load(r"boss_sprites\sprites_boss_5-removebg-preview.png")
]

imagenes_boss["muerte"] = reescalar_imagenes(imagenes_boss["muerte"], (150, 130))
imagenes_boss["quieto"] = reescalar_imagenes(imagenes_boss["quieto"], (150, 130))
imagenes_boss["atacar"] = reescalar_imagenes(imagenes_boss["atacar"], (150, 130))

imagenes_toki = {}
imagenes_toki["derecha"] = [
    pygame.image.load("sprites_toki\derecha_1.png"),
    pygame.image.load("sprites_toki\derecha_2.png"),
    pygame.image.load("sprites_toki\derecha_3.png"),
    pygame.image.load("sprites_toki\derecha_4.png"),
    pygame.image.load("sprites_toki\derecha_5.png"),
    pygame.image.load("sprites_toki\derecha_6.png"),
]
imagenes_toki["derecha"] = reescalar_imagenes(imagenes_toki["derecha"], (50, 50))
imagenes_toki["izquierda"] = rotar_imagen(imagenes_toki["derecha"], True, False)

imagenes_toki["atacar_derecha"] = [
    pygame.image.load(r"sprites_toki\atacar_derecha_1.png"),
    pygame.image.load(r"sprites_toki\atacar_derecha_2.png"),
    pygame.image.load(r"sprites_toki\atacar_derecha_3.png"),
    pygame.image.load(r"sprites_toki\atacar_derecha_4.png"),
    pygame.image.load(r"sprites_toki\atacar_derecha_5.png"),
    pygame.image.load(r"sprites_toki\atacar_derecha_6.png"),
]
imagenes_toki["atacar_derecha"] = reescalar_imagenes(imagenes_toki["atacar_derecha"], (50, 50))
imagenes_toki["atacar_izquierda"] = rotar_imagen(imagenes_toki["atacar_derecha"], True, False)

imagenes_toki["cayendo"] = [
    pygame.image.load(r"sprites_toki\saltando.png")
]
imagenes_toki["cayendo"] = reescalar_imagenes(imagenes_toki["cayendo"], (50, 50))

imagenes_bomba = {}
imagenes_bomba["cayendo"] = [
    pygame.image.load(r"klipartz.com.png")
]
imagenes_bomba["cayendo"] = reescalar_imagenes(imagenes_bomba["cayendo"], (80, 100))

imagenes_bomba["explosion"] = [
    pygame.image.load(r"klipartz.com (1).png"),
    pygame.image.load(r"klipartz.com (1).png"),
    pygame.image.load(r"klipartz.com (1).png"),
    pygame.image.load(r"klipartz.com (1).png")
]
imagenes_bomba["explosion"] = reescalar_imagenes(imagenes_bomba["explosion"], (80, 100))