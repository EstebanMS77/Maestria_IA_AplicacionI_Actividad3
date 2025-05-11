## Librerias requeridas para el modelo
from views.View_Inicial import View_Inicial
from views.View_Cifrado import View_Cifrado
from views.View_Warning import View_Warning
from views.View_Descifrado import View_Descifrado
from models.Model import Model

class Controler_App():

    ##Constructor de la clase
    def __init__(self):

        ## Creacion de los objetos de la vista y el modelo
        self.Screen_View_Inicial = View_Inicial()
        self.Screen_View_Cifrado = View_Cifrado()
        self.Screen_View_Descifrado = View_Descifrado()
        self.Screen_View_Warning = View_Warning()
        self.Model = Model(0)

        ## Asignacion de las señales a las vistas a los metodos de la clase
        self.Screen_View_Inicial.Sig_Btn_Clicked_Cifrar.connect(self._Navigate_ScreenCifrado)
        self.Screen_View_Inicial.Sig_Btn_Clicked_Descifrar.connect(self._Navigate_ScreenDescifrado)
        self.Screen_View_Inicial.Sig_Btn_Clicked_Inicio.connect(self._Navigate_ScreenInicio)
        self.Screen_View_Warning.Sig_Btn_Clicked_Inicio.connect(self._Navigate_ScreenInicio)

        self.Screen_View_Cifrado.Sig_Btn_Clicked_Inicio.connect(self._Navigate_ScreenInicio)
        self.Screen_View_Cifrado.Sig_TextInputText_Codigo.connect(self._Send_Cifrado)

        self.Screen_View_Descifrado.Sig_TextInputText_Codigo.connect(self._Send_Descifrado)        
        self.Screen_View_Descifrado.Sig_Btn_Clicked_Inicio.connect(self._Navigate_ScreenInicio)

        self._Navigate_ScreenInicio()


##    ## Metodos de la clase

    def _Navigate_ScreenInicio(self):
                 
        try:

            self._Close_Screen()
            self.Screen_View_Inicial.show()
        except Exception as e:

            self.Show_Warning(Str_Error="Se ha presentado un error en el aplicativo, de tipo:\n"+ str(type(e))+ "\n Mensaje:" +str(e.args)) 

    def _Navigate_ScreenDescifrado(self):
        try:    

            self._Close_Screen()
            self.Screen_View_Descifrado.Eliminar_Texto()
            self.Screen_View_Descifrado.show()

        except Exception as e:

            self.Show_Warning(Str_Error="Se ha presentado un error en el aplicativo, de tipo:\n"+ str(type(e))+ "\n Mensaje:" +str(e.args))

    def _Navigate_ScreenCifrado(self):

        try:

            self._Close_Screen()
            self.Screen_View_Cifrado.Eliminar_Texto()
            self.Screen_View_Cifrado.show()

        except Exception as e:

            self.Show_Warning(Str_Error="Se ha presentado un error en el aplicativo, de tipo:\n"+ str(type(e))+ "\n Mensaje:" +str(e.args))

    def Show_Warning(self,Str_Error):

        try:

            self._Close_Screen()
            self.Screen_View_Warning.Write_Error(Str_Error)
            self.Screen_View_Warning.show()

        except Exception as e:

            self.Show_Warning(Str_Error="Se ha presentado un error en el aplicativo, de tipo:\n"+ str(type(e))+ "\n Mensaje:" +str(e.args))


    def _Close_Screen(self):

        try:

            self.Screen_View_Cifrado.close()
            self.Screen_View_Descifrado.close() 
            self.Screen_View_Inicial.close()
            self.Screen_View_Warning.close()

        except Exception as e:  

            self.Show_Warning(Str_Error="Se ha presentado un error en el aplicativo, de tipo:\n"+ str(type(e))+ "\n Mensaje:" +str(e.args))
    
    def _Send_Cifrado(self):
        try:
            Num_Cifrado = self.Screen_View_Cifrado.InputText_Codigo.text()
            if Num_Cifrado != "" and len(str(Num_Cifrado)) == 6:
                self.Model._Calcular_Cifrado(Num_Cifrado)
                self.Screen_View_Cifrado._Recibir_Cifrado(str(self.Model.Int_Cifrado))
                        
        except Exception as e:

            self.Show_Warning(Str_Error="Se ha presentado un error en el aplicativo, de tipo:\n"+ str(type(e))+ "\n Mensaje:" +str(e.args))

    def _Send_Descifrado(self):
        try:
            Num_Cifrado = self.Screen_View_Descifrado.InputText_Codigo.text()
            if Num_Cifrado != "" and len(str(Num_Cifrado)) == 6:
                self.Model._Calcular_Descifrado(Num_Cifrado)
                self.Screen_View_Descifrado._Recibir_descifrado(str(self.Model.Int_Cifrado))
                        
        except Exception as e:

            self.Show_Warning(Str_Error="Se ha presentado un error en el aplicativo, de tipo:\n"+ str(type(e))+ "\n Mensaje:" +str(e.args))
