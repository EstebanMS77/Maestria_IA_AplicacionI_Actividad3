import math
import os


class Model():

    Int_Cifrado = 0
    Digitos_Cifrado = []

    def __init__(self,Num_Cifrado):
        self.Int_Cifrado = Num_Cifrado
        self.Digitos_Cifrado = []


    def _Calcular_Cifrado(self,Num_Cifrado):

        try:
            if len(str(Num_Cifrado)) == 6:
                Codigo = Num_Cifrado
                self.Digitos_Cifrado = []
                for Num in str(Codigo):
                    self.Digitos_Cifrado.append((int(Num)+7)%10)
                
                self.Digitos_Cifrado = [
                    self.Digitos_Cifrado[2],
                    self.Digitos_Cifrado[3],
                    self.Digitos_Cifrado[0],
                    self.Digitos_Cifrado[1],
                    self.Digitos_Cifrado[5],
                    self.Digitos_Cifrado[4]
                ]

                self.Int_Cifrado = str(''.join(map(str, self.Digitos_Cifrado)))

            else:
                self.Int_Cifrado = 0

        except Exception as e:

            self.Int_Cifrado = 0

    def _Calcular_Descifrado(self,Num_Cifrado):

        try:
            if len(str(Num_Cifrado)) == 6:
                Codigo = Num_Cifrado
                self.Digitos_Cifrado = []
                for Num in str(Codigo):
                    self.Digitos_Cifrado.append((int(Num)-7)%10)
                
                self.Digitos_Cifrado = [
                    self.Digitos_Cifrado[2],
                    self.Digitos_Cifrado[3],
                    self.Digitos_Cifrado[0],
                    self.Digitos_Cifrado[1],
                    self.Digitos_Cifrado[5],
                    self.Digitos_Cifrado[4]
                ]

                self.Int_Cifrado = str(''.join(map(str, self.Digitos_Cifrado)))

            else:
                self.Int_Cifrado = 0

        except Exception as e:

            self.Int_Cifrado = 0





