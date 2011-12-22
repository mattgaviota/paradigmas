#!/usr/bin/env python
#-*- coding: utf-8 -*-

#imports

from random import randint
from multiprocessing import Process, Queue
import time


def sumalista(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma


class Hilo(Process):

    def __init__(self, lista=[], cola=None):
        Process.__init__(self)
        self.lista = lista
        self.cola = cola

    def run(self):
        self.cola.put(sumalista(self.lista))


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
    num_de_procesos = raw_input('Ingrese el número de procesos a correr : ')
    print "Generando lista de números aleatorios....."
    lista = genera_lista(int(longitud))
    divisiones = [y for y in divide_lista(lista, int(num_de_procesos))]
    print 'Iniciando suma de la lista de %s elementos' % (len(lista), )
    cola = Queue()
    s = time.time()
    hilos = []
    for listas in divisiones:
        hilo = Hilo(listas, cola)
        hilo.start()
        hilos.append(hilo)
    suma = 0
    for hilo in hilos:
        suma += hilo.cola.get()
        hilo.join()
    print 'Suma con %s Procesos : ' % (num_de_procesos)
    print suma
    print 'Tiempo total = %f segundos' % (time.time() - s)
    print 'Suma sin procesos: '
    t = time.time()
    print sumalista(lista)
    print 'Tiempo total = %f segundos' % (time.time() - t)

if __name__ == '__main__':
    main()
