import pygame

class Bottom():
    def __init__(self, imagen, x, y, tamaño):  
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, tamaño)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.pos = (0, 0)
        self.toco = False
        self.retorno = False

    def draw(self, pantalla):
        self.pos = pygame.mouse.get_pos()
        
        # if self.rect.collidepoint(self.pos):
        #     if pygame.mouse.get_pressed()[0] == 1 and self.toco == False:
        #         self.toco = True
        #         self.retorno = True
            
        #     if pygame.mouse.get_pressed()[0] == 0:
        #         self.toco = False
        pantalla.blit(self.image, self.rect)
        
        return self.retorno
    
    def is_clicked(self):
        self.pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return True
            
        else:
            return False