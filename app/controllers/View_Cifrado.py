## Librerias requeridas para la vista Cifrado
import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon


##Definicion de la clase View_Cifrado
class View_Cifrado(QMainWindow):

    
    ## Constructor de la clase
    def __init__(self):
        
        super().__init__()
        uic.loadUi(r"app\views\UI\View_Cifrado.ui", self)
        

    def Run_Screen(self,app):
        Screen = View_Cifrado()
        Screen.setWindowIcon(QIcon(r"app\views\UI\resources\cyber-criminal.png"))
        Screen.show()
        sys.exit(app.exec())
