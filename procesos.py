#!/usr/bin/env python
#-*- coding: utf-8 -*-

from random import randint
from multiprocessing import Process
import time

class Hilo(Process):

    def __init__(self, lista=[], status=0):
        Process.__init__(self)
        self.lista = lista
        self.status = status

    def run(self):
        self.status = sum(self.lista)


def genera_lista(num):
    lista = []
    for x in xrange(num):
        r = randint(0, 5000)
        if r % 2 != 0:
            lista.append(float(r))
        else:
            lista.append(r)
        #print '.',
    return lista


def divide_lista(lista, divisor):
    otro = len(lista)/divisor
    for i in xrange(divisor):
        yield lista[otro*i:otro*(i+1)]

def main():
    longitud = raw_input('Ingrese la cantidad de elementos de la lista : ')
    cantidad_de_hilos = raw_input('Ingrese la cantidad de hilos a ejecutar : ')
    print "Generando lista de números aleatorios....."
    lista = genera_lista(int(longitud))
    divisiones = [y for y in divide_lista(lista, int(cantidad_de_hilos))]
    print 'Iniciando suma de la lista de %s elementos' % (len(lista), )
    s = time.time()
    hilos = []
    for listas in divisiones:
         hilo = Hilo(listas)
         hilo.start()
         hilos.append(hilo)
    suma = 0
    for hilo in hilos:
        #hilo.start()
        #hilo.join()
        print hilo.status
        suma += hilo.status
        hilo.join()
    print 'Suma con threads: '
    print suma
    print 'Tiempo total = %f' % (time.time() - s)
    print 'Suma sin threads: '
    t = time.time()
    print sum(lista)
    print 'Tiempo total = %f' % (time.time() - t)

if __name__ == '__main__':
    main()
