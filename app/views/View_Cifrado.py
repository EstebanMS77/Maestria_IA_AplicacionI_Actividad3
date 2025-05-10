## Librerias requeridas para la vista Cifrado
import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon


##Definicion de la clase View_Cifrado
class View_Cifrado(QMainWindow):

    ## Propiedades de la clase
    PathFile_ViewCifrado = r"app\views\UI\View_Cifrado.ui"
    PathFile_ViewIcon = r"app\views\UI\resources\cyber-criminal.png"
    
    ## Constructor de la clase
    def __init__(self):
        
        super().__init__()
        uic.loadUi(self.PathFile_ViewCifrado, self)
        self.setWindowIcon(QIcon(self.PathFile_ViewIcon))    
