import pygame, sys
import pygame
from class_Player import *
from config import *
from class_Piso import *
from class_enemigo import *
from imagenes import *
from class_sapo import Sapo
from class_Plataforma import Plataforma
from class_Bottom import *

pygame.init()

reloj = pygame.time.Clock()

path_caja = caja["imagen"]
pantalla = pygame.display.set_mode((ANCHO, ALTO))



pygame.display.set_caption("Juego Practica")

fondo = pygame.image.load(r"images\Fondos de juego\fondo_juego.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

player = Player(TAM_CRASH, CENTER, "Crash\Crash Quieto\Crash Style_1 (1).png", 7, imagenes_player, 3)

piso = Piso("images\pisos\piso.png", (ANCHO, 80), (0, 525))
plataforma_1 = Piso("images\pisos\piso.png", (600, 60), (120, 432))
plataforma_2 = Piso("images\pisos\piso.png", (450, 60), (280, 330))
plataforma_3 = Piso("images\pisos\piso.png", (400, 60), (120, 220))
plataforma_4 = Piso("images\pisos\piso.png", (380, 60), (300, 120))
caja = Piso(path_caja, (80, 80), (120, 354))
caja_2 = Piso(path_caja, (80, 80), (640, 250))
caja_3 = Piso(path_caja, (80, 80), (120, 145))
plataformas = [piso, plataforma_1, plataforma_2, caja, caja_2, plataforma_3, caja_3, plataforma_4]
cajas = [caja, caja_2, caja_3]

fruta = Item(imagenes_fruta, r"images\frutitas\0.png", TAM_ITEM)

generador_cangrejos = GenearadorEnemigos(r"images\cangrejos\0.png", TAM_CANGRI, 7, imagenes_cangrejos)
generador_sapos = GenearadorEnemigos(r"images\sapos\0.png", (40, 30), 5, animaciones_sapo)
lista_enemigos = generador_cangrejos.generar_enemigos(Enemigo, 2)
lista_sapos = generador_sapos.generar_enemigos(Sapo, 3)
vidas = 3
Fuente = pygame.font.SysFont("Arial", 30)
puntuacion = 0
lista_frutas = [fruta]
laser = None
bala_viva = False
rectangulos_prog = False





boton_inicio = Bottom(r"images\pisos\boton_play.png", 350, 200, (200, 80))
boton_opciones = Bottom(r"images\pisos\boton_opciones.png", 350, 300, (200, 80))
boton_exit = Bottom(r"images\pisos\boton_exit.png", 350, 400, (200, 80))
fondo_menu = pygame.image.load("images\pisos\menu juego.png")
imagen_game_over = pygame.image.load("images\pngegg.png")
imagen_game_over = pygame.transform.scale(imagen_game_over, (50, 30))

on = True

menu = True

jugando = False
game_over = False
gano = False

pausa = False

#Funciona
while on:
    eventos = pygame.event.get()
    if menu:
        pantalla.fill((45, 158, 196))
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if boton_inicio.draw(pantalla):
            nivel_actual = juego
            menu = False
            jugando = True
        if boton_opciones.draw(pantalla):
            nivel_actual = juego
            menu = False
        if boton_exit.draw(pantalla):
            on = False
            pygame.quit()
            sys.exit()
        pygame.display.flip()
    elif jugando:
        reloj.tick(27)
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if bala_viva == False:
                        laser = Laser("images\disparo.png", player.rect.midright)
                        bala_viva = True
                elif event.key == pygame.K_z:
                    if bala_viva == False:
                        laser = Laser("images\disparo.png", player.rect.midright, False)
                        bala_viva = True
                elif event.key == pygame.K_TAB:
                    rectangulos_prog = not rectangulos_prog
                elif event.key == pygame.K_ESCAPE:
                    pausa = not pausa
        # Movimientos de jugador y actualizacion de posicion.
                
        
        teclas_presionadas = pygame.key.get_pressed()
        if teclas_presionadas[pygame.K_LEFT] and player.rect.left > ANCHO / ANCHO + 7:
            player.estado = "izquierda"
        elif teclas_presionadas[pygame.K_RIGHT] and player.rect.right < ANCHO - SPEED:
            player.estado = "derecha"
        elif teclas_presionadas[pygame.K_SPACE]:
            player.estado = "salta"
        elif teclas_presionadas[pygame.K_x] or teclas_presionadas[pygame.K_z]:
            player.estado = "girar"
        else:
            player.estado = "quieto"

        # Colisiones del juego
        for enemigo in lista_enemigos:
            if enemigo.rect.colliderect(piso.rect):
                enemigo.esta_cayendo = False
                enemigo.lados["bottom"].top = piso.lados["top"].top + 4

            elif enemigo.lados["bottom"].colliderect(plataforma_1.lados["top"]):
                enemigo.esta_cayendo = False
                enemigo.lados["bottom"].top = plataforma_1.lados["top"].top + 4
                if enemigo.rect.right >= plataforma_1.rect.right:
                    enemigo.estado = "izquierda"
                elif enemigo.rect.left <= plataforma_1.rect.left:
                    enemigo.estado = "derecha"

            elif enemigo.lados["bottom"].colliderect(plataforma_2.lados["top"]):
                enemigo.esta_cayendo = False
                enemigo.lados["bottom"].top = plataforma_2.lados["top"].top + 4
                if enemigo.rect.right >= plataforma_2.rect.right:
                    enemigo.estado = "izquierda"
                elif enemigo.rect.left <= plataforma_2.rect.left:
                    enemigo.estado = "derecha"

            elif enemigo.lados["bottom"].colliderect(plataforma_3.lados["top"]):
                enemigo.esta_cayendo = False
                enemigo.lados["bottom"].top = plataforma_3.lados["top"].top + 4
                if enemigo.rect.right >= plataforma_3.rect.right:
                    enemigo.estado = "izquierda"
                elif enemigo.rect.left <= plataforma_3.rect.left:
                    enemigo.estado = "derecha"

            elif enemigo.lados["bottom"].colliderect(plataforma_4.lados["top"]):
                enemigo.esta_cayendo = False
                enemigo.lados["bottom"].top = plataforma_4.lados["top"].top + 4
                if enemigo.rect.right >= plataforma_4.rect.right:
                    enemigo.estado = "izquierda"
                elif enemigo.rect.left <= plataforma_4.rect.left:
                    enemigo.estado = "derecha"
            else:
                enemigo.esta_cayendo = True
        for sapo in lista_sapos:
            for plataforma in plataformas:
                if sapo.lados["bottom"].colliderect(plataforma.lados["top"]):
                    sapo.esta_saltando = False
                    if sapo.rect.right >= plataforma.rect.right:
                        sapo.estado = "izquierda"
                    elif sapo.rect.left <= plataforma.rect.left:
                        sapo.estado = "derecha"

        for plataforma in plataformas:
            if player.lados["bottom"].colliderect(plataforma.lados["top"]):
                player.esta_saltando = False
                break
            else:
                player.esta_saltando = True

        if player.lados["bottom"].colliderect(caja.lados["top"]):
            player.esta_saltando = False

        for fruta in lista_frutas:
            if colision_fruta_plataforma(fruta, piso):
                fruta.esta_cayendo = False

        for fruta in lista_frutas:
            if colision_fruta_player(fruta, player):
                lista_frutas.remove(fruta)
                puntuacion += 200
        
        for enemigo in lista_enemigos:
            if enemigo.rect.colliderect(player.rect):
                vidas -= 1

        for sapo in lista_sapos:
            if sapo.rect.colliderect(player.rect):
                vidas -= 1

        if puntuacion > 2000: 
            gano = True
            jugando = False

        if vidas < 1:
            gano = False
            jugando = False

        if bala_viva:
            for enemigo in lista_enemigos:
                if enemigo.rect.colliderect(laser.rect):
                    lista_enemigos.remove(enemigo)
                    puntuacion += 100
                    bala_viva = False
            for sapo in lista_sapos:
                if sapo.rect.colliderect(laser.rect):
                    lista_sapos.remove(sapo)
                    puntuacion += 100
                    bala_viva = False
            if laser.rect.x < 0:
                bala_viva = False
        
            if laser.rect.x >= ANCHO:
                bala_viva = False
        

        if len(lista_frutas) == 0:
            lista_frutas = crear_objetos_random(Item, imagenes_fruta, r"images\frutitas\0.png", TAM_ITEM, 5)

        if len(lista_enemigos) == 0:
            enemigo = Enemigo(r"images\cangrejos\0.png", TAM_CANGRI, 7, imagenes_cangrejos)
            lista_enemigos = generador_cangrejos.generar_enemigos(Enemigo, 3)
        
        cronometro = pygame.time.get_ticks() // 1000
        cronometro = 60 - int(cronometro)
        if cronometro < 1:
            game_over = True

        pantalla.blit(fondo, (0, 0))
        for plataforma in plataformas:
            pantalla.blit(plataforma.image, plataforma.rect)

        for i in range(len(lista_frutas)):
            lista_frutas[i].update(pantalla)

        if rectangulos_prog:
            for key in enemigo.lados:
                pygame.draw.rect(pantalla, AZUL, enemigo.lados[key], 2)
            for key in player.lados:
                pygame.draw.rect(pantalla, AZUL, player.lados[key], 2)
            for key in plataforma.lados:
                pygame.draw.rect(pantalla, ROJO, plataforma.lados[key], 2)
            for key in plataforma_1.lados:
                pygame.draw.rect(pantalla, ROJO, plataforma_1.lados[key], 2)
            for key in plataforma_2.lados:
                pygame.draw.rect(pantalla, ROJO, plataforma_2.lados[key], 2)
            for key in plataforma_3.lados:
                pygame.draw.rect(pantalla, ROJO, plataforma_3.lados[key], 2)
            for key in plataforma_4.lados:
                pygame.draw.rect(pantalla, ROJO, plataforma_4.lados[key], 2)
            for key in piso.lados:
                pygame.draw.rect(pantalla, ROJO, piso.lados[key], 2)
            pygame.draw.line(pantalla, ROJO, plataforma_4.rect.midleft,(plataforma_4.rect.left, 40) , 2)
            pygame.draw.line(pantalla, ROJO, plataforma_4.rect.midright,(plataforma_4.rect.right, 40) , 2)

        pantalla.blit(Fuente.render(f"X{vidas}", 0, NEGRO), (50, 20))
        pantalla.blit(Fuente.render(f"Puntos: {puntuacion}", 0, NEGRO), (200, 20))
        pantalla.blit(Fuente.render("Tiempo: " + str(cronometro), 0, BLANCO), (500, 20))

        for i in range(len(lista_enemigos)):
            lista_enemigos[i].update(pantalla)
        player.update(pantalla)

        if bala_viva:
            laser.update(pantalla)
        for sapo in lista_sapos:
            sapo.update(pantalla)
        
        pygame.display.flip()
    else:
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pantalla.fill(NEGRO)
        if gano:
            pantalla.blit(Fuente.render(f"GANO!!!!! {puntuacion}", 0, VERDE), (200, 300))
        else:
            pantalla.blit(Fuente.render(f"Perdio {puntuacion}", 0, VERDE), (200, 300))
        pygame.display.flip()
# while menu:
    # while menu == False:

    #     reloj.tick(27)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_x:
    #                 if bala_viva == False:
    #                     laser = Laser("images\disparo.png", player.rect.midright)
    #                     bala_viva = True
    #             elif event.key == pygame.K_z:
    #                 if bala_viva == False:
    #                     laser = Laser("images\disparo.png", player.rect.midright, False)
    #                     bala_viva = True
    #             elif event.key == pygame.K_TAB:
    #                 rectangulos_prog = not rectangulos_prog
    #         # Movimientos de jugador y actualizacion de posicion.

    #     teclas_presionadas = pygame.key.get_pressed()
    #     if teclas_presionadas[pygame.K_LEFT] and player.rect.left > ANCHO / ANCHO + 7:
    #         player.estado = "izquierda"
    #     elif teclas_presionadas[pygame.K_RIGHT] and player.rect.right < ANCHO - SPEED:
    #         player.estado = "derecha"
    #     elif teclas_presionadas[pygame.K_SPACE]:
    #         player.estado = "salta"
    #     elif teclas_presionadas[pygame.K_x] or teclas_presionadas[pygame.K_z]:
    #         player.estado = "girar"
    #     else:
    #         player.estado = "quieto"

    #     # Colisiones del juego
    #     for enemigo in lista_enemigos:
    #         if enemigo.rect.colliderect(piso.rect):
    #             enemigo.esta_cayendo = False
    #             enemigo.lados["bottom"].top = piso.lados["top"].top + 4

    #         elif enemigo.lados["bottom"].colliderect(plataforma_1.lados["top"]):
    #             enemigo.esta_cayendo = False
    #             enemigo.lados["bottom"].top = plataforma_1.lados["top"].top + 4
    #             if enemigo.rect.right >= plataforma_1.rect.right:
    #                 enemigo.estado = "izquierda"
    #             elif enemigo.rect.left <= plataforma_1.rect.left:
    #                 enemigo.estado = "derecha"

    #         elif enemigo.lados["bottom"].colliderect(plataforma_2.lados["top"]):
    #             enemigo.esta_cayendo = False
    #             enemigo.lados["bottom"].top = plataforma_2.lados["top"].top + 4
    #             if enemigo.rect.right >= plataforma_2.rect.right:
    #                 enemigo.estado = "izquierda"
    #             elif enemigo.rect.left <= plataforma_2.rect.left:
    #                 enemigo.estado = "derecha"

    #         elif enemigo.lados["bottom"].colliderect(plataforma_3.lados["top"]):
    #             enemigo.esta_cayendo = False
    #             enemigo.lados["bottom"].top = plataforma_3.lados["top"].top + 4
    #             if enemigo.rect.right >= plataforma_3.rect.right:
    #                 enemigo.estado = "izquierda"
    #             elif enemigo.rect.left <= plataforma_3.rect.left:
    #                 enemigo.estado = "derecha"

    #         elif enemigo.lados["bottom"].colliderect(plataforma_4.lados["top"]):
    #             enemigo.esta_cayendo = False
    #             enemigo.lados["bottom"].top = plataforma_4.lados["top"].top + 4
    #             if enemigo.rect.right >= plataforma_4.rect.right:
    #                 enemigo.estado = "izquierda"
    #             elif enemigo.rect.left <= plataforma_4.rect.left:
    #                 enemigo.estado = "derecha"
    #         else:
    #             enemigo.esta_cayendo = True

    #     for sapo in lista_sapos:
    #         for plataforma in plataformas:
    #             if sapo.lados["bottom"].colliderect(plataforma.lados["top"]):
    #                 sapo.esta_saltando = False
    #                 if sapo.rect.right >= plataforma.rect.right:
    #                     sapo.estado = "izquierda"
    #                 elif sapo.rect.left <= plataforma.rect.left:
    #                     sapo.estado = "derecha"

    #     for i in range(len(plataformas)):
    #         if player.lados["bottom"].colliderect(plataformas[i].lados["top"]):
    #             player.esta_saltando = False
    #             break
    #         else:
    #             player.esta_saltando = True

    #         if player.lados["bottom"].colliderect(caja.lados["top"]):
    #             player.esta_saltando = False
            
    #     for i in range(len(lista_frutas)):
    #         if colision_fruta_plataforma(lista_frutas[i], piso):
    #             lista_frutas[i].esta_cayendo = False

    #     for fruta in lista_frutas:
    #         if colision_fruta_player(fruta, player):
    #             lista_frutas.remove(fruta)
    #             puntuacion += 200

    #     if enemigo.rect.colliderect(player.rect):
    #         vidas -= 1

    #     if vidas < 1 or puntuacion > 2000:
    #         game_over = True

    #     if bala_viva:
    #         for enemigo in lista_enemigos:
    #             if enemigo.rect.colliderect(laser.rect):
    #                 lista_enemigos.remove(enemigo)
    #                 bala_viva = False
    #         for sapo in lista_sapos:
    #             if sapo.rect.colliderect(laser.rect):
    #                 lista_sapos.remove(sapo)
    #                 bala_viva = False
    #         if laser.rect.x < 0:
    #             bala_viva = False
        
    #         if laser.rect.x >= ANCHO:
    #             bala_viva = False

    #     if len(lista_frutas) == 0:
    #         lista_frutas = crear_objetos_random(Item, imagenes_fruta, r"images\frutitas\0.png", TAM_ITEM, 5)

    #     if len(lista_enemigos) == 0:
    #         enemigo = Enemigo(r"images\cangrejos\0.png", TAM_CANGRI, 7, imagenes_cangrejos)
    #         lista_enemigos = generador_cangrejos.generar_enemigos(Enemigo, 3)

    #     cronometro = pygame.time.get_ticks() // 1000
    #     cronometro = 60 - int(cronometro)
    #     if cronometro < 1:
    #         game_over = True

    #     pantalla.blit(fondo, (0, 0))
    #     for plataforma in plataformas:
    #         pantalla.blit(plataforma.image, plataforma.rect)

    #     for i in range(len(lista_frutas)):
    #         lista_frutas[i].update(pantalla)
    #     if rectangulos_prog:
    #         for key in enemigo.lados:
    #             pygame.draw.rect(pantalla, AZUL, enemigo.lados[key], 2)
    #         for key in player.lados:
    #             pygame.draw.rect(pantalla, AZUL, player.lados[key], 2)
    #         for key in plataforma.lados:
    #             pygame.draw.rect(pantalla, ROJO, plataforma.lados[key], 2)
    #         for key in plataforma_1.lados:
    #             pygame.draw.rect(pantalla, ROJO, plataforma_1.lados[key], 2)
    #         for key in plataforma_2.lados:
    #             pygame.draw.rect(pantalla, ROJO, plataforma_2.lados[key], 2)
    #         for key in plataforma_3.lados:
    #             pygame.draw.rect(pantalla, ROJO, plataforma_3.lados[key], 2)
    #         for key in plataforma_4.lados:
    #             pygame.draw.rect(pantalla, ROJO, plataforma_4.lados[key], 2)
    #         for key in piso.lados:
    #             pygame.draw.rect(pantalla, ROJO, piso.lados[key], 2)
    #         pygame.draw.line(pantalla, ROJO, plataforma_4.rect.midleft,(plataforma_4.rect.left, 40) , 2)
    #         pygame.draw.line(pantalla, ROJO, plataforma_4.rect.midright,(plataforma_4.rect.right, 40) , 2)

        
    #     pantalla.blit(Fuente.render(f"X{vidas}", 0, NEGRO), (50, 20))
    #     pantalla.blit(Fuente.render(f"Puntos: {puntuacion}", 0, NEGRO), (200, 20))
    #     pantalla.blit(Fuente.render("Tiempo: " + str(cronometro), 0, BLANCO), (500, 20))
    #     for i in range(len(lista_enemigos)):
    #         lista_enemigos[i].update(pantalla)
    #     player.update(pantalla)
    #     if bala_viva:
    #         laser.update(pantalla)
    #     for sapo in lista_sapos:
    #         sapo.update(pantalla)
        
        
    # pygame.display.flip()



    # for event in eventos:
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         sys.exit()
    # if boton_inicio.draw(pantalla):
    #     nivel_actual = juego
    #     menu = False
    #     print("boton inicio")
    # if boton_opciones.draw(pantalla):
    #     nivel_actual = juego
    #     print("boton opc")
    #     menu = False
    # if boton_exit.draw(pantalla):
    #     print("boton exit")
    #     pygame.quit()
    #     sys.exit()
    
    # pygame.display.flip()














































# while not menu:

#     reloj.tick(27)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_x:
#                 if bala_viva == False:
#                     laser = Laser("images\disparo.png", player.rect.midright)
#                     bala_viva = True
#             elif event.key == pygame.K_z:
#                 if bala_viva == False:
#                     laser = Laser("images\disparo.png", player.rect.midright, False)
#                     bala_viva = True
#             elif event.key == pygame.K_TAB:
#                 rectangulos_prog = not rectangulos_prog
#         # Movimientos de jugador y actualizacion de posicion.

#     teclas_presionadas = pygame.key.get_pressed()
#     if teclas_presionadas[pygame.K_LEFT] and player.rect.left > ANCHO / ANCHO + 7:
#         player.estado = "izquierda"
#     elif teclas_presionadas[pygame.K_RIGHT] and player.rect.right < ANCHO - SPEED:
#         player.estado = "derecha"
#     elif teclas_presionadas[pygame.K_SPACE]:
#         player.estado = "salta"
#     elif teclas_presionadas[pygame.K_x] or teclas_presionadas[pygame.K_z]:
#         player.estado = "girar"
#     else:
#         player.estado = "quieto"

#     # Colisiones del juego
#     for enemigo in lista_enemigos:
#         if enemigo.rect.colliderect(piso.rect):
#             enemigo.esta_cayendo = False
#             enemigo.lados["bottom"].top = piso.lados["top"].top + 4

#         elif enemigo.lados["bottom"].colliderect(plataforma_1.lados["top"]):
#             enemigo.esta_cayendo = False
#             enemigo.lados["bottom"].top = plataforma_1.lados["top"].top + 4
#             if enemigo.rect.right >= plataforma_1.rect.right:
#                 enemigo.estado = "izquierda"
#             elif enemigo.rect.left <= plataforma_1.rect.left:
#                 enemigo.estado = "derecha"

#         elif enemigo.lados["bottom"].colliderect(plataforma_2.lados["top"]):
#             enemigo.esta_cayendo = False
#             enemigo.lados["bottom"].top = plataforma_2.lados["top"].top + 4
#             if enemigo.rect.right >= plataforma_2.rect.right:
#                 enemigo.estado = "izquierda"
#             elif enemigo.rect.left <= plataforma_2.rect.left:
#                 enemigo.estado = "derecha"

#         elif enemigo.lados["bottom"].colliderect(plataforma_3.lados["top"]):
#             enemigo.esta_cayendo = False
#             enemigo.lados["bottom"].top = plataforma_3.lados["top"].top + 4
#             if enemigo.rect.right >= plataforma_3.rect.right:
#                 enemigo.estado = "izquierda"
#             elif enemigo.rect.left <= plataforma_3.rect.left:
#                 enemigo.estado = "derecha"

#         elif enemigo.lados["bottom"].colliderect(plataforma_4.lados["top"]):
#             enemigo.esta_cayendo = False
#             enemigo.lados["bottom"].top = plataforma_4.lados["top"].top + 4
#             if enemigo.rect.right >= plataforma_4.rect.right:
#                 enemigo.estado = "izquierda"
#             elif enemigo.rect.left <= plataforma_4.rect.left:
#                 enemigo.estado = "derecha"
#         else:
#             enemigo.esta_cayendo = True

#     for sapo in lista_sapos:
#         for plataforma in plataformas:
#             if sapo.lados["bottom"].colliderect(plataforma.lados["top"]):
#                 sapo.esta_saltando = False
#                 if sapo.rect.right >= plataforma.rect.right:
#                     sapo.estado = "izquierda"
#                 elif sapo.rect.left <= plataforma.rect.left:
#                     sapo.estado = "derecha"

#     for i in range(len(plataformas)):
#         if player.lados["bottom"].colliderect(plataformas[i].lados["top"]):
#             player.esta_saltando = False
#             break
#         else:
#             player.esta_saltando = True

#         if player.lados["bottom"].colliderect(caja.lados["top"]):
#             player.esta_saltando = False
        
#     for i in range(len(lista_frutas)):
#         if colision_fruta_plataforma(lista_frutas[i], piso):
#             lista_frutas[i].esta_cayendo = False

#     for fruta in lista_frutas:
#         if colision_fruta_player(fruta, player):
#             lista_frutas.remove(fruta)
#             puntuacion += 200

#     if enemigo.rect.colliderect(player.rect):
#         vidas -= 1

#     if vidas < 1 or puntuacion > 2000:
#         jugando = not jugando

#     if bala_viva:
#         for enemigo in lista_enemigos:
#             if enemigo.rect.colliderect(laser.rect):
#                 lista_enemigos.remove(enemigo)
#                 bala_viva = False
#         for sapo in lista_sapos:
#             if sapo.rect.colliderect(laser.rect):
#                 lista_sapos.remove(sapo)
#                 bala_viva = False
#         if laser.rect.x < 0:
#             bala_viva = False
    
#         if laser.rect.x >= ANCHO:
#             bala_viva = False

#     if len(lista_frutas) == 0:
#         lista_frutas = crear_objetos_random(Item, imagenes_fruta, r"images\frutitas\0.png", TAM_ITEM, 5)

#     if len(lista_enemigos) == 0:
#         enemigo = Enemigo(r"images\cangrejos\0.png", TAM_CANGRI, 7, imagenes_cangrejos)
#         lista_enemigos = generador_cangrejos.generar_enemigos(Enemigo, 3)

#     cronometro = pygame.time.get_ticks() // 1000
#     cronometro = 60 - int(cronometro)
#     if cronometro < 1:
#         jugando = False

#     pantalla.blit(fondo, (0, 0))
#     for plataforma in plataformas:
#         pantalla.blit(plataforma.image, plataforma.rect)

#     for i in range(len(lista_frutas)):
#         lista_frutas[i].update(pantalla)
#     if rectangulos_prog:
#         for key in enemigo.lados:
#             pygame.draw.rect(pantalla, AZUL, enemigo.lados[key], 2)
#         for key in player.lados:
#             pygame.draw.rect(pantalla, AZUL, player.lados[key], 2)
#         for key in plataforma.lados:
#             pygame.draw.rect(pantalla, ROJO, plataforma.lados[key], 2)
#         for key in plataforma_1.lados:
#             pygame.draw.rect(pantalla, ROJO, plataforma_1.lados[key], 2)
#         for key in plataforma_2.lados:
#             pygame.draw.rect(pantalla, ROJO, plataforma_2.lados[key], 2)
#         for key in plataforma_3.lados:
#             pygame.draw.rect(pantalla, ROJO, plataforma_3.lados[key], 2)
#         for key in plataforma_4.lados:
#             pygame.draw.rect(pantalla, ROJO, plataforma_4.lados[key], 2)
#         for key in piso.lados:
#             pygame.draw.rect(pantalla, ROJO, piso.lados[key], 2)
#         pygame.draw.line(pantalla, ROJO, plataforma_4.rect.midleft,(plataforma_4.rect.left, 40) , 2)
#         pygame.draw.line(pantalla, ROJO, plataforma_4.rect.midright,(plataforma_4.rect.right, 40) , 2)

    
#     pantalla.blit(Fuente.render(f"X{vidas}", 0, NEGRO), (50, 20))
#     pantalla.blit(Fuente.render(f"Puntos: {puntuacion}", 0, NEGRO), (200, 20))
#     pantalla.blit(Fuente.render("Tiempo: " + str(cronometro), 0, BLANCO), (500, 20))
#     for i in range(len(lista_enemigos)):
#         lista_enemigos[i].update(pantalla)
#     player.update(pantalla)
#     if bala_viva:
#         laser.update(pantalla)
#     for sapo in lista_sapos:
#         sapo.update(pantalla)
    
#     pygame.display.flip()
