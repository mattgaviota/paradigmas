#!/usr/bin/env python
#-*- coding: utf-8 -*-

from ecuacion import Ecuacion_Cuadratica
import Tkinter as tk


class Main_app:

    def __init__(self, master):
        
        self.main_frame = tk.Frame(master, bg='#c8c8c8')
        self.main_frame.grid(ipadx=2, ipady=2, padx=2, pady=2)
        self.ecuacion = None
        self.a = tk.StringVar()
        self.b = tk.StringVar()
        self.c = tk.StringVar()
        self.raices = tk.StringVar()

        ######CAJAS DE ENTRADA CON SUS CARTELES######
        '''Etiqueta del X^2'''
        self.num_label = tk.Label(self.main_frame, text="X^2 + ", bg='#c8c8c8')
        self.num_label.grid(row=1, column=2, sticky=tk.W)
        
        '''Caja de entrada del número a'''
        self.ent_numero = tk.Entry(self.main_frame, width=5, 
            textvariable=self.a, bd=2, relief=tk.GROOVE)
        self.ent_numero.grid(row=1, column=1, sticky=tk.W + tk.E)
        self.ent_numero.focus_set()
        
        '''Etiqueta de X'''
        self.base_label = tk.Label(self.main_frame, text="X +", bg='#c8c8c8')
        self.base_label.grid(row=1, column=4, sticky=tk.W)
        
        '''Caja de entrada de b'''
        self.ent_base = tk.Entry(self.main_frame, width=5, 
            textvariable=self.b, bd=2, relief=tk.GROOVE)
        self.ent_base.grid(row=1, column=3, sticky=tk.W + tk.E)
        
        '''Caja de entrada de c'''
        self.ent_mantisa = tk.Entry(self.main_frame, width=5, 
            textvariable=self.c, bd=2, relief=tk.GROOVE)
        self.ent_mantisa.grid(row=1, column=5, sticky=tk.W + tk.E)
        
        ###############ETIQUETAS CON LOS RESULTADOS################
        '''Etiqueta de las raices'''
        self.raices_label = tk.Label(self.main_frame, text='Raices',
            bg='#c8c8c8')
        self.raices_label.grid(row=2, column=1, sticky=tk.W)
        
        self.vertice_label = tk.Label(self.main_frame,
            textvariable=self.raices,bg='#c8c8c8')
        self.vertice_label.grid(row=3, column=1)

        ###########BOTONES############
        '''Boton para graficar'''
        self.btn_graficar = tk.Button(self.main_frame, text="Graficar",
            command=self.graficar, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_graficar.grid(row=4, column=1)

        '''Boton para limpiar los resultados'''
        self.btn_limpiar = tk.Button(self.main_frame, text="Limpiar",
            command=self.clean, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_limpiar.grid(row=5, column=3, sticky=tk.E + tk.W)
        
        '''Boton para mostrar las raices'''
        self.btn_raices = tk.Button(self.main_frame, text="Acerca de",
            command=self.raices, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_raices.grid(row=5, column=4, sticky=tk.E + tk.W)
        
    def clean(self):
        '''
        Función para limpiar todos los campos
        '''
        self.a.set('')
        self.b.set('')
        self.c.set('')
        self.a.focus_set()

    def graficar(self):
        '''Función para graficar'''
        a = self.a.get()
        b = self.b.get()
        c = self.c.get()
        self.ecuacion = Ecuacion_Cuadratica(a, b, c)
        self.ecuacion.graficar()
    
    def raices(self):
        pass


def main():
    
    root = tk.Tk()
    root.title("Ecuación Cuadratica")
    app = Main_app(root)
    root.mainloop()
    return 0

if __name__ == '__main__':
	main()
