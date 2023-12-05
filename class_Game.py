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

class Game():
    def __init__(self, pantalla) -> None:
        pygame.font.init()
        self.pantalla = pantalla
        self.estado_juego = "inicio"
        self.Fuente = pygame.font.SysFont("Segoe Print", 30)
        self.user = None
        self.opcion_seleccionada = False
        self.contenedor_niveles = None
        self.on = True
        self.boton_inicio = Bottom(r"images\pisos\boton_play.png", 350, 200, (200, 80))
        self.boton_exit = Bottom(r"images\pisos\boton_exit.png", 350, 400, (200, 80))

        self.boton_nivel1 = Bottom(r"images\BOTONES\Nivel 1.png", 320, 200, (90, 90))
        self.boton_nivel2 = Bottom(r"images\BOTONES\nivel 2.png", 450, 200, (90, 90))
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
                break
    

    def inicio(self):
        text = ""
        while self.user == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        self.user = text.upper()
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 10:
                            text += event.unicode 
            
            palabra = self.Fuente.render(text.upper(), 0, NEGRO)
            self.pantalla.fill((45, 158, 196))
            self.pantalla.blit(palabra, (300, 300))
            pygame.display.flip()

    def menu(self):
        while self.opcion_seleccionada == False:
            print(pygame.mouse.get_pos())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.pantalla.fill((45, 158, 196))
            self.pantalla.blit(self.Fuente.render(self.user, 0, NEGRO), (0, 0))
            if self.boton_inicio.draw(pantalla):
                self.opcion_seleccionada = True

            if self.boton_exit.draw(pantalla):
                self.on = False
                pygame.quit()
                sys.exit()
            pygame.display.flip()

    def eleccion_nivel(self):
        while self.contenedor_niveles == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.pantalla.fill((45, 158, 196))
            self.pantalla.blit(self.fondo_seleccion_niveles, (300, 100))
            if self.boton_nivel1.draw(self.pantalla):
                self.estado_juego = "jugando"
                self.contenedor_niveles = self.Nivel1

            if self.boton_nivel2.draw(self.pantalla):
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
                pantalla.blit(self.Fuente.render(f"{self.user} /  Puntaje: {puntuacion}", 0, VERDE), (300, 250))
                
            else:
                pantalla.blit(self.fondo_fin_juego, (0, 0))
                pantalla.blit(self.imagen_game_over, (300, 250))
                pantalla.blit(self.Fuente.render(f"{self.user} /  Puntaje: {puntuacion}", 0, ROJO), (300, 250))
            pygame.display.flip()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
game = Game(pantalla)
game.run()