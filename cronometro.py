import pygame
from config import *
import sys

class Cronometro():
    def __init__(self, tiempo_inicial : int, asc : True, limite =  None) -> None:
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_actual = self.tiempo_inicial
        self.inicio = False
        self.ascendente = asc
        self.tiempo_pygame = 0
        self.limite = limite

    def encender(self):
        self.inicio = True
        if self.inicio:
            self.tiempo_pygame = pygame.time.get_ticks() // 1000
            if (pygame.time.get_ticks() // 1000) > 1:
                self.tiempo_inicial = self.tiempo_inicial + (pygame.time.get_ticks() // 1000)

    def actualizar(self):
        self.tiempo_pygame = pygame.time.get_ticks() // 1000
        #desciende
        if self.inicio:
            if not self.ascendente:
                self.tiempo_actual = self.tiempo_inicial - self.tiempo_pygame
        #asciende
            else:
                self.tiempo_actual = (self.tiempo_inicial - self.tiempo_pygame) * -1

    def mostrar_tiempo(self):
        return int(self.tiempo_actual)
    
    def termino(self):
        if self.limite is not None and self.tiempo_actual == self.limite:
            return True
        else:
            return False

    def reiniciar(self, tiempo_inicial, asc, limite = None):
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_actual = self.tiempo_inicial
        self.inicio = False
        self.ascendente = asc
        self.tiempo_pygame = 0
        self.limite = limite
        self.tiempo_pygame = 0


    def set_pausa(self, tiempo_pausado):
        self.tiempo_pausado = tiempo_pausado
        self.pausa = True

    def quitar_pausa(self):
        self.pausa = False
        self.tiempo_pausado = 0





# pygame.init()

# pantalla = pygame.display.set_mode((ANCHO, ALTO))
# cro_principal = Cronometro(30, False, 0)

# cro_prausa = Cronometro(0, True)
# reloj = pygame.time.Clock()

# Fuente = pygame.font.SysFont("Segoe Print", 30)
# pausa = False
# encendido = False
# while True:
#     reloj.tick(30)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_x:
#                 cro_principal.encender()

#             elif event.key == pygame.K_p:
#                 cro_prausa.encender()
            
#             elif event.key == pygame.K_r:
#                 cro_principal.reiniciar(30, False)
#                 cro_prausa.reiniciar(0, True)

#     cro_prausa.actualizar()
#     cro_principal.actualizar()

#     pantalla.fill(ROJO)
#     pantalla.blit(Fuente.render(str(cro_principal.mostrar_tiempo()), 0, BLANCO), (0, 0))
#     pantalla.blit(Fuente.render(str(cro_prausa.mostrar_tiempo()), 0, BLANCO), (100, 0))
#     # pantalla.blit(Fuente.render(str(cro_prausa.mostrar_tiempo()), 0, BLANCO), (400, 0))
#     print(cro_principal.tiempo_actual)
    

#     pygame.display.flip()