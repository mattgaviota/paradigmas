#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Importamos los módulos de Qt
from PyQt4 import QtCore, QtGui, uic, Qt

# Importamos la libreria de la ecuación
from ecuacion import Ecuacion_Cuadratica

# Importamos los modulos para graficar
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanva
from matplotlib.figure import Figure
import numpy as np


class Main(QtGui.QDialog):
    """La ventana principal de la aplicación."""
    def __init__(self):
        QtGui.QDialog.__init__(self)

        # Cargamos la interfaz desde el archivo .ui
        uifile = os.path.join(os.path.abspath(
            os.path.dirname(__file__)), 'interfaz.ui')
        uic.loadUi(uifile, self)

        self.validation()

    def validation(self):
        re = QtCore.QRegExp('^-?[0-9]+([,.]?[0-9]+)$')
        validator = QtGui.QRegExpValidator(re, None)
        self.a_edit.setValidator(validator)
        self.b_edit.setValidator(validator)
        self.c_edit.setValidator(validator)

    def get_vars(self):
        a = self.a_edit.text()
        b = self.b_edit.text()
        c = self.c_edit.text()
        return a, b, c

    @QtCore.pyqtSlot()
    def clean_all(self):
        self.raices_text.clear()
        self.a_edit.clear()
        self.b_edit.clear()
        self.c_edit.clear()
        self.a_edit.setFocus()

    @QtCore.pyqtSlot()
    def on_limpiar_clicked(self):
        self.clean_all()

    @QtCore.pyqtSlot()
    def on_raices_clicked(self):
        a, b, c = self.get_vars()

        if a:
            ecuacion = Ecuacion_Cuadratica(a, b, c)
            r1, r2 = ecuacion.resolver_ecuacion()
            raices = '(%s, %s)' % (r1, r2)
            self.raices_text.setText(raices)
        else:
            QtGui.QMessageBox.warning(self, u'Error',
            u'Debe ingresar el coeficiente cuadratico')
            self.a_edit.setFocus()

    @QtCore.pyqtSlot()
    def on_graficar_clicked(self):
        ##self.canva = MyMplCanvas()
        a, b, c = self.get_vars()
        ecuacion = Ecuacion_Cuadratica(a, b, c)
        ecuacion.graficar()
        ##a, b ,c = ecuacion.get_variables()
        ##h, k = ecuacion.vertice()
        ##self.canva.compute_initial_figure(a, b, c, h, k)


class MyStaticMplCanvas(FigureCanva):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanva.__init__(self, fig)

        FigureCanva.setSizePolicy(self, QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanva.updateGeometry(self)

    def compute_initial_figure(self, a, b, c, h, k):
        t = np.arange(-30.0, 30.0, 0.01)
        s = a * (t ** 2) + b * t + c

        #self.axes.annotate(u'vértice', xy=(h, k), xytext=(h+5, k),
        #        arrowprops=dict(facecolor='black', shrink=0.05),
        #            )

        self.axes.set_xlabel('X')
        self.axes.set_ylabel('Y')
        self.axes.set_ylim(-2,2)
        #self.axes.grid(True)
        #self.axes.show()
        self.axes.plot(t, s)





def main():
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
	main()
