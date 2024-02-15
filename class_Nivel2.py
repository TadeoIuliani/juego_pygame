import pygame, sys
from class_Personaje import Personaje
from class_enemigo import *
from class_item import *
from class_Piso import *
from class_Nivel import *
from config import *
from imagenes import *
from config import *


class Nivel_2(Nivel):
    def __init__(self, fondo_path, plataformas, cajas) -> None:
        super().__init__(fondo_path, plataformas, cajas)
        self.plataformas = agregar_lista_a_lista(self.plataformas, self.cajas)
        self.enemigo_dispara = Enemigo_2("images\camaleon\camaleon_ataque_4.png", (80, 50), 5, camaleon, (500, 300))
        self.contador_camaleon = 1
        self.lista_enemigos = [self.enemigo_dispara]
        pygame.mixer.init()
        self.sonido_disparo = pygame.mixer.Sound("sounds\laser.mp3")
        self.sonido_muerte = pygame.mixer.Sound("sounds\menos_vida.mp3")
        self.sonido_menos_vida = pygame.mixer.Sound("sounds\menos_vida.mp3")
        self.sonido_item = pygame.mixer.Sound(r"sounds\mario-coin.mp3")
        self.sonido_motosierra = pygame.mixer.Sound(r"sounds\sonido_motosierra.mp3")
        self.reloj = pygame.time.Clock()
        self.bala_enemigo = None
        self.vida_bala_enemigo = False
        self.trampa = Trampa(r"images\trampa\Off.png", (30, 30), (200, 170), True, trampa)
        self.trampa_2 = Trampa(r"images\trampa\Off.png", (30, 30), (660, 170), True, trampa)
        self.trampas = [self.trampa, self.trampa_2]
        self.lista_enemigos_cangrejos = self.genearador_cangrejos.generar_enemigos(Enemigo, 3)
        self.objetos_collision_plataformas = [self.player]
        self.objetos_collision_plataformas = agregar_lista_a_lista(self.objetos_collision_plataformas, self.lista_enemigos)
        self.objetos_collision_plataformas = agregar_lista_a_lista(self.objetos_collision_plataformas, self.lista_enemigos_cangrejos)



    def play(self, lista_eventos):
        self.reloj.tick(30)
        if self.cronometro == None and ((pygame.time.get_ticks() // 1000) > 1):
            self.tiempo_inicio = self.tiempo_inicio + (pygame.time.get_ticks() // 1000)
            self.cronometro = pygame.time.get_ticks() // 1000
        self.leer_inputs(lista_eventos)
        self.collisiones()
        self.disparos_collisiones()
        self.trampas_collisiones()
        self.actualizar_estado_juego()
        self.actualizar_pantalla() 
    
    def leer_inputs(self, lista_eventos):
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if self.bala_viva == False and self.pause == False:
                        self.laser = Laser("images\disparo.png", self.player.rect.midright, 20)
                        self.sonido_disparo.play()
                        self.bala_viva = True
                elif event.key == pygame.K_z:
                    if self.bala_viva == False and self.pause == False:
                        self.laser = Laser("images\disparo.png", self.player.rect.midright,20 ,False)
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
        collision_objeto_plataforma(self.objetos_collision_plataformas, self.plataformas)

        if len(self.lista_frutas) != 0:
            for fruta in self.lista_frutas:
                if colision_fruta_plataforma(fruta, self.plataformas):
                    fruta.esta_cayendo = False

            for fruta in self.lista_frutas:
                if colision_fruta_otro_objeto(fruta, self.player):
                    self.sonido_item.play()
                    self.lista_frutas.remove(fruta)
                    self.puntuacion += PUNTAJE_FRUTA
        else:
            self.lista_frutas = crear_objetos_random(Item, imagenes_fruta, r"images\frutitas\0.png", TAM_ITEM, 5)

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
                    self.objetos_collision_plataformas.remove(enemigo)

                if self.player.rect.colliderect(enemigo.rect_tiro):
                    if self.player.rect.x < enemigo.rect.x and self.vida_bala_enemigo == False:
                        enemigo.estado = "atacar_izquierda"
                        self.bala_enemigo = Laser(r"images\Ice Particle.png", enemigo.rect.midleft,10 , False)
                        self.vida_bala_enemigo = True
                    elif self.vida_bala_enemigo == False:
                        enemigo.estado = "atacar_derecha"
                        self.bala_enemigo = Laser(r"images\Ice Particle.png", enemigo.rect.midleft,10 , True)
                        self.vida_bala_enemigo = True
                else:
                    if enemigo.estado == "atacar_derecha":
                        enemigo.estado = "izquierda"
                    elif enemigo.estado == "atacar_izquierda":
                        enemigo.estado = "derecha"

        elif self.contador_camaleon < 2:
            self.contador_camaleon += 1
            self.enemigo_dispara = Enemigo_2("images\camaleon\camaleon_ataque_4.png", (80, 50), 5, camaleon, (0, 100))
            self.lista_enemigos.append(self.enemigo_dispara)
            self.objetos_collision_plataformas = agregar_lista_a_lista(self.objetos_collision_plataformas, self.lista_enemigos)
        
        if len(self.lista_enemigos_cangrejos) != 0:
            for enemigo in self.lista_enemigos_cangrejos: 
                if enemigo.toco == False and enemigo.rect.colliderect(self.player.rect):
                    enemigo.toco = True
                    self.vidas -= 1
                    self.sonido_muerte.play()
                elif not enemigo.rect.colliderect(self.player.rect):
                    enemigo.toco = False
                
                if enemigo.rect.y > ALTO:
                    self.lista_enemigos_cangrejos.remove(enemigo)
                    self.objetos_collision_plataformas.remove(enemigo)
        else:
            self.lista_enemigos_cangrejos = self.genearador_cangrejos.generar_enemigos(Enemigo, 3)
            self.objetos_collision_plataformas = agregar_lista_a_lista(self.objetos_collision_plataformas, self.lista_enemigos_cangrejos)

    def actualizar_pantalla(self):
        self.pantalla.blit(self.fondo, (0, 0))
        for plataforma in self.plataformas:
            self.pantalla.blit(plataforma.image, plataforma.rect)
        for caja in self.cajas:
            self.pantalla.blit(caja.image, caja.rect)

        for fruta in self.lista_frutas:
            fruta.update(self.pantalla)

        if self.rectangulos_prog:
            for enemigo in self.lista_enemigos:
                for key in enemigo.lados:
                    pygame.draw.rect(self.pantalla, AZUL, enemigo.lados[key], 2)

            for piso in self.plataformas:
                for key in piso.lados:
                    pygame.draw.rect(self.pantalla, AZUL, piso.lados[key], 2)

            for key in self.player.lados:
                pygame.draw.rect(self.pantalla, AZUL, self.player.lados[key], 2)

            for enemigo in self.lista_enemigos:
                pygame.draw.rect(self.pantalla, AZUL, enemigo.rect_tiro, 2)
                

        self.pantalla.blit(self.Fuente.render(f"X{self.vidas}", 0, NEGRO), UBICACION_VIDA)
        self.pantalla.blit(self.Fuente.render(f"Puntos: {self.puntuacion}", 0, NEGRO), UBICACION_PUNTUACION)
        self.pantalla.blit(self.Fuente.render(f"Tiempo: {self.tiempo_actual}", 0, BLANCO), UBICACION_TIEMPO)

        for enemigo in self.lista_enemigos:
            enemigo.update(self.pantalla)

        for enemigo in self.lista_enemigos_cangrejos:
            enemigo.update(self.pantalla)

        self.player.update(self.pantalla)
        if self.bala_viva:
            self.laser.update(self.pantalla)

        if self.vida_bala_enemigo:
            self.bala_enemigo.update(self.pantalla)
        
        for trampa in self.trampas:
            trampa.update(self.pantalla)
        pygame.display.flip()

    def get_puntuacion(self):
        return super().get_puntuacion()
    
    def pausa(self):
        return super().pausa()
    
    def get_estado_juego(self):
        return super().get_estado_juego()
    
    def get_resultado(self):
        return super().get_resultado()
    
    def set_sonido_activado(self, activado):
        self.sonidos_activados = activado
    
    def configuracion_sonidos(self, volumen):
        if volumen:
            self.sonido_disparo.set_volume(self.sonido_disparo.get_volume() + 0.3)
            self.sonido_item.set_volume(self.sonido_item.get_volume() + 0.3)
            self.sonido_muerte.set_volume(self.sonido_muerte.get_volume() + 0.3)
            self.sonido_menos_vida.set_volume(self.sonido_menos_vida.get_volume() + 0.3)
        else:
            self.sonido_disparo.set_volume(self.sonido_disparo.get_volume() - 0.3)
            self.sonido_item.set_volume(self.sonido_item.get_volume() - 0.3)
            self.sonido_muerte.set_volume(self.sonido_muerte.get_volume() - 0.3)
            self.sonido_menos_vida.set_volume(self.sonido_menos_vida.get_volume() - 0.3)

    def set_cronometro(self, tiempo_pausa):
        return super().set_cronometro(tiempo_pausa)
    
    def disparos_collisiones(self):
        if self.vida_bala_enemigo:
            if self.bala_enemigo.rect.x < 0 or self.bala_enemigo.rect.x > ANCHO:
                self.vida_bala_enemigo = False
            if self.bala_enemigo.rect.colliderect(self.player.rect):
                self.vidas -= 1
                self.vida_bala_enemigo = False
        
        if self.bala_viva: 
            if len(self.lista_enemigos) != 0:
                for enemigo in self.lista_enemigos:
                    if enemigo.rect.colliderect(self.laser.rect):
                        self.sonido_muerte.play()
                        self.lista_enemigos.remove(enemigo)
                        self.objetos_collision_plataformas.remove(enemigo)
                        self.puntuacion += 300
                        self.contador_enemigos += 1
                        self.bala_viva = False
            
            if len(self.lista_enemigos_cangrejos) != 0:
                for enemigo in self.lista_enemigos_cangrejos:
                    if enemigo.rect.colliderect(self.laser.rect):
                        self.sonido_muerte.play()
                        self.lista_enemigos_cangrejos.remove(enemigo)
                        self.objetos_collision_plataformas.remove(enemigo)
                        self.puntuacion += 100
                        self.contador_enemigos += 1
                        self.bala_viva = False
        
            if self.laser.rect.x < 0 or self.laser.rect.x >= ANCHO:
                self.bala_viva = False

    def trampas_collisiones(self):
        for trampa in self.trampas:
            if trampa.toco == False and trampa.rect.colliderect(self.player.rect):
                self.sonido_muerte.play()
                trampa.toco = True
                self.vidas -= 1
            elif not trampa.rect.colliderect(self.player.rect):
                trampa.toco = False

    def actualizar_estado_juego(self):
        self.cronometro = pygame.time.get_ticks() // 1000
        if self.tiempo_actual > 1:
            self.tiempo_actual = self.tiempo_inicio - self.cronometro + self.tiempo_pausa
            self.fin_juego = False
        else:
            self.fin_juego = True

        if self.puntuacion > PUNTAJE_GANAR:
            self.gano = True
        else:
            self.gano = False

        if self.contador_enemigos > 7:
            self.puntuacion = self.puntuacion * self.tiempo_actual 
            self.gano = True
            self.fin_juego = True

        elif self.vidas < 1:
            self.fin_juego = True



