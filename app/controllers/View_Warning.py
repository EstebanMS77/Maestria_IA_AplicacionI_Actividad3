## Librerias requeridas para la vista inicial
import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from views.UI import resources

##Definicion de la clase View_Inicial
class View_Warning(QMainWindow):
    
    ## Constructor de la clase
    def __init__(self):        
        super().__init__()
        uic.loadUi(r"app\views\UI\View_Warning.ui", self)
        
    def Run_Screen(self,app,Type,Args):
        Screen = View_Warning()
        Screen.setWindowIcon(QIcon(r"app\views\UI\resources\cyber-criminal.png"))        
        Label_Error = Screen.findChild(QLabel,"Label_Error")
        Str_Content = "Se ha presentado el siguiente error: \n "+str(Type) + "\n" + str(Args)
        Label_Error.setText(Str_Content)
        Screen.show()
        sys.exit(app.exec())
