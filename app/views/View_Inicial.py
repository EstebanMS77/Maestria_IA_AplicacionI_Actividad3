## Librerias requeridas para la vista inicial
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


##Definicion de la clase View_Inicial
class View_Inicial(QMainWindow):
    
    ## Propiedades de la clase
    PathFile_ViewInicial = r"app\views\UI\View_Inicio.ui"
    PathFile_ViewIcon = r"app\views\UI\resources\cyber-criminal.png"

    Sig_Btn_Clicked_Cifrar = pyqtSignal()
    Sig_Btn_Clicked_Descifrar = pyqtSignal()
    Sig_Btn_Clicked_Inicio = pyqtSignal() 

    ## Constructor de la clase
    def __init__(self): 
               
        super().__init__() ##Asignacion de memoria
        uic.loadUi(self.PathFile_ViewInicial, self) #Lectura de la interfaz grafica
        self.setWindowIcon(QIcon(self.PathFile_ViewIcon))   ##Seleccion de icono de la ventana

        ##Creacion de las instanciasde los elemntos graficos a interactuar
        self.Btn_Cifrar = self.findChild(QPushButton, "Button_Encriptar")
        self.Btn_Descifrar = self.findChild(QPushButton, "Button_Decepcriptar")
        self.Btn_Inicio = self.findChild(QPushButton, "Button_Inicio")

        ##Asignacion de los eventos generados por el usuario a los metodos de la clase
        self.Btn_Cifrar.clicked.connect(self._Enviar_Btn_Cifrar)
        self.Btn_Descifrar.clicked.connect(self._Enviar_Btn_Descifrar)
        self.Btn_Inicio.clicked.connect(self._Enviar_Btn_Inicio)

    ## Metodos de la clase
    def _Enviar_Btn_Cifrar(self):

        self.Sig_Btn_Clicked_Cifrar.emit()

    def _Enviar_Btn_Descifrar(self):

        self.Sig_Btn_Clicked_Descifrar.emit()
    
    def _Enviar_Btn_Inicio(self):
        self.Sig_Btn_Clicked_Inicio.emit()

    