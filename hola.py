#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
from tkMessageBox import showinfo

class Main_app():
    def __init__(self, master):
        self.main_frame = tk.Frame(master, bg='#c8c8c8')
        self.main_frame.grid(ipadx=2, ipady=2, padx=2, pady=2)
        
        '''Boton para saludar'''
        self.btn_saludar = tk.Button(self.main_frame, text="Saludar",
            command=self.saludar, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_saludar.grid(row=1, column=1, columnspan=2,
        rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S)

    def saludar(self):
        showinfo(title='Saludo', message='hola mundo')

def main():
    
    root = tk.Tk()
    root.title("Ecuación Cuadratica")
    app = Main_app(root)
    root.mainloop()
    return 0

if __name__ == '__main__':
	main()
