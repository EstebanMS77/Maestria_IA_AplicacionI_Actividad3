## Librerias requeridas para la vista Cifrado
import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import pyqtSignal 


##Definicion de la clase View_Cifrado
class View_Descifrado(QMainWindow):

    ## Propiedades de la clase
    PathFile_View_Descifrado = r"app\views\UI\View_Decepcriptar.ui"
    PathFile_ViewIcon = r"app\views\UI\resources\cyber-criminal.png"
    Sig_Btn_Clicked_Inicio = pyqtSignal() 
    Sig_TextInputText_Codigo = pyqtSignal()

    ## Constructor de la clase
    def __init__(self):
        
        super().__init__()
        uic.loadUi(self.PathFile_View_Descifrado, self)
        self.setWindowIcon(QIcon(self.PathFile_ViewIcon))   

        self.Btn_Inicio = self.findChild(QPushButton, "Button_Inicio")    
        self.InputText_Codigo = self.findChild(QLineEdit, "InputText_Codigo")
        self.lcdNumber_Cifrado = self.findChild(QLCDNumber, "lcdNumber_Cifrado")


        self.Btn_Inicio.clicked.connect(self._Enviar_Btn_Inicio)
        self.InputText_Codigo.textChanged.connect(self._Enviar_TextChange_Codigo)   

    def _Enviar_Btn_Inicio(self):
        self.Sig_Btn_Clicked_Inicio.emit()

    def _Enviar_TextChange_Codigo(self):
        self.Sig_TextInputText_Codigo.emit()

    def _Recibir_descifrado(self, Str_Cifrado):
        self.lcdNumber_Cifrado.display(Str_Cifrado)
        
    def Eliminar_Texto(self):
        self.InputText_Codigo.clear()
        self.lcdNumber_Cifrado.display(0)
