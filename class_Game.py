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

class Game():
    def __init__(self, pantalla) -> None:
        pygame.font.init()
        self.pantalla = pantalla
        self.estado_juego = "inicio"
        #menu---------------------------------------------------------------------------
        self.Fuente_user = pygame.font.SysFont("Copperplate Gothic", 50)
        self.rectangulo_user = pygame.Rect(350, 300, 100, 60)
        self.txt_user = TextBox(self.Fuente_user, NEGRO, "", self.rectangulo_user, BLANCO, 10)
        self.user = None
        self.logo_inicio = pygame.image.load(r"images\Portada\5.png")
        self.logo_inicio = pygame.transform.scale(self.logo_inicio, (250, 250))
        self.boton_user = Bottom("images\BOTONES\ingresar.png", 300, 400, (300, 100))

        self.opcion_seleccionada = None
        self.contenedor_niveles = None

        self.on = True
        self.boton_inicio = Bottom(r"images\BOTONES\play.png", 100, 200, (300, 100))
        self.boton_ranking = Bottom(r"images\BOTONES\ranking.png", 400, 200, (300, 100))

        self.boton_nivel1 = Bottom(r"images\BOTONES\Nivel 1.png", 320, 200, (100, 100))
        self.boton_nivel2 = Bottom(r"images\BOTONES\nivel 2.png", 450, 200, (100, 100))
        self.fondo_seleccion_niveles = pygame.image.load(r"images\BOTONES\fondo_score.png")
        #Pasar a Json a futuro-----------------------------------------------------
        piso = Piso("images\pisos\piso.png", (ANCHO, 80), (0, 525))
        plataforma_1 = Piso("images\pisos\piso.png", (600, 60), (120, 432))
        plataforma_2 = Piso("images\pisos\piso.png", (450, 60), (280, 330))
        plataforma_3 = Piso("images\pisos\piso.png", (400, 60), (120, 220))
        plataforma_4 = Piso("images\pisos\piso.png", (380, 60), (300, 120))
        caja = Piso(r"images\cajas\normal.png", (80, 80), (120, 354))
        caja_2 = Piso(r"images\cajas\normal.png", (80, 80), (640, 250))
        caja_3 = Piso(r"images\cajas\normal.png", (80, 80), (120, 145))
        cajas = [caja, caja_2, caja_3]
        plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4]
        #-----------------------------------------------------------------------------
        self.Nivel1 = Nivel(r"images\Fondos de juego\fondo_juego.jpg", plataformas, cajas)
        self.puntuacion = 0
        #pantalla_final-----------------------------------------------------------------
        self.imagen_game_over = pygame.image.load("images\pngegg.png")
        self.imagen_game_over = pygame.transform.scale(self.imagen_game_over, (250, 150))
        self.fondo_fin_juego = pygame.image.load("images\Fondos de juego\Fondo de juego.jpg")
        self.fondo_fin_juego = pygame.transform.scale(self.fondo_fin_juego, (ANCHO, ALTO))

    def run(self):
        pygame.init()
        while self.on:
            print(self.opcion_seleccionada)
            eventos = pygame.event.get()
            if self.estado_juego == "inicio":
                self.inicio()
                self.estado_juego = "menu"
                
            elif self.estado_juego == "menu":
                self.menu()
                self.estado_juego = "niveles"

            elif self.estado_juego == "niveles":
                self.eleccion_nivel()

            elif self.estado_juego == "jugando":
                self.contenedor_niveles.play(eventos)
                if self.contenedor_niveles.get_estado_juego() == True:
                    self.puntuacion = self.contenedor_niveles.get_puntuacion()
                    if self.contenedor_niveles.get_resultado:
                        self.estado_juego = "gano"
                    else:
                        self.estado_juego = "game_over"
                
            elif self.estado_juego == "gano":
                self.pantalla_final(self.puntuacion, True)
            elif self.estado_juego == "game_over":
                self.pantalla_final(self.puntuacion, False)

            else:
                print("ERROR")
                break

    def inicio(self):
        while self.user == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.pantalla.fill(COLOR_MENU)
            self.pantalla.blit(self.logo_inicio, (330, 50))
            self.txt_user.draw(self.pantalla, pygame.event.get())

            self.boton_user.draw(pantalla)
            if self.boton_user.is_clicked() == True:
                self.user = self.txt_user.get_text()
                self.estado_juego = "menu"
            pygame.display.flip()

    def menu(self):
        while self.opcion_seleccionada not in ["jugar", "ranking"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.pantalla.fill(COLOR_MENU)
            self.pantalla.blit(self.Fuente_user.render(f"Usuario {self.user}", 0, NEGRO), (0, 0))

            self.boton_inicio.draw(self.pantalla)
            self.boton_ranking.draw(self.pantalla)

            if self.boton_inicio.is_clicked() == True:
                self.estado_juego = "niveles"
                self.opcion_seleccionada = "jugar"

            elif self.boton_ranking.is_clicked() == True:
                self.estado_juego = "niveles"
                self.opcion_seleccionada = "ranking"

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
            self.boton_nivel1.draw(pantalla)
            self.boton_nivel2.draw(pantalla)

            if self.boton_nivel1.is_clicked() == True:
                if self.opcion_seleccionada == "jugar":
                    self.estado_juego = "jugando"
                    self.contenedor_niveles = self.Nivel1
                elif self.opcion_seleccionada == "ranking":
                    self.ranking(1)

            if self.boton_nivel2.is_clicked() == True:
                print("Nivel 2 ... proximamente")
            pygame.display.flip()

    def pantalla_final(self, puntuacion, resultado):
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
                pantalla.blit(self.imagen_game_over, (300, 250))
                pantalla.blit(self.Fuente_user.render(f"{self.user} /  Puntaje: {puntuacion}", 0, ROJO), (300, 250))
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


pantalla = pygame.display.set_mode((ANCHO, ALTO))
game = Game(pantalla)
game.run()