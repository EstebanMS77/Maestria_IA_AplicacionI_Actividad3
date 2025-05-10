from views.View_Inicial import View_Inicial
from views.View_Cifrado import View_Cifrado
from views.View_Warning import View_Warning
from views.View_Descifrado import View_Descifrado

class Controler_App():

    def __init__(self):

        self.Screen_View_Inicial = View_Inicial()
        self.Screen_View_Cifrado = View_Cifrado()
        self.Screen_View_Descifrado = View_Descifrado()
        self.Screen_View_Warning = View_Warning()

        self.Screen_View_Inicial.Btn_Clicked.connect(self._Navigate_ScreenCifrado)

        self._Run_ScreenInicial()


    def _Run_ScreenInicial(self):
        
        self.Screen_View_Inicial.show()

    def _Navigate_ScreenDescifrado(self):
        try:    
            self._Close_Screen()
            self.Screen_View_Descifrado.show()

        except Exception as e:

            self.Show_Warning(Str_Error="Se ha presentado un error en el aplicativo, de tipo:\n"+ str(type(e))+ "\n Mensaje:" +str(e.args))

    def _Navigate_ScreenCifrado(self):

        try:    
            self._Close_Screen()
            self.Screen_View_Cifrado.show()

        except Exception as e:

            self.Show_Warning(Str_Error="Se ha presentado un error en el aplicativo, de tipo:\n"+ str(type(e))+ "\n Mensaje:" +str(e.args))

    def Show_Warning(self,Str_Error):

        self._Close_Screen()
        self.Screen_View_Warning.Write_Error(Str_Error)
        self.Screen_View_Warning.show()


    def _Close_Screen(self):

        self.Screen_View_Cifrado.close()
        self.Screen_View_Descifrado.close() 
        self.Screen_View_Inicial.close()
        self.Screen_View_Warning.close()
    

