## Librerias requeridas para la vista inicial
import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from views.UI import resources

##Definicion de la clase View_Inicial
class View_Warning(QMainWindow):
    
#   #Propiedades de la clase
    PathFile_ViewWarning = r"app\views\UI\View_Warning.ui"
    PathFile_ViewIcon = r"app\views\UI\resources\cyber-criminal.png"

    ## Constructor de la clase
    def __init__(self):  

        super().__init__()
        uic.loadUi(self.PathFile_ViewWarning, self)
        self.setWindowIcon(QIcon(self.PathFile_ViewIcon))
        self.Label_Error = self.findChild(QLabel,"Label_Error")

    def Write_Error(self,Str_Error):      
        
        self.Label_Error.setText(Str_Error)

        
