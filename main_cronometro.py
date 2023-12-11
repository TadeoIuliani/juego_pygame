import pygame
import sys
from config import *


class Cronometro:
    def __init__(self, tiempo_inicial):
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_actual = tiempo_inicial
        self.font = pygame.font.SysFont("Arial", 36)
        self.is_running = False
        self.start_time = 0

    def iniciar_cronometro(self):
        self.is_running = True
        self.start_time = pygame.time.get_ticks()

    def detener_cronometro(self):
        self.is_running = False

    def reiniciar_cronometro(self):
        self.tiempo_actual = self.tiempo_inicial
        self.is_running = False

    def actualizar_cronometro(self):
        if self.is_running:
            elapsed_time = pygame.time.get_ticks() - self.start_time
            self.tiempo_actual = self.tiempo_inicial - elapsed_time

            if self.tiempo_actual < 0:
                self.tiempo_actual = 0
                self.is_running = False

    def dibujar_cronometro(self, pantalla):
        tiempo_texto = f"Tiempo: {self.tiempo_actual // 1000}s"
        texto_surface = self.font.render(tiempo_texto, True, BLANCO)
        pantalla.blit(texto_surface, (10, 10))
    
    def get_tiempo_actual(self):
        return self.tiempo_actual // 1000


class Cronometro_2:
    def __init__(self, tiempo_inicial) -> None:
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_actual = self.tiempo_inicial
        self.is_running = False
    
    def iniciar_cronometro(self):
        self.is_running = True
        self.tiempo_pygame = pygame.time.get_ticks // 1000

        self.tiempo_transcurrido = pygame.time.get_ticks() - self.tiempo_inicial

# Ejemplo usandolo:
# pygame.init()
# pantalla = pygame.display.set_mode((ANCHO, ALTO))
# pygame.display.set_caption("Cronometro Example")

# cronometro = Cronometro(tiempo_inicial=10000)  # 10 segundos

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 cronometro.iniciar_cronometro()
#             elif event.key == pygame.K_r:
#                 cronometro.reiniciar_cronometro()

#     pantalla.fill(NEGRO)
#     cronometro.actualizar_cronometro()
#     cronometro.dibujar_cronometro(pantalla)

#     pygame.display.flip()
