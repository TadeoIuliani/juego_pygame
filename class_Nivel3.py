import pygame, sys
from class_Personaje import Personaje
from class_enemigo import *
from class_item import *
from class_Piso import *
from class_Nivel2 import Nivel_2
from config import *
from imagenes import *
from Class_Proyectiles import Laser

class Nivel3(Nivel_2):
    def __init__(self, fondo_path, plataformas, cajas, puntuacion) -> None:
        super().__init__(fondo_path, plataformas, cajas, puntuacion)
        self.boss = Boss(TAM_BOSS, COOR_BOSS, r"boss_sprites\sprites_boss_1-removebg-preview.png", 2, imagenes_boss)
        self.objetos_collision_plataformas.append(self.boss)
        self.generador_enemigos = GenearadorEnemigos_2(r"sprites_toki\saltando.png", (80, 50), 5, imagenes_toki, None)
        self.lista_enemigos = self.generador_enemigos.generar_enemigos(Enemigo_2, 3)
        self.objetos_collision_plataformas = agregar_lista_a_lista(self.objetos_collision_plataformas, self.lista_enemigos)
        self.trampa = Trampa(r"trampa\Off.png", (30, 30), (300, 110), True, trampa)
        self.trampa_2 = Trampa(r"trampa\Off.png", (30, 30), (340, 310), True, trampa)
        self.trampas = [self.trampa, self.trampa_2]
        self.contador_oleadas = 1
        self.bombas = []

    def play(self, lista_eventos):
        self.reloj.tick(30)
        if self.bandera == False:
            self.cronometro.encender()
            self.bandera = True
        self.leer_inputs(lista_eventos)
        self.collisiones()
        self.disparos_collisiones()
        self.trampas_collisiones()
        self.actualizar_estado_juego()
        self.actualizar_pantalla()  

    def collisiones(self):
        collision_objeto_plataforma(self.objetos_collision_plataformas, self.plataformas)

        if len(self.bombas) != 0:
            for bomba in self.bombas:
                if bomba.rect.colliderect(self.player.rect):
                    bomba.esta_cayendo = False
                    bomba.estado = "explosion"
                    self.vidas -= 1
                if bomba.get_explosion() == True:
                    self.bombas.remove(bomba)
                    self.objetos_collision_plataformas.remove(bomba)

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
            self.lista_frutas = crear_objetos_random(Item, imagenes_fruta, r"frutitas\0.png", TAM_ITEM, 5)

        if len(self.lista_enemigos) != 0:
            self.boss.estado = "quieto"
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
                        self.bala_enemigo = Laser(r"sprites_toki\fuego_izquierda.png", enemigo.rect.midleft,10 , False)
                        self.vida_bala_enemigo = True
                    elif self.vida_bala_enemigo == False:
                        enemigo.estado = "atacar_derecha"
                        self.bala_enemigo = Laser(r"sprites_toki\fuego_derecha.png", enemigo.rect.midleft,10 , True)
                        self.vida_bala_enemigo = True
                else:
                    if enemigo.estado == "atacar_derecha":
                        enemigo.estado = "izquierda"
                    elif enemigo.estado == "atacar_izquierda":
                        enemigo.estado = "derecha"
        elif self.contador_oleadas < 4:
            self.bombas = crear_objetos_random(Bomba, imagenes_bomba, r"klipartz.com.png", (80, 100), 3)
            self.objetos_collision_plataformas = agregar_lista_a_lista(self.objetos_collision_plataformas, self.bombas)
            self.boss.estado = "atacar"

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

            pygame.draw.line(self.pantalla, AZUL, self.enemigo_dispara.rect.topleft, (0, self.enemigo_dispara.rect.y))
            pygame.draw.line(self.pantalla, AZUL, self.enemigo_dispara.rect.topright, (ANCHO, self.enemigo_dispara.rect.y))
            for enemigo in self.lista_enemigos:
                pygame.draw.rect(self.pantalla, AMARILLO, enemigo.rect_tiro, 2)
            
            for key in self.trampa.lados:
                    pygame.draw.rect(self.pantalla, ROJO, self.trampa.lados[key], 2)
            for key in self.trampa_2.lados:
                    pygame.draw.rect(self.pantalla, ROJO, self.trampa_2.lados[key], 2)

        self.pantalla.blit(self.Fuente.render(f"X{self.vidas}", 0, NEGRO), UBICACION_VIDA)
        self.pantalla.blit(self.Fuente.render(f"Puntos: {self.puntuacion}", 0, NEGRO), UBICACION_PUNTUACION)
        self.pantalla.blit(self.Fuente.render(f"Tiempo: {int(self.cronometro.mostrar_tiempo())}", 0, BLANCO), UBICACION_TIEMPO)

        for enemigo in self.lista_enemigos:
            enemigo.update(self.pantalla)

        if len(self.bombas) != 0:
            for bomba in self.bombas:
                bomba.update(self.pantalla)

        self.boss.update(self.pantalla) 
        self.player.update(self.pantalla)
        if self.bala_viva:
            self.laser.update(self.pantalla)

        if self.vida_bala_enemigo:
            self.bala_enemigo.update(self.pantalla)
        
        for trampa in self.trampas:
            trampa.update(self.pantalla)
        
        pygame.display.flip()

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
                        self.laser = Laser("disparo.png", self.player.rect.midright,20 ,False)
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

    def disparos_collisiones(self):
        if self.vida_bala_enemigo:
            if self.bala_enemigo.rect.x < 0 or self.bala_enemigo.rect.x > ANCHO:
                self.vida_bala_enemigo = False
            elif self.bala_enemigo.rect.colliderect(self.player.rect):
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
                        self.bala_viva = False
        
            if self.laser.rect.x < 0 or self.laser.rect.x >= ANCHO:
                self.bala_viva = False

    def actualizar_estado_juego(self):
        if self.boss.get_atacar() == True:
            self.lista_enemigos = self.generador_enemigos.generar_enemigos(Enemigo_2, 3)
            self.objetos_collision_plataformas = agregar_lista_a_lista(self.objetos_collision_plataformas, self.lista_enemigos)
            self.contador_oleadas += 1

        self.cronometro.actualizar()
        if self.cronometro.termino():
            self.fin_juego = True
        else:
            self.fin_juego = False

        if self.puntuacion > PUNTAJE_GANAR_3:
            self.gano = True
        else:
            self.gano = False

        if self.vidas < 1:
            self.fin_juego = True
            self.gano = False
