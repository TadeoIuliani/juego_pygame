import pygame, sys
from config import *
from class_Piso import *
from class_enemigo import *
from imagenes import *
from class_sapo import Sapo
from class_Bottom import *
from class_Nivel import * 
from class_Nivel2 import * 
from class_Nivel3 import * 
from textbox import *
import json
from based import *
from cronometro import *
from class_Barra import Barra


class Game():
    def __init__(self, pantalla, bd) -> None:
        pygame.font.init()
        self.pantalla = pantalla
        self.estado_juego = "inicio"
        self.on = True
        self.puntuacion = 0
        self.nivel_seleccionado = None
        self.base_datos = bd
        #inicio---------------------------------------------------------------------------
        self.Fuente_user = pygame.font.SysFont("Copperplate Gothic", 50)
        self.Fuente_prueba = pygame.font.SysFont("Algerian", 100)
        self.Fuente_ranking = pygame.font.SysFont("Copperplate Gothic", 30)
        self.rectangulo_user = pygame.Rect(350, 300, 100, 60)
        self.txt_user = TextBox(self.Fuente_user, NEGRO, "", self.rectangulo_user, BLANCO, 4)
        self.resetear_juego = Bottom("BOTONES\pngwing.com (13).png", 800, 50, (50, 50))
        self.user = None
        self.logo_inicio = pygame.image.load(r"BOTONES\Crash_bandicoot_logo_by_jerimiahisaiah.png")
        self.logo_inicio = pygame.transform.scale(self.logo_inicio, (500, 200))
        self.boton_user = Bottom("BOTONES\start.png", 300, 400, (300, 100))
        self.opcion_seleccionada = None
        self.contenedor_niveles = None
        self.exit_menu = Bottom("BOTONES\exit_renovado.png", 20, 10, (100, 40))

        #menu-----------------------------------------------------------------------------------
        self.play = Bottom("BOTONES\play_renovado.png", 600, 500, (200, 70))
        self.exit = Bottom("BOTONES\exit_renovado.png", 100, 500, (200, 70))
        self.boton_nivel1 = Bottom(r"BOTONES\Nivel 1.png", 326, 200, (120, 120))
        self.boton_nivel2 = Bottom(r"BOTONES\nivel 2.png", 475, 200, (120, 120))
        self.boton_nivel3 = Bottom(r"BOTONES\nivel 3.png", 400, 330, (120, 120))
        self.boton_nivel1_bloqueado = Bottom(r"BOTONES\Nivel1_bloqueado.png", 326, 200, (120, 120))
        self.boton_nivel2_bloqueado = Bottom(r"BOTONES\nivel2_bloqueado.png", 475, 200, (120, 120))
        self.boton_nivel3_bloqueado = Bottom(r"BOTONES\nivel3_bloqueado.png", 400, 330, (120, 120))

        #Eleccion niveles-------------------------------------------------------------------
        self.fondo_seleccion_niveles = pygame.image.load(r"BOTONES\fondo_score.png")
        self.fondo_seleccion_niveles = pygame.transform.scale(self.fondo_seleccion_niveles, (350, 400))
        self.image_crash = pygame.image.load(r"Portada\4.png")
        self.image_crash = pygame.transform.scale(self.image_crash, (290, 300))
        self.fuente_niveles = pygame.font.SysFont("Algerian", 90)
        self.nivel = None
        self.nivel_1 = None
        self.nivel_2 = None
        self.nivel_3 = None

        #pantalla_final-----------------------------------------------------------------
        self.fondo_fin_juego = pygame.image.load("Fondos de juego\Fondo de juego.jpg")
        self.fondo_fin_juego = pygame.transform.scale(self.fondo_fin_juego, (ANCHO, ALTO))
        self.fondo_ranking = pygame.image.load(r"BOTONES\tabla_clasificacion.png")
        self.fondo_ranking = pygame.transform.scale(self.fondo_ranking, (370, 400))
        self.logo_player = pygame.image.load(r"BOTONES\kisspng-user-silhouette-simplicity-vector-5b52f75d202791.0292972215321639331317.png")
        self.logo_player = pygame.transform.scale(self.logo_player, (40, 40))
        self.logo_win = pygame.image.load("Fondos de juego\win_logo.png")
        self.logo_win = pygame.transform.scale(self.logo_win, (400, 170))
        self.logo_game_over = pygame.image.load("Fondos de juego\game_over.png")
        self.logo_game_over = pygame.transform.scale(self.logo_game_over, (340, 120))
        self.reiniciar_nivel = Bottom("BOTONES\pngwing.com (13).png", 60, 400, (100, 100))
        self.boton_menu = Bottom("BOTONES\Menu.png", 750, 400, (100, 100))
        self.exit_ranking = Bottom("BOTONES\exit_renovado.png", 20, 420, (200, 60))

        #Pausa-----------------------------------------------------------------------------
        self.fuente_pause = pygame.font.SysFont("Cooper", 40)
        self.boton_pausa = Bottom("BOTONES\pausa_boton.png", 390, 300, (135, 120))
        self.boton_mas_musica = Bottom(r"BOTONES\boton_mas.png", 550, 190, (40, 40))
        self.boton_menos_musica = Bottom(r"BOTONES\boton_menos.png", 500, 190, (40, 40))
        self.boton_mas_sonido = Bottom(r"BOTONES\boton_mas.png", 550, 240, (40, 40))
        self.boton_menos_sonido = Bottom(r"BOTONES\boton_menos.png", 500, 240, (40, 40))
        #---------------------------------------------------------------------------------
        pygame.mixer.init()
        pygame.mixer.music.load("sounds\musica-espera-separador-musical-.mp3")
        pygame.mixer.music.play(-1)
        self.reloj = pygame.time.Clock
        self.cronometro_transicion = Cronometro(0, True, 3)
        self.barra_carga_nivel = Barra(220, 500, 450, 40, ROJO, VERDE, self.cronometro_transicion.mostrar_tiempo(), 2)
        self.musica_nivel_1 = "sounds\Electronic Fantasy.ogg"
        self.musica_nivel_2 = "sounds\sonic-sth_OcGsuVMq.mp3"
        self.musica_nivel_3 = "sounds\ringtones-super-mario-bros.mp3"
        #--------------------------------------------------------------------------------
        self.level_1 = pygame.image.load("BOTONES\LEVEL_1.png")
        self.level_1 = pygame.transform.scale(self.level_1, (450, 250))

        self.level_2 = pygame.image.load("BOTONES\LEVEL_2.png")
        self.level_2 = pygame.transform.scale(self.level_2, (450, 250))

        self.level_3 = pygame.image.load("BOTONES\LEVEL_3.png")
        self.level_3 = pygame.transform.scale(self.level_3, (450, 250))

        self.nivel_1_activado = True
        self.nivel_2_activado = False
        self.nivel_3_activado = False

    def run(self):
        pygame.init()
        while self.on:
            print(self.estado_juego)
            eventos = pygame.event.get()
            if self.estado_juego == "inicio":
                self.inicio()
                self.estado_juego = "menu"
            
            elif self.estado_juego == "menu":
                self.menu()

            elif self.estado_juego == "jugando":
                self.contenedor_niveles.play(eventos)
                if not self.contenedor_niveles.get_fin_de_juego():
                    if self.contenedor_niveles.get_pausa():
                        self.pausa()
                        self.contenedor_niveles.cronometro.encender()

                    if self.contenedor_niveles.get_reiniciar():
                        self.reiniciar()
                elif self.contenedor_niveles.get_resultado():
                    self.gameplay()
                
                else:
                    self.puntuacion =+ self.contenedor_niveles.get_puntuacion()
                    self.estado_juego = "game_over"

            elif self.estado_juego == "game_over" or self.estado_juego == "gano":
                self.pantalla_final()
                
            else:
                print("ERROR")
                self.on = False

    def inicio(self):
        while self.user == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.manejo_volumen_musica()
            self.pantalla.fill(COLOR_MENU)
            self.pantalla.blit(self.logo_inicio, (200, 50))

            self.txt_user.dibujar(self.pantalla, pygame.event.get())
            self.boton_user.dibujar(self.pantalla)
            self.exit_menu.dibujar(self.pantalla)
            self.resetear_juego.dibujar(pantalla)

            if self.boton_user.se_hace_clic() == True:
                self.user = self.txt_user.get_text()
                self.estado_juego = "menu"
            
            if self.exit_menu.se_hace_clic() == True:
                pygame.quit()
                sys.exit()

            if self.resetear_juego.se_hace_clic() == True:
                resetear_juego(self.base_datos)
            pygame.display.flip()


    def menu(self):
        self.logo_inicio = pygame.transform.scale(self.logo_inicio, (300, 100))
        self.nivel_seleccionado = None
        self.contenedor_niveles = None

        while self.estado_juego == "menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.manejo_volumen_musica()
            self.pantalla.fill(COLOR_MENU)
            self.pantalla.blit(self.image_crash, (10, 170))
            self.pantalla.blit(self.image_crash, (600, 170))
            self.pantalla.blit(self.fondo_seleccion_niveles, (280, 100))
            self.pantalla.blit(self.logo_inicio, (300, 20))

            self.play.dibujar(self.pantalla)
            self.exit.dibujar(self.pantalla)

            if self.nivel_1_activado:
                self.boton_nivel1.dibujar(self.pantalla)
            else:
                self.boton_nivel1_bloqueado.dibujar(self.pantalla)

            if self.nivel_2_activado:
                self.boton_nivel2.dibujar(self.pantalla)
            else:
                self.boton_nivel2_bloqueado.dibujar(self.pantalla)

            if self.nivel_3_activado:
                self.boton_nivel3.dibujar(self.pantalla)
            else:
                self.boton_nivel3_bloqueado.dibujar(self.pantalla)

