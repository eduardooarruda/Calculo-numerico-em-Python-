# coding: latin-1

# para executar no google colab:
# https://colab.research.google.com/drive/15enJF806kdYX-twTuJItWtK9k5WquHss?usp=sharing

from math import log, sqrt, e, sin, cos

class MetodoNewton:
    def __init__(self, X0, numCasasDecimais, precisao_1, precisao_2=None):
        self.X0 = X0
        self.precisao_1 = precisao_1
        self.precisao_2 = precisao_2 if precisao_2 != None else precisao_1
        self.numCasasDecimais = numCasasDecimais

    def funcao(self,x):
        return x**3-9*x+3

    #Derivada da função
    def funcaoAux(self,x):
        return  3*x**2-9 

    def metodoNewton(self):
        primeiro = True
        Xn = round(self.X0, self.numCasasDecimais)
        Xn2 = None
        iteracao = 0

        print("Iteração  " , " " * (self.qtdEspacos("Iteração")) , "Xn" , 
        " " * ((self.qtdEspacos("Xn"))) , 
              "|Xn - Xn-1|" , " " * (18) , "|f(Xn)|" , sep="")

        while abs(self.funcao(Xn)) > self.precisao_2:

            if primeiro:
                Xn2 = Xn
                Xn = round(Xn - self.funcao(Xn)/self.funcaoAux(Xn), self.numCasasDecimais)
                print(str(iteracao) , " " * self.qtdEspacos(iteracao)  , str(Xn2) , " " * self.qtdEspacos(Xn2) , 
                      "-----------" , " " * (19) , str(abs(self.funcao(Xn2))), sep="")
                iteracao += 1
                primeiro = False
                continue
            
            if abs(Xn - Xn2) < self.precisao_1:
                break
            
            if iteracao == 50:
                print("O limite de iterações foi atingido!")
                break

            print(str(iteracao) , " " * self.qtdEspacos(iteracao)  , str(Xn) , " " * self.qtdEspacos(Xn) , str(abs(Xn-Xn2)) ,
                  " " * (30 - self.qtdCaracteres(abs(Xn-Xn2))) , str(abs(self.funcao(Xn))), sep="")
            Xn2 = Xn
            Xn = round(Xn - self.funcao(Xn)/self.funcaoAux(Xn), self.numCasasDecimais)
            iteracao += 1

        print(str(iteracao) , " " * self.qtdEspacos(iteracao)  , str(Xn) , " " * self.qtdEspacos(Xn) , str(abs(Xn-Xn2)) , 
              " " * (30 - self.qtdCaracteres(abs(Xn-Xn2))) , str(abs(self.funcao(Xn))), sep="")

    def qtdCaracteres(self,num):
        num = str(num)
        return len(num)

    def qtdEspacos(self, num):
        num = str(num)
        return self.numCasasDecimais * 2 - len(num) + 6


x = MetodoNewton(1.5, 8, 10**-3)

x.metodoNewton()
