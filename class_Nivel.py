import pygame, sys

from class_Personaje import Personaje
from class_enemigo import *
from class_item import *
from class_Piso import *
from class_sapo import Sapo
from config import *
from imagenes import *
from config import *
from Class_Proyectiles import Laser
from cronometro import Cronometro


class Nivel:
    def __init__(self, fondo_path, plataformas, cajas, puntuacion) -> None:
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.fondo = pygame.image.load(fondo_path) 
        self.fondo = pygame.transform.scale(self.fondo, (ANCHO, ALTO))
        self.player = Personaje(TAM_CRASH, CENTER, "Crash\Crash Quieto\Crash Style_1 (1).png", 7, imagenes_player, 3)
        self.plataformas = plataformas
        self.cajas = cajas
        self.genearador_cangrejos = GenearadorEnemigos(r"cangrejos\0.png", TAM_CANGRI, 7, imagenes_cangrejos)
        self.genearador_sapos = GenearadorEnemigos(r"sapos\0.png", TAM_SAPO, 5, animaciones_sapo)
        self.lista_enemigos = self.genearador_cangrejos.generar_enemigos(Enemigo, 3)
        self.lista_sapos = self.genearador_sapos.generar_enemigos(Sapo, 2)
        self.Fuente = pygame.font.SysFont("Segoe Print", 30)
        self.puntuacion = puntuacion
        self.lista_frutas = crear_objetos_random(Item, imagenes_fruta, r"frutitas\0.png", TAM_ITEM, 3)
        self.laser = Laser(r"disparo.png", self.player.rect.bottomright, 15)
        self.bala_viva = False
        self.rectangulos_prog = False
        self.gano = None
        self.fin_juego = False
        self.pause = False
        self.reset = False

        pygame.mixer.init()
        self.sonido_disparo = pygame.mixer.Sound("sounds\laser.mp3")
        self.sonido_muerte = pygame.mixer.Sound("sounds\menos_vida.mp3")
        self.sonido_menos_vida = pygame.mixer.Sound("sounds\mario-mario-touch-enemy.mp3")
        self.sonido_item = pygame.mixer.Sound(r"sounds\mario-coin.mp3")

        self.reloj = pygame.time.Clock()
        self.contador_enemigos = 0
        self.objetos_collision_plataformas = [self.player]
        self.objetos_collision_plataformas = agregar_lista_a_lista(self.objetos_collision_plataformas, self.lista_sapos)
        self.objetos_collision_plataformas = agregar_lista_a_lista(self.objetos_collision_plataformas, self.lista_enemigos)
        self.bandera = False
        self.cronometro = Cronometro(20, False, 0)
        self.tiempo_pausa = 0

    def play(self, lista_eventos):
        self.reloj.tick(30)
        if self.bandera == False:
            self.cronometro.encender()
            self.bandera = True
        self.leer_inputs(lista_eventos)
        self.collisiones()
        self.disparos_collisiones()
        self.actualizar_estado_juego()
        self.cronometro.actualizar()
        self.actualizar_pantalla()  

    def leer_inputs(self, lista_eventos):
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if self.bala_viva == False and self.pause == False:
                        self.laser = Laser("disparo.png", self.player.rect.midright, 20)
                        self.sonido_disparo.play()
                        self.bala_viva = True
                elif event.key == pygame.K_z:
                    if self.bala_viva == False and self.pause == False:
                        self.laser = Laser("disparo.png", self.player.rect.midright, 20, False)
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
        
        if self.pause:
            self.tiempo_pausa = self.cronometro.mostrar_tiempo()
            self.cronometro.reiniciar(self.tiempo_pausa, False, 0)

    def collisiones(self):
        collision_objeto_plataforma(self.objetos_collision_plataformas, self.plataformas)
        collision_player_caja(self.player, self.cajas)

        if len(self.lista_frutas) != 0:
            for fruta in self.lista_frutas:
                if colision_fruta_plataforma(fruta, self.plataformas):
                    fruta.esta_cayendo = False

                if colision_fruta_otro_objeto(fruta, self.player):
                    self.sonido_item.play()
                    self.lista_frutas.remove(fruta)
                    self.puntuacion += PUNTAJE_FRUTA
        else:
            self.lista_frutas = crear_objetos_random(Item, imagenes_fruta, r"frutitas\0.png", TAM_ITEM, 5)

        if len(self.lista_enemigos) != 0:
            for enemigo in self.lista_enemigos: 
                if enemigo.toco == False and enemigo.rect.colliderect(self.player.rect):
                    enemigo.toco = True
                    self.player.vidas -= 1
                    self.sonido_menos_vida.play()
                elif not enemigo.rect.colliderect(self.player.rect):
                    enemigo.toco = False
                
                if enemigo.rect.y > ALTO:
                    self.lista_enemigos.remove(enemigo)
        else:
            self.lista_enemigos = self.genearador_cangrejos.generar_enemigos(Enemigo, 3)
            self.objetos_collision_plataformas = agregar_lista_a_lista(self.objetos_collision_plataformas, self.lista_enemigos)

        if len(self.lista_sapos) != 0:
            for sapo in self.lista_sapos: 
                if sapo.toco == False and sapo.rect.colliderect(self.player.rect):
                    sapo.toco = True
                    self.player.vidas -= 1
                    self.sonido_menos_vida.play()
                elif not sapo.rect.colliderect(self.player.rect):
                    sapo.toco = False
        else:
            self.lista_sapos = self.genearador_sapos.generar_enemigos(Sapo, 3)
            self.objetos_collision_plataformas = agregar_lista_a_lista(self.objetos_collision_plataformas, self.lista_sapos)

    def actualizar_pantalla(self):
        self.pantalla.blit(self.fondo, (0, 0))
        for plataforma in self.plataformas:
            self.pantalla.blit(plataforma.image, plataforma.rect)
        for caja in self.cajas:
            self.pantalla.blit(caja.image, caja.rect)

        for fruta in self.lista_frutas:
            fruta.actualizar(self.pantalla)

        if self.rectangulos_prog:
            for enemigo in self.lista_enemigos:
                for key in enemigo.lados:
                    pygame.draw.rect(self.pantalla, AZUL, enemigo.lados[key], 2)

            for piso in self.plataformas:
                for key in piso.lados:
                    pygame.draw.rect(self.pantalla, AZUL, piso.lados[key], 2)

            for key in self.player.lados:
                pygame.draw.rect(self.pantalla, AZUL, self.player.lados[key], 2)

        self.pantalla.blit(self.Fuente.render(f"X{self.player.vidas}", 0, NEGRO), UBICACION_VIDA)
        self.pantalla.blit(self.Fuente.render(f"Puntos: {self.puntuacion}", 0, NEGRO), UBICACION_PUNTUACION)
        self.pantalla.blit(self.Fuente.render(f"Tiempo: {int(self.cronometro.mostrar_tiempo())}", 0, BLANCO), UBICACION_TIEMPO)

        for enemigo in self.lista_enemigos:
            enemigo.actualizar(self.pantalla)

        self.player.actualizar(self.pantalla)
        if self.bala_viva:
            self.laser.actualizar(self.pantalla)

        for sapo in self.lista_sapos:
            sapo.actualizar(self.pantalla)
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
        self.cronometro.reiniciar(self.tiempo_pausa, False, 0)
        
    def get_fin_de_juego(self):
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
    
    def get_reiniciar(self):
        return self.reset
    
    def get_pausa(self):
        return self.pause
    
    def configuracion_sonidos(self, volumen):
        if volumen != None:
            if volumen:
                self.sonido_disparo.set_volume(self.sonido_disparo.get_volume() + 0.5)
                self.sonido_item.set_volume(self.sonido_item.get_volume() + 0.5)
                self.sonido_muerte.set_volume(self.sonido_muerte.get_volume() + 0.5)
                self.sonido_menos_vida.set_volume(self.sonido_menos_vida.get_volume() + 0.5)
            else:
                self.sonido_disparo.set_volume(self.sonido_disparo.get_volume() - 0.5)
                self.sonido_item.set_volume(self.sonido_item.get_volume() - 0.5)
                self.sonido_muerte.set_volume(self.sonido_muerte.get_volume() - 0.5)
                self.sonido_menos_vida.set_volume(self.sonido_menos_vida.get_volume() - 0.5)


    def disparos_collisiones(self):
        if self.bala_viva:
            for enemigo in self.lista_enemigos:
                if enemigo.rect.colliderect(self.laser.rect):
                    self.sonido_muerte.play()
                    self.lista_enemigos.remove(enemigo)
                    self.objetos_collision_plataformas.remove(enemigo)
                    self.puntuacion += PUNTAJE_ENEMIGOS
                    self.contador_enemigos += 1
                    self.bala_viva = False
            for sapo in self.lista_sapos:
                if sapo.rect.colliderect(self.laser.rect):
                    self.sonido_muerte.play()
                    self.lista_sapos.remove(sapo)
                    self.objetos_collision_plataformas.remove(sapo)
                    self.puntuacion += PUNTAJE_ENEMIGOS
                    self.contador_enemigos += 1
                    self.bala_viva = False
            
            if self.laser.rect.x < 0 or self.laser.rect.x >= ANCHO:
                self.bala_viva = False

    def actualizar_estado_juego(self):
        self.cronometro.actualizar()

        if self.cronometro.termino():
            self.fin_juego = True
        else:
            self.fin_juego = False

        if self.puntuacion > PUNTAJE_GANAR:
            self.gano = True
        else:
            self.gano = False

        if self.player.vidas < 1:
            self.fin_juego = True
            self.gano = False