#-------------------------------------------------------------------------

            if self.boton_nivel1.se_hace_clic() == True and self.nivel_1_activado:
                self.nivel_seleccionado = 1
            
            if self.boton_nivel2.se_hace_clic() == True and self.nivel_2_activado:
                self.nivel_seleccionado = 2

            if self.boton_nivel3.se_hace_clic() == True and self.nivel_3_activado:
                self.nivel_seleccionado = 3

            if self.play.se_hace_clic() == True and self.nivel_seleccionado is not None:
                self.cargar_niveles()
                self.estado_juego = "jugando"
                pygame.mixer.music.pause()
                pygame.mixer.music.load("sounds\Electronic Fantasy.ogg")
                pygame.mixer.music.play(1)
                pygame.mixer.music.set_volume(VOL_PREDETERMINADO)
                self.contenedor_niveles = self.nivel
            
            if self.exit.se_hace_clic() == True:
                pygame.quit()
                sys.exit()

            pygame.display.flip()

    def gameplay(self):
        self.manejo_nivel = False
        while not self.manejo_nivel:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.nivel_seleccionado == 1 and self.manejo_nivel == False:
                self.puntuacion =+ self.contenedor_niveles.get_puntuacion()
                self.nivel_2_activado = True
                self.manejo_nivel = True
                self.cargar_nivel(2)
                self.escena_trancision(2)
                self.estado_juego = "jugando"
                pygame.mixer.music.pause()
                pygame.mixer.music.load("sounds\sonic-sth_OcGsuVMq.mp3")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(VOL_PREDETERMINADO)

            elif self.nivel_seleccionado == 2 and self.manejo_nivel == False:
                self.puntuacion =+ self.contenedor_niveles.get_puntuacion()
                self.nivel_3_activado = True
                self.manejo_nivel = True
                self.cargar_nivel(3)
                self.escena_trancision(3)
                self.estado_juego = "jugando"
                pygame.mixer.music.pause()
                pygame.mixer.music.load(r"sounds\ringtones-super-mario-bros.mp3")
                pygame.mixer.music.play(-1)
            
            elif self.nivel_seleccionado == 3 and self.manejo_nivel == False:
                self.manejo_nivel = True
                self.estado_juego = "gano"

            pygame.display.flip()


    def pantalla_final(self):
        pygame.mixer.music.pause()
        if self.estado_juego == "gano":
            pygame.mixer.music.load(r"sounds\010564339_prev.mp3")
        elif self.estado_juego == "game_over":
            pygame.mixer.music.load(r"sounds\010607643_prev.mp3")
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(VOL_PREDETERMINADO)

        agregar_regristro(self.base_datos, self.user, self.puntuacion)
        lista_ranking = traer_ranking(self.base_datos)

        for lista in lista_ranking:
            print(lista)
        while self.estado_juego == "gano" or self.estado_juego == "game_over":
            self.manejo_volumen_musica()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.pantalla.fill(COLOR_MENU)
            self.pantalla.blit(self.fondo_ranking, (260, 150))

            if self.estado_juego == "gano":
                self.pantalla.blit(self.logo_win, (250, 0))
            elif self.estado_juego == "game_over":
                self.pantalla.blit(self.logo_game_over, (270, 20))

            self.exit_ranking.dibujar(self.pantalla)
            self.boton_menu.dibujar(self.pantalla)

            if self.exit_ranking.se_hace_clic() == True: 
                pygame.quit()
                sys.exit()

            if self.boton_menu.se_hace_clic() == True:
                self.estado_juego = "menu"
                self.puntuacion = 0
                print("volver_menu")

            if len(lista_ranking) == 1:
                user_surface = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[0][0]} || {lista_ranking[0][1]}", UBICACION_PRIMER_PUESTO_USER, NEGRO)
                self.pantalla.blit(self.logo_player,  UBICACION_PRIMER_PUESTO_LOGO)
                user_surface.dibujar(self.pantalla)
            elif len(lista_ranking) == 2:
                user_surface = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[0][0]} || {lista_ranking[0][1]}", UBICACION_PRIMER_PUESTO_USER, NEGRO)
                user_surface_2 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[1][0]} || {lista_ranking[1][1]}", UBICACION_SEGUNDO_PUESTO_USER, NEGRO)
                self.pantalla.blit(self.logo_player,  UBICACION_PRIMER_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_SEGUNDO_PUESTO_LOGO)
                user_surface.dibujar(self.pantalla)
                user_surface_2.dibujar(self.pantalla)
            elif len(lista_ranking) == 3:
                user_surface = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[0][0]} || {lista_ranking[0][1]}", UBICACION_PRIMER_PUESTO_USER, NEGRO)
                user_surface_2 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[1][0]} || {lista_ranking[1][1]}", UBICACION_SEGUNDO_PUESTO_USER, NEGRO)
                user_surface_3 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[2][0]} || {lista_ranking[2][1]}", UBICACION_TERCER_PUESTO_USER, NEGRO)
                self.pantalla.blit(self.logo_player,  UBICACION_PRIMER_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_SEGUNDO_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_TERCER_PUESTO_LOGO)
                user_surface.dibujar(self.pantalla)
                user_surface_2.dibujar(self.pantalla)
                user_surface_3.dibujar(self.pantalla)
            else:
                user_surface = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[0][0]} || {lista_ranking[0][1]}", UBICACION_PRIMER_PUESTO_USER, NEGRO)
                user_surface_2 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[1][0]} || {lista_ranking[1][1]}", UBICACION_SEGUNDO_PUESTO_USER, NEGRO)
                user_surface_3 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[2][0]} || {lista_ranking[2][1]}", UBICACION_TERCER_PUESTO_USER, NEGRO)
                user_surface_4 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[3][0]} || {lista_ranking[3][1]}", UBICACION_CUARTO_PUESTO_USER, NEGRO)
                self.pantalla.blit(self.logo_player,  UBICACION_PRIMER_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_SEGUNDO_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_TERCER_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_CUARTO_PUESTO_LOGO)
                user_surface.dibujar(self.pantalla)
                user_surface_2.dibujar(self.pantalla)
                user_surface_3.dibujar(self.pantalla)
                user_surface_4.dibujar(self.pantalla)

            pygame.display.flip()

    def reiniciar(self):
        self.cargar_niveles()
        self.contenedor_niveles = self.nivel
        self.estado_juego = "jugando"

    def cargar_nivel(self, nivel):
        self.nivel_seleccionado = nivel
        self.cargar_niveles()
        self.contenedor_niveles = self.nivel

    def cargar_niveles(self):
        with open('Nivel.json') as file:
            data = json.load(file)
        if self.nivel_seleccionado == 1:
            info_piso = data["Nivel_1"]["Piso"]
            info_plataforma_1 = data["Nivel_1"]["Plataforma_1"]
            info_plataforma_2 = data["Nivel_1"]["Plataforma_2"]
            info_plataforma_3 = data["Nivel_1"]["Plataforma_3"]
            info_plataforma_4 = data["Nivel_1"]["Plataforma_4"]
            info_caja = data["Nivel_1"]["caja"]
            info_caja_1 = data["Nivel_1"]["caja_1"]
            info_caja_2 = data["Nivel_1"]["caja_2"]
            piso = Piso(info_piso["imagen"], info_piso["dimensiones"], info_piso["ubicacion"])
            plataforma_1 = Piso(info_plataforma_1["imagen"], info_plataforma_1["dimensiones"], info_plataforma_1["ubicacion"])
            plataforma_2 = Piso(info_plataforma_2["imagen"], info_plataforma_2["dimensiones"], info_plataforma_2["ubicacion"])
            plataforma_3 = Piso(info_plataforma_3["imagen"], info_plataforma_3["dimensiones"], info_plataforma_3["ubicacion"])
            plataforma_4 = Piso(info_plataforma_4["imagen"], info_plataforma_4["dimensiones"], info_plataforma_4["ubicacion"])

            caja = Piso(info_caja["imagen"], info_caja["dimensiones"], info_caja["ubicacion"])

            caja_1 = Piso(info_caja_1["imagen"], info_caja_1["dimensiones"], info_caja_1["ubicacion"])
            caja_2 = Piso(info_caja_2["imagen"], info_caja_2["dimensiones"], info_caja_2["ubicacion"])
            cajas = [caja, caja_1, caja_2]
            plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4]
            self.nivel = Nivel(r"Fondos de juego\fondo_juego.jpg", plataformas, cajas, self.puntuacion)

        elif self.nivel_seleccionado == 2:
            info_piso = data["Nivel_2"]["Piso"]
            info_plataforma_1 = data["Nivel_2"]["Plataforma_1"]
            info_plataforma_2 = data["Nivel_2"]["Plataforma_2"]
            info_plataforma_3 = data["Nivel_2"]["Plataforma_3"]
            info_plataforma_4 = data["Nivel_2"]["Plataforma_4"]
            info_plataforma_5 = data["Nivel_2"]["Plataforma_5"]
            info_plataforma_6 = data["Nivel_2"]["Plataforma_6"]

            info_caja_1 = data["Nivel_2"]["caja_1"]
            info_caja_2 = data["Nivel_2"]["caja_2"]
            
            piso = Piso(info_piso["imagen"], info_piso["dimensiones"], info_piso["ubicacion"])
            plataforma_1 = Piso(info_plataforma_1["imagen"], info_plataforma_1["dimensiones"], info_plataforma_1["ubicacion"])
            plataforma_2 = Piso(info_plataforma_2["imagen"], info_plataforma_2["dimensiones"], info_plataforma_2["ubicacion"])
            plataforma_3 = Piso(info_plataforma_3["imagen"], info_plataforma_3["dimensiones"], info_plataforma_3["ubicacion"])
            plataforma_4 = Piso(info_plataforma_4["imagen"], info_plataforma_4["dimensiones"], info_plataforma_4["ubicacion"])
            plataforma_5 = Piso(info_plataforma_5["imagen"], info_plataforma_5["dimensiones"], info_plataforma_5["ubicacion"])
            plataforma_6 = Piso(info_plataforma_6["imagen"], info_plataforma_6["dimensiones"], info_plataforma_6["ubicacion"])
            caja_1 = Piso(info_caja_1["imagen"], info_caja_1["dimensiones"], info_caja_1["ubicacion"])
            caja_2 = Piso(info_caja_2["imagen"], info_caja_2["dimensiones"], info_caja_2["ubicacion"])

            cajas = [caja_1, caja_2]
            plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4, plataforma_5, plataforma_6]
            self.nivel = Nivel_2(r"Fondos de juego\47792.jpg", plataformas, cajas, self.puntuacion)

        elif self.nivel_seleccionado == 3:
            info_piso = data["Nivel_3"]["Piso"]
            info_plataforma_1 = data["Nivel_3"]["Plataforma_1"]
            info_plataforma_2 = data["Nivel_3"]["Plataforma_2"]
            info_plataforma_3 = data["Nivel_3"]["Plataforma_3"]
            info_plataforma_4 = data["Nivel_3"]["Plataforma_4"]
            info_plataforma_5 = data["Nivel_3"]["Plataforma_5"]
            piso = Piso(info_piso["imagen"], info_piso["dimensiones"], info_piso["ubicacion"])
            plataforma_1 = Piso(info_plataforma_1["imagen"], info_plataforma_1["dimensiones"], info_plataforma_1["ubicacion"])
            plataforma_2 = Piso(info_plataforma_2["imagen"], info_plataforma_2["dimensiones"], info_plataforma_2["ubicacion"])
            plataforma_3 = Piso(info_plataforma_3["imagen"], info_plataforma_3["dimensiones"], info_plataforma_3["ubicacion"])
            plataforma_4 = Piso(info_plataforma_4["imagen"], info_plataforma_4["dimensiones"], info_plataforma_4["ubicacion"])
            plataforma_5 = Piso(info_plataforma_5["imagen"], info_plataforma_5["dimensiones"], info_plataforma_5["ubicacion"])
            cajas = []
            plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4, plataforma_5]
            self.nivel = Nivel3(r"Fondos de juego\vecteezy_alien-planet-game-background_6316482.jpg", plataformas, cajas, self.puntuacion)

    def pausa(self):
        while self.contenedor_niveles.get_pausa():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.pantalla.fill(COLOR_MENU)
            self.pantalla.blit(self.fuente_niveles.render("PAUSA", 0, NEGRO), (310, 20))
            self.pantalla.blit(self.fondo_seleccion_niveles, (290, 100))
            self.pantalla.blit(self.fuente_pause.render("MUSICA", 0, NEGRO), (330, 200))
            self.pantalla.blit(self.fuente_pause.render("SONIDO", 0, NEGRO), (330, 250))

            self.boton_pausa.dibujar(self.pantalla)
            self.boton_mas_musica.dibujar(self.pantalla)
            self.boton_mas_sonido.dibujar(self.pantalla)

            self.boton_menos_musica.dibujar(self.pantalla)
            self.boton_menos_sonido.dibujar(self.pantalla)

            if self.boton_pausa.se_hace_clic():
                self.contenedor_niveles.pause = False

            if self.boton_mas_musica.se_hace_clic() == True:
                self.control_volumen_musica(True)
                self.pantalla.blit(self.fuente_pause.render("MUSICA", 0, VERDE), (330, 200))
            
            elif self.boton_menos_musica.se_hace_clic() == True:
                self.control_volumen_musica(False)
                self.pantalla.blit(self.fuente_pause.render("MUSICA", 0, ROJO), (330, 200))

            elif self.boton_mas_sonido.se_hace_clic() == True:
                self.control_volumen_sonido(True)
                self.pantalla.blit(self.fuente_pause.render("SONIDO", 0, VERDE), (330, 250))
            
            elif self.boton_menos_sonido.se_hace_clic() == True:
                self.control_volumen_sonido(False)
                self.pantalla.blit(self.fuente_pause.render("SONIDO", 0, ROJO), (330, 250))
            

            pygame.display.flip()

    def control_volumen_musica(self, control= False):
        if not control:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        else:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)        

    def control_volumen_sonido(self, control):
        self.contenedor_niveles.configuracion_sonidos(control)

    def manejo_volumen_musica(self):
        teclas_presionadas = pygame.key.get_pressed()
        if teclas_presionadas[pygame.K_F3]:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()- 0.01)
            print("-")
        elif teclas_presionadas[pygame.K_F4]:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+ 0.01)
            print("+")

    def escena_trancision(self, numero):
        self.fin_transicion = False
        self.primera_iteracion = False
        self.cronometro_transicion.reiniciar(0, True, 3)

        while not self.fin_transicion:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if not self.primera_iteracion:
                self.cronometro_transicion.encender()
                self.primera_iteracion = True

            self.pantalla.fill(NEGRO)
            if numero == 1:
                self.pantalla.blit(self.level_1, (220, 100))
            elif numero == 2:
                self.pantalla.blit(self.level_2, (220, 100))
            elif numero == 3:
                self.pantalla.blit(self.level_3, (220, 100))
            self.barra_carga_nivel.actualizar(self.pantalla, self.cronometro_transicion.mostrar_tiempo())

            self.cronometro_transicion.actualizar()
            if self.cronometro_transicion.termino():
                self.fin_transicion = True
                self.estado_juego = "jugando"
            pygame.display.flip()        


pantalla = pygame.display.set_mode((ANCHO, ALTO))
game = Game(pantalla, "base_datos.db")
game.run()