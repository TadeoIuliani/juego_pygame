import pygame, sys

from class_Player import *
from class_enemigo import *
from class_item import *
from class_Piso import *
from class_sapo import Sapo
from main_cronometro import Cronometro
from config import *
from imagenes import *
from config import *


class Nivel:
    def __init__(self, fondo_path, plataformas, cajas) -> None:
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.fondo = pygame.image.load(fondo_path) 
        self.fondo = pygame.transform.scale(self.fondo, (ANCHO, ALTO))
        self.player = Player(TAM_CRASH, CENTER, "Crash\Crash Quieto\Crash Style_1 (1).png", 7, imagenes_player, 3)
        self.plataformas = plataformas
        self.cajas = cajas
        self.genearador_cangrejos = GenearadorEnemigos(r"images\cangrejos\0.png", TAM_CANGRI, 7, imagenes_cangrejos)
        self.genearador_sapos = GenearadorEnemigos(r"images\sapos\0.png", (40, 30), 5, animaciones_sapo)
        self.lista_enemigos = self.genearador_cangrejos.generar_enemigos(Enemigo, 3)
        self.lista_sapos = self.genearador_sapos.generar_enemigos(Sapo, 2)
        self.vidas = 3
        self.Fuente = pygame.font.SysFont("Segoe Print", 30)
        self.puntuacion = 0
        self.lista_frutas = crear_objetos_random(Item, imagenes_fruta, r"images\frutitas\0.png", TAM_ITEM, 3)
        self.bala_viva = False
        self.laser = Laser(r"images\disparo.png", self.player.rect.bottomright)
        self.rectangulos_prog = False
        self.gano = None
        self.fin_juego = False
        self.pause = False
        self.reset = False
        self.sonidos_activados = True
        pygame.mixer.init()
        self.sonido_disparo = pygame.mixer.Sound("sounds\laser.mp3")
        self.sonido_muerte = pygame.mixer.Sound("sounds\menos_vida.mp3")
        self.sonido_menos_vida = pygame.mixer.Sound("sounds\menos_vida.mp3")
        self.sonido_item = pygame.mixer.Sound(r"sounds\mario-coin.mp3")
        self.reloj = pygame.time.Clock()
        self.cronometro = None
        self.tiempo_inicio = 60
        self.tiempo_actual = self.tiempo_inicio


    def play(self, lista_eventos):
        self.reloj.tick(30)
        if self.cronometro == None and ((pygame.time.get_ticks() // 1000) > 1):
            self.tiempo_inicio = self.tiempo_inicio + (pygame.time.get_ticks() // 1000)
            self.cronometro = pygame.time.get_ticks() // 1000
        self.configuracion_sonidos()
        self.leer_inputs(lista_eventos)
        self.pausa()
        self.collisiones()
        self.actualizar_pantalla()  


    def leer_inputs(self, lista_eventos):
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if self.bala_viva == False and self.pause == False:
                        self.laser = Laser("images\disparo.png", self.player.rect.midright)
                        self.sonido_disparo.play()
                        self.bala_viva = True
                elif event.key == pygame.K_z:
                    if self.bala_viva == False and self.pause == False:
                        self.laser = Laser("images\disparo.png", self.player.rect.midright, False)
                        self.sonido_disparo.play()
                        self.bala_viva = True
                elif event.key == pygame.K_TAB:
                    self.rectangulos_prog = not self.rectangulos_prog
                elif event.key == pygame.K_r:
                    self.reset = True
                elif event.key == pygame.K_p:
                    self.pause = not self.pause

        teclas_presionadas = pygame.key.get_pressed()
        if teclas_presionadas[pygame.K_LEFT] and self.player.rect.left > ANCHO / ANCHO + 7:
            self.player.estado = "izquierda"
        elif teclas_presionadas[pygame.K_RIGHT] and self.player.rect.right < ANCHO - SPEED:
            self.player.estado = "derecha"
        elif teclas_presionadas[pygame.K_SPACE]:
            self.player.estado = "salta"
        elif teclas_presionadas[pygame.K_x] or teclas_presionadas[pygame.K_z]:
            self.player.estado = "girar"
        else:
            self.player.estado = "quieto"

    def collisiones(self):
        collision_enemigos_plataformas(self.lista_enemigos, self.plataformas)
        collision_sapo_plataformas(self.lista_sapos, self.plataformas)
        collision_player_plataformas(self.player, self.plataformas)
        collision_player_caja(self.player, self.cajas)

        if len(self.lista_frutas) != 0:
            for fruta in self.lista_frutas:
                if colision_fruta_plataforma(fruta, self.plataformas):
                    fruta.esta_cayendo = False

            for fruta in self.lista_frutas:
                if colision_fruta_otro_objeto(fruta, self.player):
                    self.sonido_item.play()
                    self.lista_frutas.remove(fruta)
                    self.puntuacion += 200

        if len(self.lista_enemigos) != 0:
            for enemigo in self.lista_enemigos: 
                if enemigo.toco == False and enemigo.rect.colliderect(self.player.rect):
                    enemigo.toco = True
                    self.vidas -= 1
                    self.sonido_muerte.play()
                elif not enemigo.rect.colliderect(self.player.rect):
                    enemigo.toco = False
                
                if enemigo.rect.y > ALTO:
                    self.lista_enemigos.remove(enemigo)

        if len(self.lista_sapos) != 0:
            for sapo in self.lista_sapos: 
                if sapo.toco == False and sapo.rect.colliderect(self.player.rect):
                    sapo.toco = True
                    self.vidas -= 1
                    self.sonido_muerte.play()
                elif not sapo.rect.colliderect(self.player.rect):
                    sapo.toco = False
                

        if self.puntuacion > 2500: 
            self.gano = True
            self.fin_juego = True

        if self.vidas < 1:
            self.gano = False
            self.fin_juego = True

        if self.bala_viva:
            for enemigo in self.lista_enemigos:
                if enemigo.rect.colliderect(self.laser.rect):
                    self.sonido_muerte.play()
                    self.lista_enemigos.remove(enemigo)
                    self.puntuacion += 100
                    self.bala_viva = False
            for sapo in self.lista_sapos:
                if sapo.rect.colliderect(self.laser.rect):
                    self.sonido_muerte.play()
                    self.lista_sapos.remove(sapo)
                    self.puntuacion += 100
                    self.bala_viva = False
            if self.laser.rect.x < 0:
                self.bala_viva = False
        
            if self.laser.rect.x >= ANCHO:
                self.bala_viva = False
        

        if len(self.lista_frutas) == 0:
            self.lista_frutas = crear_objetos_random(Item, imagenes_fruta, r"images\frutitas\0.png", TAM_ITEM, 5)

        if len(self.lista_enemigos) == 0:
            self.lista_enemigos = self.genearador_cangrejos.generar_enemigos(Enemigo, 3)
            
        if len(self.lista_sapos) == 0:
            self.lista_sapos = self.genearador_sapos.generar_enemigos(Sapo, 3)
        
        self.cronometro = pygame.time.get_ticks() // 1000
        if self.tiempo_actual > 1:
            self.tiempo_actual = self.tiempo_inicio - self.cronometro
        else:
            self.gano = True
            self.fin_juego = True
        print(self.tiempo_actual)



    def actualizar_pantalla(self):
        self.pantalla.blit(self.fondo, (0, 0))
        for plataforma in self.plataformas:
            self.pantalla.blit(plataforma.image, plataforma.rect)
        for caja in self.cajas:
            self.pantalla.blit(caja.image, caja.rect)

        for i in range(len(self.lista_frutas)):
            self.lista_frutas[i].update(self.pantalla)

        if self.rectangulos_prog:
            for enemigo in self.lista_enemigos:
                for key in enemigo.lados:
                    pygame.draw.rect(self.pantalla, AZUL, enemigo.lados[key], 2)

            for piso in self.plataformas:
                for key in piso.lados:
                    pygame.draw.rect(self.pantalla, AZUL, piso.lados[key], 2)

            for key in self.player.lados:
                pygame.draw.rect(self.pantalla, AZUL, self.player.lados[key], 2)

        self.pantalla.blit(self.Fuente.render(f"X{self.vidas}", 0, NEGRO), (50, 20))
        self.pantalla.blit(self.Fuente.render(f"Puntos: {self.puntuacion}", 0, NEGRO), (200, 20))
        self.pantalla.blit(self.Fuente.render(f"Tiempo: {self.tiempo_actual}", 0, BLANCO), (500, 20))

        for enemigo in self.lista_enemigos:
            enemigo.update(self.pantalla)

        self.player.update(self.pantalla)
        if self.bala_viva:
            self.laser.update(self.pantalla)

        for sapo in self.lista_sapos:
            sapo.update(self.pantalla)
        
        pygame.display.flip()


    def pausa(self):    
        if self.pause:
            self.player.velocidad = 0
            for enemigo in self.lista_enemigos:
                enemigo.velocidad = 0
            for sapo in self.lista_sapos:
                sapo.velocidad = 0
        else:
            self.player.velocidad = 7
            for enemigo in self.lista_enemigos:
                enemigo.velocidad = 7
            for sapo in self.lista_sapos:
                sapo.velocidad = 5


    def get_estado_juego(self):
        if self.fin_juego:
            return True
        else:
            return False
    
    def get_resultado(self):
        if self.gano:
            return True
        else:
            return False
        
    def get_puntuacion(self):
        return self.puntuacion
    
    def get_reset(self):
        return self.reset
    
    def get_pausa(self):
        return self.pause
    
    def get_sonido_activado(self):
        return self.sonidos_activados
    
    def set_sonido_activado(self, activado):
        self.sonidos_activados = activado

    def configuracion_sonidos(self):
        if self.sonidos_activados:
            self.sonido_disparo.set_volume(0.3)
            self.sonido_item.set_volume(0.3)
            self.sonido_muerte.set_volume(0.3)
            self.sonido_menos_vida.set_volume(0.3)
        else:
            self.sonido_disparo.set_volume(0.0)
            self.sonido_item.set_volume(0.0)
            self.sonido_muerte.set_volume(0.0)
            self.sonido_menos_vida.set_volume(0.0)
