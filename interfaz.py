#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re

from ecuacion import Ecuacion_Cuadratica

import Tkinter as tk
from tkMessageBox import showinfo, showerror


class Main_app:

    def __init__(self, master):
        
        self.main_frame = tk.Frame(master, bg='#c8c8c8')
        self.main_frame.grid(ipadx=2, ipady=2, padx=2, pady=2)
        self.ecuacion = None
        self.a = tk.StringVar()
        self.b = tk.StringVar()
        self.c = tk.StringVar()
        self.raices = tk.StringVar()
        self.vertice = tk.StringVar()
        self.factorizacion = tk.StringVar()
        self.reg = r'^(-?[0-9]*)([,.]?[0-9]+)$'

        ######CAJAS DE ENTRADA CON SUS CARTELES######
        '''Etiqueta del X^2'''
        self.num_label = tk.Label(self.main_frame, text="X^2 + ", bg='#c8c8c8')
        self.num_label.grid(row=1, column=2, sticky=tk.W + tk.E)
        
        '''Caja de entrada del número a'''
        self.ent_a = tk.Entry(self.main_frame, width=4, 
            textvariable=self.a, bd=2, relief=tk.GROOVE)
        self.ent_a.grid(row=1, column=1, sticky=tk.W + tk.E)
        self.ent_a.focus_set()
        
        '''Etiqueta de X'''
        self.base_label = tk.Label(self.main_frame, text="X +", bg='#c8c8c8')
        self.base_label.grid(row=1, column=4, sticky=tk.W + tk.E)
        
        '''Caja de entrada de b'''
        self.ent_b = tk.Entry(self.main_frame, width=4, 
            textvariable=self.b, bd=2, relief=tk.GROOVE)
        self.ent_b.grid(row=1, column=3, sticky=tk.W + tk.E)
        
        '''Caja de entrada de c'''
        self.ent_c = tk.Entry(self.main_frame, width=4, 
            textvariable=self.c, bd=2, relief=tk.GROOVE)
        self.ent_c.grid(row=1, column=5, sticky=tk.W + tk.E)
        
        ###############ETIQUETAS CON LOS RESULTADOS################
        '''Etiqueta de las raices'''
        self.raices_label = tk.Label(self.main_frame, text='Raices :',
            bg='#c8c8c8')
        self.raices_label.grid(row=3, column=1, sticky=tk.W)
        
        self.raices_entry = tk.Entry(self.main_frame,
            textvariable=self.raices,bg='#c8c8c8', state='readonly')
        self.raices_entry.grid(row=4, column=1, columnspan=2)

        '''Etiqueta del vertice'''
        self.vertice_label = tk.Label(self.main_frame, text='Vertice :',
            bg='#c8c8c8')
        self.vertice_label.grid(row=3, column=3, sticky=tk.W)
        
        self.vertice_entry = tk.Entry(self.main_frame,
            textvariable=self.vertice,bg='#c8c8c8', state='readonly')
        self.vertice_entry.grid(row=4, column=4, columnspan=2)

        '''Etiqueta de la factorizacion'''
        self.factorizacion_label = tk.Label(self.main_frame,
            text='Factorizacion :', bg='#c8c8c8')
        self.factorizacion_label.grid(row=5, column=1, sticky=tk.W)
        
        self.factorizacion_entry = tk.Entry(self.main_frame,
            textvariable=self.factorizacion, bg='#c8c8c8', state='readonly')
        self.factorizacion_entry.grid(row=5, column=2, columnspan=2)

        ###########BOTONES############
        '''Boton para graficar'''
        self.btn_graficar = tk.Button(self.main_frame, text="Graficar",
            command=self.graficar, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_graficar.grid(row=2, column=2)

        '''Boton para limpiar los resultados'''
        self.btn_limpiar = tk.Button(self.main_frame, text="Limpiar",
            command=self.clean, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_limpiar.grid(row=2, column=3, sticky=tk.E + tk.W)
        
        '''Boton para hacer los calculos'''
        self.btn_raices = tk.Button(self.main_frame, text="Calcular",
            command=self.calcular, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_raices.grid(row=2, column=1, sticky=tk.E + tk.W)

        '''Boton para salir'''
        self.btn_raices = tk.Button(self.main_frame, text="Salir",
            command=quit, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_raices.grid(row=2, column=4, columnspan=2, sticky=tk.E + tk.W)
        
    def clean(self):
        '''
        Función para limpiar todos los campos
        '''
        self.a.set('')
        self.b.set('')
        self.c.set('')
        self.raices.set('')
        self.vertice.set('')
        self.factorizacion.set('')
        self.ent_a.focus_set()

    def graficar(self):
        '''Función para graficar'''
        a = self.a.get()
        b = self.b.get()
        c = self.c.get()
        self.ecuacion = Ecuacion_Cuadratica(a, b, c)
        self.ecuacion.graficar()

    def analizar_entrada(self, a, b, c):
        re_a = re.match(self.reg, a)
        re_b = re.match(self.reg, b)
        re_c = re.match(self.reg, c)
        if re_a and re_b and re_c:
            return True
        else:
            return False

    def calcular(self):
        a = self.a.get()
        b = self.b.get()
        c = self.c.get()
        if self.analizar_entrada(a, b, c):
            self.ecuacion = Ecuacion_Cuadratica(a, b, c)
            self.raices.set(self.ecuacion.resolver_ecuacion())
            self.vertice.set(self.ecuacion.vertice())
            self.factorizacion.set(self.ecuacion.ecuacion_factorizada())
        else:
            mensaje = 'Algún valor está mal escrito, solo pueden ser números'
            showerror(title='Error', message=mensaje)


def main():
    
    root = tk.Tk()
    root.title("Ecuación Cuadratica")
    app = Main_app(root)
    root.mainloop()
    return 0

if __name__ == '__main__':
	main()
