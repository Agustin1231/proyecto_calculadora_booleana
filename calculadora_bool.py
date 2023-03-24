from PySide6.QtWidgets import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property
import random 

class juego(QMainWindow):
    
    def setup(self):
        # Fondo
        self.set_fixed_size (500,400)
        self.style_sheet = "background: #1A141E"

        # Contenedor tablas
        self.fr_tabla = QFrame(self)
        self.fr_tabla.geometry = QRect(10,40,480,350)
        self.fr_tabla.style_sheet = "background: white;"

        # Contenedor variable p
        self.p = QFrame(self.fr_tabla)
        self.p.geometry = QRect(10,10,50,330)
        self.p.style_sheet = "background: pink;"

        # Contenedor variable q
        self.q = QFrame(self.fr_tabla)
        self.q.geometry = QRect(70,10,50,330)
        self.q.style_sheet = "background: pink;"

        # Contenedor variable r
        self.r = QFrame(self.fr_tabla)
        self.r.geometry = QRect(130,10,50,330)
        self.r.style_sheet = "background: pink;"

        # Contenedor variable q1
        self.q1 = QFrame(self.fr_tabla)
        self.q1.geometry = QRect(190,10,85,330)
        self.q1.style_sheet = "background: pink;"

        # Contenedor variable q2
        self.q2 = QFrame(self.fr_tabla)
        self.q2.geometry = QRect(285,10,85,330)
        self.q2.style_sheet = "background: pink;"

        # Contenedor variable q3
        self.q3 = QFrame(self.fr_tabla)
        self.q3.geometry = QRect(385,10,85,330)
        self.q3.style_sheet = "background: pink;"



import sys

app = QApplication(sys.argv)
window = juego()
window.setup()
window.show()
sys.exit(app.exec())   