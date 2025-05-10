## Librerias requeridas para la vista inicial
import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from views.UI import resources

##Definicion de la clase View_Inicial
class View_Inicial(QMainWindow):
    
    ## Constructor de la clase
    def __init__(self):        
        super().__init__()
        uic.loadUi(r"app\views\UI\View_Inicio.ui", self)
        
    def Run_Screen(self,app):
        Screen = View_Inicial()
        Screen.setWindowIcon(QIcon(r"app\views\UI\resources\cyber-criminal.png"))        
        Screen.show()
        sys.exit(app.exec())




    