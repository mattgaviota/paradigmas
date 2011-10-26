#/usr/bin/env python
#-*- coding: utf-8 -*-

class Persona():
    
    def __init__(self, nombre='', mama=None, papa=None):
        ''' Inicializa los atributos'''
        self.__mama = mama
        self.__papa = papa
        self.__nombre = nombre
    
    def get_nombre(self):
        '''devuelve el nombre'''
        return self.__nombre

    def get_mama(self):
        '''devuelve la madre'''
        return self.__mama

    def get_papa(self):
        '''devuelve el padre'''
        return self.__papa

    def validar(self, objeto):
        '''Devuelve verdadero si el objeto pasado como parametro es 
        distinto de nulo, en otro caso devuelve falso'''
        if objeto != None:
            return True
        else:
            return False

    def es_hijo(self, padre):
        '''Retorna un valor booleano de acuerdo a si el parametro es padre
        del objeto. True si es padre, False si no lo es'''
        if padre != self and padre != None:
            if self.get_papa() == padre: 
                return self.validar(self.get_papa())
            elif self.get_mama() == padre:
                return self.validar(self.get_mama())
            else:
                return False
        else:
            return False

    def es_padre(self, hijo):
        '''Retorna un valor booleano de acuerdo a si el parametro es hijo
        del objeto. True si es hijo, False si no lo es'''
        if hijo != self and hijo != None:
            if hijo.es_hijo(self):
                return True
            else:
                return False
        else:
            return False

    def es_hermano(self, hermano):
        '''Retorna un valor booleano de acuerdo a si el parametro es hermano
        del objeto. True si es hermano, False si no lo es'''
        if hermano != self and hermano != None:
            if hermano.get_papa() == self.get_papa():
                return self.validar(self.get_papa())
            elif hermano.get_mama() == self.get_mama():
                return self.validar(self.get_mama())
            else:
                return False
        else:
            return False
            
    def es_tio(self, sobrino):
        '''Retorna un valor booleano de acuerdo a si el parametro es sobrino
        del objeto. True si es sobrino, False si no lo es'''
        if  sobrino!= self and sobrino != None:
            if self.es_hermano(sobrino.get_papa()) or (
                self.es_hermano(sobrino.get_mama())):
                    return True
            else:
                return False
        else:
            return False

    def es_sobrino(self, tio):
        '''Retorna un valor booleano de acuerdo a si el parametro es tio
        del objeto. True si es tio, False si no lo es'''
        if tio != self and tio != None:
            if tio.es_tio(self):
                return True
            else:
                return False
        else:
            return False

    def es_primo(self, primo):
        '''Retorna un valor booleano de acuerdo a si el parametro es primo
        del objeto. True si es primo, False si no lo es'''
        if primo != self and primo != None:
            if self.get_papa().es_hermano(primo.get_papa()):
                return True
            elif self.get_papa().es_hermano(primo.get_mama()):
                return True
            elif self.get_mama().es_hermano(primo.get_papa()):
                return True
            elif self.get_mama().es_hermano(primo.get_mama()):
                return True
            else:
                return False
        else:
            return False

    def es_nieto(self, abuelo):
        '''Retorna un valor booleano de acuerdo a si el parametro es abuelo
        del objeto. True si es abuelo, False si no lo es'''
        if abuelo != self and abuelo != None:
            if self.get_papa() != None: 
                if self.get_papa().es_hijo(abuelo):
                    return True
            elif self.get_mama() != None:
                if self.get_mama().es_hijo(abuelo):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def es_abuelo(self, nieto):
        '''Retorna un valor booleano de acuerdo a si el parametro es nieto
        del objeto. True si es nieto, False si no lo es'''
        if nieto != self and nieto != None:
            if nieto.es_nieto(self):
                return True
            else:
                return False
        else:
            return False

    def es_bisabuelo(self, bisnieto):
        '''Retorna un valor booleano de acuerdo a si el parametro es bisnieto
        del objeto. True si es bisnieto, False si no lo es'''
        if bisnieto != self and bisnieto != None:
            if bisnieto.get_papa() != None:
                if bisnieto.get_papa().es_nieto(self):
                    return True
            elif bisnieto.get_mama() != None:
                if bisnieto.get_mama().es_nieto(self):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def es_bisnieto(self, bisabuelo):
        '''Retorna un valor booleano de acuerdo a si el parametro es bisabuelo
        del objeto. True si es bisabuelo, False si no lo es'''
        if bisabuelo != self and bisabuelo != None:
            if bisabuelo.es_bisabuelo(self):
                return True
            else:
                return False
        else:
            return False


def main():
    susana = Persona('Susana')
    fernando = Persona('fernando')
    eliana = Persona('Eliana')
    matias = Persona('Matias', susana, fernando)
    pedro = Persona('Pedro', susana)
    juan = Persona('Juan', eliana, pedro)
    diego = Persona('Diego', None, matias)
    if matias.es_hermano(pedro):
        print '%s es hermano de %s' % (matias.get_nombre(), pedro.get_nombre())
    else:
        print '%s no es hermano de %s' % (matias.get_nombre(), pedro.get_nombre())
    
    if matias.es_tio(juan):
        print '%s es tio de %s' % (matias.get_nombre(), juan.get_nombre())
    else:
        print '%s no es tio de %s' % (matias.get_nombre(), juan.get_nombre())

    if diego.es_nieto(fernando):
        print '%s es nieto de %s' % (diego.get_nombre(), fernando.get_nombre())
    else:
        print '%s no es nieto de %s' % (diego.get_nombre(), fernando.get_nombre())
    if susana.es_abuelo(juan):
        print '%s es abuelo de %s' % (susana.get_nombre(), juan.get_nombre())
    else:
        print '%s no es abuelo de %s' % (susana.get_nombre(), juan.get_nombre())


if __name__ == '__main__':
    main()
