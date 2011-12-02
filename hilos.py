#!/usr/bin/env python
#-*- coding: utf-8 -*-

from random import randint
from threading import Thread
import time
import os


def sumalista(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma


class Hilo(Thread):

    def __init__(self, lista):
        Thread.__init__(self)
        self.lista = lista
        self.suma = 0

    def run(self):
        self.status = sumalista(self.lista)


def genera_lista(num):
    lista = []
    diez = num / 10.0
    for x in xrange(num):
        r = randint(0, 5000)
        if r % 2 != 0:
            lista.append(float(r))
        else:
            lista.append(r)
        if x % diez == 0:
            porcentaje = x * 100 / num
            print porcentaje, '%'
        elif x == num - 1:
            print '100 %'
    return lista


def divide_lista(lista, divisor):
    otro = len(lista) / divisor
    for i in xrange(divisor):
        yield lista[otro * i:otro * (i + 1)]


def main():
    longitud = raw_input('Ingrese la cantidad de elementos de la lista : ')
    num_de_hilos = raw_input('Ingrese la cantidad de hilos a ejecutar : ')
    print "Generando lista de números aleatorios....."
    lista = genera_lista(int(longitud))
    divisiones = [y for y in divide_lista(lista, int(num_de_hilos))]
    print 'Iniciando suma de la lista de %s elementos' % (len(lista), )
    s = time.time()
    hilos = []
    for listas in divisiones:
        hilo = Hilo(listas)
        hilo.start()
        hilos.append(hilo)
    suma = 0
    for hilo in hilos:
        hilo.join()
        suma += hilo.status
    print 'Suma con %s threads: ' % (num_de_hilos, )
    print suma
    print 'Tiempo total = %f segundos' % (time.time() - s)
    print 'Suma sin threads: '
    t = time.time()
    print sumalista(lista)
    print 'Tiempo total = %f segundos' % (time.time() - t)

if __name__ == '__main__':
    main()
