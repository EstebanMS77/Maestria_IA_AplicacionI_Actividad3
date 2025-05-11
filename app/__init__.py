##Librerias requeridas para la aplicacion
from controllers.controler import Controler_App
from PyQt6.QtWidgets import QApplication
import sys


## Definicion de la funcion principal
if __name__ == "__main__":
    
    try:
        App  = QApplication(sys.argv)
        Obj_Controler_App = Controler_App() 
        sys.exit(App.exec()) 

    except Exception as e:
        print("Se ha presentado un error en el aplicativo, de tipo:\n"+ str(type(e))+ "\n Mensaje:" +str(e.args))
        sys.exit()
