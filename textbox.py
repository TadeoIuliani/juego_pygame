import pygame, sys
from config import *

pygame.init()

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((800, 600))
Fuente = pygame.font.SysFont("Segoe Print", 20)
text = ""

input_rect = pygame.Rect(200, 200, 140, 40)

# while True:
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
pygame.draw.rect(pantalla, ROJO, input_rect, 2)

palabra = Fuente.render(text, 0, BLANCO)

pantalla.blit(palabra, (input_rect.x + 5, input_rect.y +5))
input_rect.w = max(100, palabra.get_width() + 10)
pygame.display.flip()


class TextBox():
    def __init__(self, fuente, color, text, rectangulo, color_rectangulo, maximo_letras) -> None:
        self.fuente = fuente
        self.color = color
        self.text = text
        self.input_rect = rectangulo
        self.color_rect = color_rectangulo
        self.maximo = maximo_letras

    def update(self, eventos):
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < self.maximo:
                        self.text += event.unicode


    def draw(self, pantalla, eventos):
        self.update(eventos)
        # pygame.draw.line(pantalla, self.color_rect, self.input_rect.x, self.input_rect.right, 1)
        if len(self.text) != 0:
            pygame.draw.line(pantalla, self.color_rect, self.input_rect.bottomleft, self.input_rect.bottomright)
        palabra_surface = self.fuente.render(self.text.upper(), 0, self.color)
        # pantalla.blit(palabra_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        pantalla.blit(palabra_surface, self.input_rect)
        self.input_rect.w = max(100, palabra_surface.get_width() + 10)

    def get_text(self): 
        return self.text.upper()
    
    def remover_ultima_letra(self):
        return self.text[:-1]