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
from textbox import TextBox
import json

class Game():
    def __init__(self, pantalla) -> None:
        pygame.font.init()
        self.pantalla = pantalla
        self.estado_juego = "inicio"
        self.on = True
        self.puntuacion = 0
        #menu---------------------------------------------------------------------------
        self.Fuente_user = pygame.font.SysFont("Copperplate Gothic", 50)
        self.rectangulo_user = pygame.Rect(350, 300, 100, 60)
        self.txt_user = TextBox(self.Fuente_user, NEGRO, "", self.rectangulo_user, BLANCO, 10)
        self.user = None
        self.logo_inicio = pygame.image.load(r"images\BOTONES\Crash_bandicoot_logo_by_jerimiahisaiah.png")
        self.logo_inicio = pygame.transform.scale(self.logo_inicio, (500, 200))
        self.boton_user = Bottom("images\BOTONES\ingresar.png", 300, 400, (300, 100))
        self.opcion_seleccionada = None
        self.contenedor_niveles = None

        #Eleccion niveles-------------------------------------------------------------------
        self.boton_nivel1 = Bottom(r"images\BOTONES\Nivel 1.png", 320, 200, (100, 100))
        self.boton_nivel2 = Bottom(r"images\BOTONES\nivel 2.png", 450, 200, (100, 100))
        self.fondo_seleccion_niveles = pygame.image.load(r"images\BOTONES\fondo_score.png")
        self.fondo_seleccion_niveles = pygame.transform.scale(self.fondo_seleccion_niveles, (350, 400))
        self.image_crash = pygame.image.load(r"images\Portada\4.png")
        self.image_crash = pygame.transform.scale(self.image_crash, (290, 300))

        #pantalla_final-----------------------------------------------------------------
        self.imagen_game_over = pygame.image.load("images\pngegg.png")
        self.imagen_game_over = pygame.transform.scale(self.imagen_game_over, (250, 150))
        self.fondo_fin_juego = pygame.image.load("images\Fondos de juego\Fondo de juego.jpg")
        self.fondo_fin_juego = pygame.transform.scale(self.fondo_fin_juego, (ANCHO, ALTO))

        #Pausa-----------------------------------------------------------------------------
        self.boton_pausa = Bottom("images\BOTONES\pausa_boton.png", 390, 300, (135, 120))
        self.boton_mas_musica = Bottom(r"images\BOTONES\boton_mas.png", 550, 190, (40, 40))
        self.boton_menos_musica = Bottom(r"images\BOTONES\boton_menos.png", 500, 190, (40, 40))

        self.boton_mas_sonido = Bottom(r"images\BOTONES\boton_mas.png", 550, 240, (40, 40))
        self.boton_menos_sonido = Bottom(r"images\BOTONES\boton_menos.png", 500, 240, (40, 40))
        #---------------------------------------------------------------------------------
        pygame.mixer.music.load("sounds\musica-espera-separador-musical-.mp3")
        pygame.mixer.music.play(-1)



    def run(self):
        pygame.init()
        while self.on:
            eventos = pygame.event.get()
            if self.estado_juego == "inicio":
                self.inicio()
                self.estado_juego = "niveles"

            elif self.estado_juego == "niveles":
                self.eleccion_nivel()

            elif self.estado_juego == "jugando":
                self.contenedor_niveles.play(eventos)
                if self.contenedor_niveles.get_estado_juego() == True:
                    self.puntuacion = self.contenedor_niveles.get_puntuacion()
                    if self.contenedor_niveles.get_resultado():
                        self.estado_juego = "gano"
                    else:
                        self.estado_juego = "game_over"
                else:
                    if self.contenedor_niveles.get_pausa():
                        self.pausa()

            elif self.estado_juego == "gano":
                self.pantalla_final(self.puntuacion, True)
            elif self.estado_juego == "game_over":
                self.pantalla_final(self.puntuacion, False)

            else:
                print("ERROR")
                self.on = False

    def inicio(self):
        while self.user == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.pantalla.fill(COLOR_MENU)
            self.pantalla.blit(self.logo_inicio, (200, 50))
            self.txt_user.draw(self.pantalla, pygame.event.get())

            self.boton_user.draw(pantalla)
            if self.boton_user.is_clicked() == True:
                self.user = self.txt_user.get_text()
                self.estado_juego = "menu"
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
            self.boton_nivel1.draw(pantalla)
            self.boton_nivel2.draw(pantalla)

            if self.boton_nivel1.is_clicked() == True:
                self.cargar_nivel(1)
                self.estado_juego = "jugando"
                pygame.mixer.music.pause()
                pygame.mixer.music.load("sounds\Electronic Fantasy.ogg")
                pygame.mixer.music.play(1)
                pygame.mixer.music.set_volume(VOL_PREDETERMINADO)
                self.contenedor_niveles = self.Nivel1
                
            if self.boton_nivel2.is_clicked() == True:
                print("Nivel 2 ... proximamente")
            pygame.display.flip()

    def pantalla_final(self, puntuacion, resultado):
        pygame.mixer.music.pause()
        pygame.mixer.music.load(r"sounds\010607643_prev.mp3")
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(VOL_PREDETERMINADO)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.on = False
            if resultado:
                pantalla.blit(self.fondo_fin_juego, (0, 0))
                pantalla.blit(self.Fuente_user.render(f"{self.user} /  Puntaje: {puntuacion}", 0, VERDE), (300, 250))
                
            else:
                pantalla.blit(self.fondo_fin_juego, (0, 0))
                pantalla.blit(self.imagen_game_over, (300, 100))
                pantalla.blit(self.Fuente_user.render(f"{self.user} /  Puntaje: {puntuacion}", 0, ROJO), (200, 400))
            pygame.display.flip()

    def ranking(self, numero_nivel):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.estado_juego = "niveles"
                    break

            pantalla.blit(self.fondo_fin_juego, (0, 0))
            pantalla.blit(self.Fuente_user.render(f"Proximamente se viene ranking", 0, ROJO), (0, 250))

            pygame.display.flip()

    def reset(self):
        self.contenedor_niveles = self.Nivel1

    def cargar_nivel(self, numero_nivel):
        with open('Nivel.json') as file:
            data = json.load(file)
        if numero_nivel == 1:
            info_piso = data["Piso"]
            info_plataforma_1 = data["Plataforma_1"]
            info_plataforma_2 = data["Plataforma_2"]
            info_plataforma_3 = data["Plataforma_3"]
            info_plataforma_4 = data["Plataforma_4"]
            info_caja = data["caja"]
            info_caja_1 = data["caja_1"]
            info_caja_2 = data["caja_2"]
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
            self.Nivel1 = Nivel(r"images\Fondos de juego\fondo_juego.jpg", plataformas, cajas)

    def pausa(self):
        self.fuente_pause = pygame.font.SysFont("Cooper", 40)
        while self.contenedor_niveles.get_pausa():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pantalla.fill(COLOR_MENU)
            pantalla.blit(self.fondo_seleccion_niveles, (290, 100))
            pantalla.blit(self.fuente_pause.render("MUSICA", 0, NEGRO), (330, 200))
            pantalla.blit(self.fuente_pause.render("SONIDO", 0, NEGRO), (330, 250))
            self.boton_pausa.draw(pantalla)
            self.boton_mas_musica.draw(pantalla)
            self.boton_mas_sonido.draw(pantalla)

            self.boton_menos_musica.draw(pantalla)
            self.boton_menos_sonido.draw(pantalla)

            if self.boton_pausa.is_clicked():
                self.contenedor_niveles.pause = False

            if self.boton_mas_musica.is_clicked() == True:
                self.control_volumen_musica(True)
                pantalla.blit(self.fuente_pause.render("MUSICA", 0, VERDE), (330, 200))
            
            if self.boton_menos_musica.is_clicked() == True:
                self.control_volumen_musica(False)
                pantalla.blit(self.fuente_pause.render("MUSICA", 0, ROJO), (330, 200))

            if self.boton_mas_sonido.is_clicked() == True:
                self.control_volumen_sonido(True)
                pantalla.blit(self.fuente_pause.render("SONIDO", 0, VERDE), (330, 250))
            
            if self.boton_menos_sonido.is_clicked() == True:
                self.control_volumen_sonido(False)
                pantalla.blit(self.fuente_pause.render("SONIDO", 0, ROJO), (330, 250))

            pygame.display.flip()

    def control_volumen_musica(self, control= False):
        if not control:
            pygame.mixer.music.set_volume(VOL_PREDETERMINADO - 0.2)
        else:
            pygame.mixer.music.set_volume(VOL_PREDETERMINADO + 0.2)

    def control_volumen_sonido(self, control):
        self.contenedor_niveles.set_sonido_activado(control)



pantalla = pygame.display.set_mode((ANCHO, ALTO))
game = Game(pantalla)
game.run()