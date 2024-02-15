import pygame, sys
from config import *

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
        if len(self.text) != 0:
            pygame.draw.line(pantalla, self.color_rect, self.input_rect.bottomleft, self.input_rect.bottomright)
        palabra_surface = self.fuente.render(self.text.upper(), 0, self.color)
        pantalla.blit(palabra_surface, self.input_rect)
        self.input_rect.w = max(10, palabra_surface.get_width() + 10)

    def get_text(self): 
        return self.text.upper()
    
    def remover_ultima_letra(self):
        return self.text[:-1]

class Label():
    def __init__(self, fuente, color, text, rectangulo, color_rectangulo) -> None:
        self.fuente = fuente
        self.color = color
        self.text = text
        self.rect = pygame.Rect(rectangulo)
        self.color_rect = color_rectangulo
    
    def draw(self, pantalla):
        palabra_surface = self.fuente.render(self.text, 0, self.color)
        self.rect.w = palabra_surface.get_width() + 10
        pygame.draw.rect(pantalla, self.color_rect, self.rect, 1)
        pantalla.blit(palabra_surface, self.rect)
