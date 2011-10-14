#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Importo os para usar el metodo system('clear') para limpiar la pantalla
import os
# Importo la funcion sqrt(raiz) y fabs(valor absoluto)
from math import sqrt, fabs
import matplotlib.pyplot as plt
import numpy as np


class Ecuacion_Cuadratica():

    def __init__(self, a, b, c):
        '''Constructor de la clase, convierte los atributos
        ya que se ingresan como cadenas'''
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__raices = None

    def get_variables(self):
        a = self.__a
        b = self.__b
        c = self.__c
        return a, b, c

    def solve(self, band=0):
        '''Se encarga de resolver la ecuación de acuerdo a la formula
        para resolver las ecuaciones cuadráticas. Devuelve las raices
        de acuerdo al tipo de raiz'''
        a, b, c = self.__a, self.__b, self.__c
        if not band:
            raiz1 = (-1 * b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
            raiz2 = (-1 * b - sqrt((b ** 2) - (4 * a * c))) / (2 * a)
            return raiz1, raiz2
        elif band == 1:
            raiz1 = (-1 * b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
            return raiz1, 'd'
        else:
            discriminante = sqrt(fabs((b ** 2) - (4 * a * c)))
            raiz1 = '(-%s + %s i) / 2*%s' % (b, discriminante, a)
            raiz2 = '(-%s - %s i) / 2*%s' % (b, discriminante, a)
            return raiz1, raiz2

    def determinar_raiz(self):
        '''Determina el caracter de las raices, ya sean reales y distintas,
        reales e iguales o complejas y conjugadas'''
        a, b, c = self.__a, self.__b, self.__c
        discriminante = (b ** 2) - 4 * a * c
        if discriminante > 0:
            return 1 # raices reales y distintas
        elif discriminante == 0:
            return 2 # raices reales e iguales
        else:
            return 3 # raices complejas y conjugadas

    def resolver_ecuacion(self):
        '''Se encarga de determinar el tipo de raiz y entregar el resultado
        acorde al tipo de raices'''
        dis = self.determinar_raiz()
        if dis == 1:
            self.__raices = self.solve() # raices reales y distintas
        if dis == 2:
            self.__raices = self.solve(1) # raices reales e iguales
        if dis == 3:
            self.__raices = self.solve(2) # raices complejas y conjugadas
        return self.__raices

    def vertice(self):
        '''Calcula vértice de la ecuación'''
        a, b, c = self.__a, self.__b, self.__c
        h = (-1 * b) / (2 * a)
        k = ((4 * a * c) - (b ** 2)) / (4 * a)
        return h, k

    def mostrar_vertice(self):
        '''Muestra vértice de la ecuación'''
        h, k = self.vertice()
        print 'Vertice: '
        print
        print '(%s,%s)' % (h, k)

    def ecuacion_factorizada(self):
        '''Muestra la ecuación factorizada de acuerdo a sus raices'''
        self.resolver_ecuacion()
        r1, r2 = self.__raices
        if r2 == 'd':
            if r1 >= 0:
                return '(X - %s)^2' % r1,
            else:
                return '(X + %s)^2' % r1,
        else:
            if r1 >= 0 and r2 >= 0:
                return '(X - %s) * (X - %s)' % (r1, r2)
            elif r1 >= 0 and r2 <= 0:
                return '(X - %s) * (X + %s)' % (r1, -1 * r2)
            elif r1 <= 0 and r2 <= 0:
                return '(X + %s) * (X + %s)' % (-1 * r1, -1 * r2)
            elif r1 <= 0 and r2 >= 0:
                return '(X + %s) * (X - %s)' % (-1 * r1, r2)

    def mostrar_raices(self):
        '''Muestra las raices de la ecuación'''
        self.resolver_ecuacion()
        print 'raices: '
        print
        print self.__raices
    
    def graficar(self):
        a, b, c = self.__a, self.__b, self.__c
        h, k = self.vertice()
        ax = plt.subplot(111)

        t = np.arange(h - 20, k + 20.0, 0.01)
        s = a * (t ** 2) + b * t + c
        line, = plt.plot(t, s, lw=2)
        
        plt.annotate(u'vértice', xy=(h, k), xytext=(h+5, k),
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    )
        
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.ylim(-2,2)
        plt.grid(True)
        plt.show()


def main():
    a = raw_input('ingrese a: ')
    b = raw_input('ingrese b: ')
    c = raw_input('ingrese c: ')
    os.system('clear')
    ec = Ecuacion_Cuadratica(a, b, c)
    ec.mostrar_raices()
    print 'factorizacion : '
    print ec.ecuacion_factorizada()
    ec.mostrar_vertice()
    ec.graficar()


if __name__ == '__main__':
    main()
