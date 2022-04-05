# coding: latin-1

# para executar no google colab:
# https://colab.research.google.com/drive/1aEJctvuwbCDZs2YTFtXa-27FHQ3hzwdr?usp=sharing

from math import e, sin, log, sqrt

class MetodoSecante:
    def __init__(self, X0, X1, numCasasDecimais, precisao_1, precisao_2=None):
        self.X0 = X0
        self.X1 = X1
        self.precisao_1 = precisao_1
        self.precisao_2 = precisao_2 if precisao_2 != None else precisao_1
        self.numCasasDecimais = numCasasDecimais

    def funcao(self,x):
        return 4*sin(x)-e**x

    def funcaoMetodo(self,Xn, Xn2):
        return (Xn * self.funcao(Xn2) - Xn2 * self.funcao(Xn)) / (self.funcao(Xn2) - self.funcao(Xn))

    def metodoSecante(self):
        primeiro = True
        Xn = round(self.X0, self.numCasasDecimais)
        Xn2 = round(self.X1, self.numCasasDecimais)
        iteracao = 1

        print("Iteração" , " " * (self.qtdEspacos("Iteração")) , "Xn" , " " * ((self.qtdEspacos("Xn"))) ,
              "|Xn - Xn-1|" , " " * (18) , "|f(Xn)|", sep="")

        while abs(self.funcao(Xn)) > self.precisao_2:

            if primeiro:
                Xn = round(self.funcaoMetodo(Xn,Xn2), self.numCasasDecimais)
                primeiro = False
                continue

            if abs(Xn - Xn2) < self.precisao_1:
                break
            
            if iteracao == 50:
                print("O limite de iterações foi atingido!")
                break

            
            print(str(iteracao) , " " * self.qtdEspacos(iteracao)  , str(Xn) , " " * self.qtdEspacos(Xn) ,
                  str(abs(Xn-Xn2)) , " " * (30 - self.qtdCaracteres(abs(Xn-Xn2))) , str(abs(self.funcao(Xn))), sep="")
            xAux = Xn
            Xn = round(self.funcaoMetodo(Xn,Xn2), self.numCasasDecimais)
            Xn2 = xAux
            iteracao += 1

        print(str(iteracao) , " " * self.qtdEspacos(iteracao)  , str(Xn) , " " * self.qtdEspacos(Xn) , str(abs(Xn-Xn2)) ,
              " " * (30 - self.qtdCaracteres(abs(Xn-Xn2))) , str(abs(self.funcao(Xn))), sep="")

    def qtdCaracteres(self,num):
        num = str(num)
        return len(num)

    def qtdEspacos(self, num):
        num = str(num)
        return self.numCasasDecimais * 2 - len(num) + 5


x = MetodoSecante(0,1, 9, 10**-5)

x.metodoSecante()