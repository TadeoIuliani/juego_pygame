import pygame
from class_Personaje import Personaje
from class_item import Item
from Class_Proyectiles import *


class Player(Personaje):
    def __init__(self, tamaño, coor, imagen, velocidad: int, animaciones: dict, vidas: int) -> None:
        super().__init__(tamaño, coor, imagen, velocidad, animaciones)
        self.vidas = vidas

    # def sumar_bala(self, cantidad: int):
    #     self.proyectil.agregar_municiones(cantidad)

    # def lanzar(self, velocidad):
    #     if self.estado == "derecha":
    #         self.proyectil.mover(False, True, velocidad)

    #     elif self.estado == "izquierda":
    #         self.proyectil.mover(True, False, velocidad)

    #     self.proyectil.eliminar_municiones()

    def restar_vida(self):
        self.vidas -= 1
