## Librerias requeridas para la vista inicial
import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from views.UI import resources
from PyQt6.QtCore import pyqtSignal

##Definicion de la clase View_Inicial
class View_Warning(QMainWindow):
    
#   #Propiedades de la clase
    PathFile_ViewWarning = r"app\views\UI\View_Warning.ui"
    PathFile_ViewIcon = r"app\views\UI\resources\cyber-criminal.png"
    Sig_Btn_Clicked_Inicio = pyqtSignal() 
    ## Constructor de la clase
    def __init__(self):  

        super().__init__()
        uic.loadUi(self.PathFile_ViewWarning, self)
        self.setWindowIcon(QIcon(self.PathFile_ViewIcon))
        self.Label_Error = self.findChild(QLabel,"Label_Error")

        self.Btn_Inicio = self.findChild(QPushButton, "Button_Inicio") 
        self.Btn_Inicio.clicked.connect(self._Enviar_Btn_Inicio)


    def Write_Error(self,Str_Error):      
        
        self.Label_Error.setText(Str_Error)

    def _Enviar_Btn_Inicio(self):
        self.Sig_Btn_Clicked_Inicio.emit()

        
