import pygame, sys
from config import *

pygame.init()

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((800, 600))
Fuente = pygame.font.SysFont("Segoe Print", 50)
text = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode 
    
    pantalla.fill((45, 158, 196))
    palabra = Fuente.render(text, 0, BLANCO)
    pantalla.blit(palabra, (200, 300))
    pygame.display.flip()