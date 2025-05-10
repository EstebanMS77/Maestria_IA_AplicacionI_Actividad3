from controllers.View_Inicial import View_Inicial
from controllers.View_Warning import View_Warning
import sys
from PyQt6.QtWidgets import QApplication



if __name__ == "__main__":
    
    try:
        app  = QApplication(sys.argv)
        View_Inicial = View_Inicial()
        View_Inicial.Run_Screen(app)
    except Exception as e:
        QApplication.closeAllWindows()
        app = QApplication(sys.argv)
        View_Warning = View_Warning()
        View_Warning.Run_Screen(app,type(e),e.args)
        QApplication.quit()
        