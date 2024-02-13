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
from class_Nivel import * 
from class_Nivel2 import * 
from class_Nivel3 import * 
from textbox import *
import json
from based import *

class Game():
    def __init__(self, pantalla, bd) -> None:
        pygame.font.init()
        self.pantalla = pantalla
        self.estado_juego = "inicio"
        self.on = True
        self.puntuacion = 0
        self.nivel_seleccionado = None
        self.base_datos = bd
        self.cronometro = None
        self.tiempo_inicial = 0
        self.tiempo_actual = self.tiempo_inicial
        #menu---------------------------------------------------------------------------
        self.Fuente_user = pygame.font.SysFont("Copperplate Gothic", 50)
        self.Fuente_ranking = pygame.font.SysFont("Copperplate Gothic", 30)
        self.rectangulo_user = pygame.Rect(350, 300, 100, 60)
        self.txt_user = TextBox(self.Fuente_user, NEGRO, "", self.rectangulo_user, BLANCO, 5)
        self.resetear_juego = Bottom("images\BOTONES\pngwing.com (13).png", 800, 50, (50, 50))
        self.user = None
        self.logo_inicio = pygame.image.load(r"images\BOTONES\Crash_bandicoot_logo_by_jerimiahisaiah.png")
        self.logo_inicio = pygame.transform.scale(self.logo_inicio, (500, 200))
        self.boton_user = Bottom("images\BOTONES\ingresar.png", 300, 400, (300, 100))
        self.opcion_seleccionada = None
        self.contenedor_niveles = None

        #Eleccion niveles-------------------------------------------------------------------
        self.boton_nivel1 = Bottom(r"images\BOTONES\Nivel 1.png", 326, 200, (120, 120))
        self.boton_nivel2 = Bottom(r"images\BOTONES\nivel 2.png", 475, 200, (120, 120))
        self.boton_nivel3 = Bottom(r"images\BOTONES\nivel 3.png", 400, 330, (120, 120))
        self.fondo_seleccion_niveles = pygame.image.load(r"images\BOTONES\fondo_score.png")
        self.fondo_seleccion_niveles = pygame.transform.scale(self.fondo_seleccion_niveles, (350, 400))
        self.image_crash = pygame.image.load(r"images\Portada\4.png")
        self.image_crash = pygame.transform.scale(self.image_crash, (290, 300))
        self.fuente_niveles = pygame.font.SysFont("Algerian", 90)
        self.nivel = None

        #pantalla_final-----------------------------------------------------------------
        self.fondo_fin_juego = pygame.image.load("images\Fondos de juego\Fondo de juego.jpg")
        self.fondo_fin_juego = pygame.transform.scale(self.fondo_fin_juego, (ANCHO, ALTO))
        self.fondo_ranking = pygame.image.load(r"images\BOTONES\tabla_clasificacion.png")
        self.fondo_ranking = pygame.transform.scale(self.fondo_ranking, (370, 400))
        self.logo_player = pygame.image.load(r"images\BOTONES\kisspng-user-silhouette-simplicity-vector-5b52f75d202791.0292972215321639331317.png")
        self.logo_player = pygame.transform.scale(self.logo_player, (40, 40))
        self.logo_win = pygame.image.load("images\Fondos de juego\win_logo.png")
        self.logo_win = pygame.transform.scale(self.logo_win, (400, 170))
        self.logo_game_over = pygame.image.load("images\Fondos de juego\game_over.png")
        self.logo_game_over = pygame.transform.scale(self.logo_game_over, (340, 120))
        #Pausa-----------------------------------------------------------------------------
        self.fuente_pause = pygame.font.SysFont("Cooper", 40)
        self.boton_pausa = Bottom("images\BOTONES\pausa_boton.png", 390, 300, (135, 120))
        self.boton_mas_musica = Bottom(r"images\BOTONES\boton_mas.png", 550, 190, (40, 40))
        self.boton_menos_musica = Bottom(r"images\BOTONES\boton_menos.png", 500, 190, (40, 40))
        self.boton_mas_sonido = Bottom(r"images\BOTONES\boton_mas.png", 550, 240, (40, 40))
        self.boton_menos_sonido = Bottom(r"images\BOTONES\boton_menos.png", 500, 240, (40, 40))
        #---------------------------------------------------------------------------------
        pygame.mixer.init()
        pygame.mixer.music.load("sounds\musica-espera-separador-musical-.mp3")
        pygame.mixer.music.play(-1)
        self.reloj = pygame.time.Clock


    def run(self):
        pygame.init()
        while self.on:
            eventos = pygame.event.get()
            if self.estado_juego == "inicio":
                self.inicio()
                self.estado_juego = "niveles"

            elif self.estado_juego == "niveles":
                self.nivel_seleccionado = None
                self.contenedor_niveles = None
                self.eleccion_nivel()

            elif self.estado_juego == "jugando":
                print(self.contenedor_niveles.sonido_disparo.get_volume())
                self.contenedor_niveles.play(eventos)
                if self.contenedor_niveles.get_estado_juego() == True:
                    self.puntuacion = self.contenedor_niveles.get_puntuacion()
                    if self.contenedor_niveles.get_resultado():
                        self.estado_juego = "gano"
                    else:
                        self.estado_juego = "game_over"
                else:
                    if self.contenedor_niveles.get_pausa():
                        self.cronometro = None
                        self.tiempo_inicial = 0
                        self.tiempo_actual = self.tiempo_inicial
                        self.pausa()
                    
                    if self.contenedor_niveles.get_reset():
                        self.reset()

            elif self.estado_juego == "gano":
                self.pantalla_final(True)
            elif self.estado_juego == "game_over":
                self.pantalla_final(False)

            else:
                print("ERROR")
                self.on = False

    def inicio(self):
        while self.user == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            teclas_presionadas = pygame.key.get_pressed()
            if teclas_presionadas[pygame.K_F3]:
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()- 0.01)
                print("-")
            elif teclas_presionadas[pygame.K_F4]:
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+ 0.01)
                print("+")
            self.pantalla.fill(COLOR_MENU)
            self.pantalla.blit(self.logo_inicio, (200, 50))
            self.txt_user.draw(self.pantalla, pygame.event.get())

            self.boton_user.draw(pantalla)
            if self.boton_user.is_clicked() == True:
                self.user = self.txt_user.get_text()
                self.estado_juego = "menu"

            self.resetear_juego.draw(pantalla)
            if self.resetear_juego.is_clicked() == True:
                resetear_juego(self.base_datos)
            pygame.display.flip()

    def eleccion_nivel(self):
        self.contenedor_niveles = None
        while self.contenedor_niveles == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.pantalla.fill(COLOR_MENU)
            self.pantalla.blit(self.fondo_seleccion_niveles, (290, 100))
            self.pantalla.blit(self.image_crash, (10, 170))
            self.pantalla.blit(self.image_crash, (630, 170))
            
            self.pantalla.blit(self.fuente_niveles.render("NIVELES", 0, NEGRO), (300, 20))

            self.boton_nivel1.draw(self.pantalla)
            self.boton_nivel2.draw(self.pantalla)
            self.boton_nivel3.draw(self.pantalla)

            if self.boton_nivel1.is_clicked() == True:
                self.nivel_seleccionado = 1
                self.cargar_nivel()
                self.estado_juego = "jugando"
                pygame.mixer.music.pause()
                pygame.mixer.music.load("sounds\Electronic Fantasy.ogg")
                pygame.mixer.music.play(1)
                pygame.mixer.music.set_volume(VOL_PREDETERMINADO)
                self.contenedor_niveles = self.nivel
                
            if self.boton_nivel2.is_clicked() == True:
                self.nivel_seleccionado = 2
                self.cargar_nivel()
                self.estado_juego = "jugando"
                pygame.mixer.music.pause()
                pygame.mixer.music.load("sounds\sonic-sth_OcGsuVMq.mp3")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(VOL_PREDETERMINADO)
                self.contenedor_niveles = self.nivel

            if self.boton_nivel3.is_clicked() == True:
                self.nivel_seleccionado = 3
                self.cargar_nivel()
                self.estado_juego = "jugando"
                pygame.mixer.music.pause()
                pygame.mixer.music.load(r"sounds\ringtones-super-mario-bros.mp3")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(VOL_PREDETERMINADO)
                self.contenedor_niveles = self.nivel
            pygame.display.flip()

    def pantalla_final(self,resultado):
        pygame.mixer.music.pause()
        if self.estado_juego == "gano":
            pygame.mixer.music.load(r"sounds\010564339_prev.mp3")
        elif self.estado_juego == "game_over":
            pygame.mixer.music.load(r"sounds\010607643_prev.mp3")
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(VOL_PREDETERMINADO)
        agregar_regristro(self.base_datos, self.nivel_seleccionado, self.user, self.puntuacion)
        lista_ranking = traer_ranking(self.base_datos, self.nivel_seleccionado)

        for lista in lista_ranking:
            print(lista)
        while self.estado_juego == "gano" or self.estado_juego == "game_over":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("volver_menu")
                        self.estado_juego = "niveles"
                        
            self.pantalla.fill(COLOR_MENU)
            self.pantalla.blit(self.fondo_ranking, (260, 150))
            if self.estado_juego == "gano":
                self.pantalla.blit(self.logo_win, (250, 0))
            elif self.estado_juego == "game_over":
                self.pantalla.blit(self.logo_game_over, (270, 20))

            if len(lista_ranking) == 1:
                user_surface = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[0][0]} || {lista_ranking[0][1]}", UBICACION_PRIMER_PUESTO_USER, NEGRO)
                self.pantalla.blit(self.logo_player,  UBICACION_PRIMER_PUESTO_LOGO)
                user_surface.draw(self.pantalla)
            elif len(lista_ranking) == 2:
                user_surface = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[0][0]} || {lista_ranking[0][1]}", UBICACION_PRIMER_PUESTO_USER, NEGRO)
                user_surface_2 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[1][0]} || {lista_ranking[1][1]}", UBICACION_SEGUNDO_PUESTO_USER, NEGRO)
                self.pantalla.blit(self.logo_player,  UBICACION_PRIMER_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_SEGUNDO_PUESTO_LOGO)
                user_surface.draw(self.pantalla)
                user_surface_2.draw(self.pantalla)
            elif len(lista_ranking) == 3:
                user_surface = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[0][0]} || {lista_ranking[0][1]}", UBICACION_PRIMER_PUESTO_USER, NEGRO)
                user_surface_2 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[1][0]} || {lista_ranking[1][1]}", UBICACION_SEGUNDO_PUESTO_USER, NEGRO)
                user_surface_3 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[2][0]} || {lista_ranking[2][1]}", UBICACION_TERCER_PUESTO_USER, NEGRO)
                self.pantalla.blit(self.logo_player,  UBICACION_PRIMER_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_SEGUNDO_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_TERCER_PUESTO_LOGO)
                user_surface.draw(self.pantalla)
                user_surface_2.draw(self.pantalla)
                user_surface_3.draw(self.pantalla)
            else:
                user_surface = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[0][0]} || {lista_ranking[0][1]}", UBICACION_PRIMER_PUESTO_USER, NEGRO)
                user_surface_2 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[1][0]} || {lista_ranking[1][1]}", UBICACION_SEGUNDO_PUESTO_USER, NEGRO)
                user_surface_3 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[2][0]} || {lista_ranking[2][1]}", UBICACION_TERCER_PUESTO_USER, NEGRO)
                user_surface_4 = Label(self.Fuente_ranking, NEGRO, f" {lista_ranking[3][0]} || {lista_ranking[3][1]}", UBICACION_CUARTO_PUESTO_USER, NEGRO)
                self.pantalla.blit(self.logo_player,  UBICACION_PRIMER_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_SEGUNDO_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_TERCER_PUESTO_LOGO)
                self.pantalla.blit(self.logo_player, UBICACION_CUARTO_PUESTO_LOGO)
                user_surface.draw(self.pantalla)
                user_surface_2.draw(self.pantalla)
                user_surface_3.draw(self.pantalla)
                user_surface_4.draw(self.pantalla)

            pygame.display.flip()

    def reset(self):
        self.cargar_nivel()
        self.contenedor_niveles = self.nivel

    def cargar_nivel(self):
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
            self.nivel = Nivel(r"images\Fondos de juego\fondo_juego.jpg", plataformas, cajas)

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
            self.nivel = Nivel_2(r"images\Fondos de juego\47792.jpg", plataformas, cajas)

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
            self.nivel = Nivel3(r"images\Fondos de juego\vecteezy_alien-planet-game-background_6316482.jpg", plataformas, cajas)

    def pausa(self):
        while self.contenedor_niveles.get_pausa():
            print(self.contenedor_niveles.sonido_disparo.get_volume())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if self.cronometro == None and (pygame.time.get_ticks() // 1000) > 1:
                self.tiempo_inicial = self.tiempo_inicial + (pygame.time.get_ticks() // 1000)
                self.cronometro = pygame.time.get_ticks() // 1000
            else:
                self.cronometro = pygame.time.get_ticks() // 1000
                self.tiempo_actual = (self.tiempo_inicial - self.cronometro) / -1
            self.pantalla.fill(COLOR_MENU)
            self.pantalla.blit(self.fuente_niveles.render("PAUSA", 0, NEGRO), (310, 20))
            self.pantalla.blit(self.fondo_seleccion_niveles, (290, 100))
            self.pantalla.blit(self.fuente_pause.render("MUSICA", 0, NEGRO), (330, 200))
            self.pantalla.blit(self.fuente_pause.render("SONIDO", 0, NEGRO), (330, 250))

            self.boton_pausa.draw(self.pantalla)
            self.boton_mas_musica.draw(self.pantalla)
            self.boton_mas_sonido.draw(self.pantalla)

            self.boton_menos_musica.draw(self.pantalla)
            self.boton_menos_sonido.draw(self.pantalla)

            if self.boton_pausa.is_clicked():
                self.contenedor_niveles.pause = False

            if self.boton_mas_musica.is_clicked() == True:
                self.control_volumen_musica(True)
                self.pantalla.blit(self.fuente_pause.render("MUSICA", 0, VERDE), (330, 200))
            
            elif self.boton_menos_musica.is_clicked() == True:
                self.control_volumen_musica(False)
                self.pantalla.blit(self.fuente_pause.render("MUSICA", 0, ROJO), (330, 200))

            elif self.boton_mas_sonido.is_clicked() == True:
                self.control_volumen_sonido(True)
                self.pantalla.blit(self.fuente_pause.render("SONIDO", 0, VERDE), (330, 250))
            
            elif self.boton_menos_sonido.is_clicked() == True:
                self.control_volumen_sonido(False)
                self.pantalla.blit(self.fuente_pause.render("SONIDO", 0, ROJO), (330, 250))
            
            self.contenedor_niveles.set_cronometro(int(self.tiempo_actual))
            pygame.display.flip()

    def control_volumen_musica(self, control= False):
        if not control:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        else:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        

    def control_volumen_sonido(self, control):
        self.contenedor_niveles.configuracion_sonidos(control)


pantalla = pygame.display.set_mode((ANCHO, ALTO))
game = Game(pantalla, "ranking.db")
game.run()