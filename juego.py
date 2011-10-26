#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random


class Carta():

    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def get_palo(self):
        return self.palo

    def get_valor(self):
        return self.valor

    def __str__(self):
        return '%s de %s' % (self.valor, self.palo)

class Mazo():

    def __init__(self):
        self.baraja = self.genera_mazo()

    def genera_mazo(self):
        '''genera un mazo(una lista de objetos cartas) para 
        poder usarla durante el juego'''
        palos = ['Espada', 'Oro', 'Basto', 'Copa']
        valores = [v for v in range(1,8)] + [v for v in range(10,13)]
        return [Carta(palo, valor) for palo in palos for valor in valores]
	
    def reparte_cartas(self):
        '''Entrega cartas aleatoriamente a medida que se la piden
        y elimina el mazo la que se entrega'''
        while len(self.baraja) > 0:
            carta = random.choice(self.baraja)
            self.baraja.remove(carta)
            yield carta

    def genera_mano(self):
        '''genera una mano valida para jugar'''
        mano = []
        for i in range(3):
            mano.append(self.reparte_cartas().next())
        return mano

    def muestra_mazo(self):
        '''Muestra las cartas del mazo'''
        for carta in self.baraja:
            print carta


class Jugador():
    '''Clase jugador, tiene como atributo una mano y tiene todos
    los metodos que podría hacer un jugador'''
    def __init__(self):
        self.mano = []

    def obtener_mano(self, mano):
        '''obtiene una mano(3 cartas distintas)'''
        self.mano = mano

    def mostrar_mano(self):
        '''Muestra la mano que tiene el jugador'''
        for carta in self.mano:
            print carta

    def cantar_envido(self):
        '''Aca iría la parte en que canta envido, hay que implementarla'''
        #TODO
        pass


class Truco():
    '''Clase que tendría el juego en si, y la pseud inteligencia
    artificial de la computadora'''
    def __init__(self):
        '''Genera dos jugadores, uno humano que es el que se puede
        manejar y otro artificial que es el rival, y un mazo entero'''
        self.humano = Jugador()
        self.computadora = Jugador()
        self.mazo = Mazo()

    def repartir_cartas(self):
        '''Les reparte la mano a cada jugador'''
        mano1 = self.mazo.genera_mano()
        mano2 = self.mazo.genera_mano()
        self.humano.obtener_mano(mano1)
        self.computadora.obtener_mano(mano2)

    def empezar_juego(self):
        '''Acá va el juego en si. Faltan varias cosas. Por ahora solo
        muestra la mano del jugador humano'''
        self.repartir_cartas()
        self.humano.mostrar_mano()
        #TODO

def main():
    '''Acá va ir la parte principal'''
    truco = Truco()
    truco.empezar_juego()
    #TODO

if __name__ == '__main__':
    main()
