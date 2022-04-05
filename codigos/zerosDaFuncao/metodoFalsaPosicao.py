# coding: latin-1

# Para executar no google colab:
# https://colab.research.google.com/drive/1vComb-uCUF9GKtG-QTH4USdNJT5qbbfR?usp=sharing

from math import sqrt, log, e, sin

class metodoFalsaPosicao:
    def __init__(self,a,b, precisao, numCasasDecimais):
        # a e b são os intervalos iniciais 
        self.a = a #  início do intervalo
        self.b = b # fim do intervalo
        self.precisao_1 = precisao
        self.precisao_2 = precisao  
        self.numCasasDecimais = numCasasDecimais 


    def funcao(self, x):
        return x**3-9*x+3
    
    def acharIntervalos(self):
        primeiro = True
        x = self.a
        x2 = None
        Fx2 = None
        raizes = []
        while x <= self.b:
            
            Fx = self.funcao(x)
                
            if not primeiro:
                if (Fx2 < 0 and Fx >= 0) or (Fx2 >= 0 and Fx < 0):
                    raizes.append([x2, x])

            Fx2 = Fx
            x2 = x
            primeiro = False
            x +=  1

        return raizes

    def MFP(self):
        raizes = self.acharIntervalos()

        if not raizes:
            print("Não foi possível encontrar raízes!\n\n")
        elif len(raizes) == 1:
            print("Foi encontrado 1 raiz\n\n")
        else:
            print(f"Foram encontradas {len(raizes)} raízes.\n\n")

        for raiz in raizes:
            a = round(raiz[0], self.numCasasDecimais)
            b = round(raiz[1], self.numCasasDecimais)
            qtdEspacos = self.numCasasDecimais * 2
            iteracao = 1
            n =  qtdEspacos + 1

            print("Iteração" , " " * self.qtdEspacos("Iteração") , "a" , " " * self.qtdEspacos("a") , "b" , 
                  " "  * self.qtdEspacos("b") , "x" , " " * self.qtdEspacos("x") , "b-a" , " " * (27) ,
                  "|f(x)|" , " " * (22) , "f(a)"  , "   "  , "f(m)" , "   " , "f(b)", sep="")
            
            while b-a > self.precisao_1:
                x0 = round((a*self.funcao(b)- b*self.funcao(a))/(self.funcao(b)-self.funcao(a)), self.numCasasDecimais)
                
                Fx0 = self.funcao(x0)
    
                if abs(Fx0) < self.precisao_2:
                    break

                Fa = self.funcao(a)
                Fb = self.funcao(b)

                aSinal = "+" if Fa > 0 else "-"
                mSinal = "+" if Fx0 > 0 else "-"
                bSinal = "+" if Fb > 0 else "-" 

                print(str(iteracao) , " " * self.qtdEspacos(iteracao) , str(a) , " " * self.qtdEspacos(a) , str(b) ,
                      " " *  self.qtdEspacos(b) , str(x0) , " " *  self.qtdEspacos(x0) , str(b-a) , 
                      " " * (30 - self.qtdCaracteres(b-a)) , str(abs(Fx0)) , " " *  (30 - self.qtdCaracteres(Fx0)) ,
                      str(aSinal)  , " " * 6   , str(mSinal)  , " " * 6  , str(bSinal), sep="")
            
                if Fx0 * Fa < 0:
                    b = x0                                                                 
                elif Fx0 * Fb < 0:
                    a = x0
                if iteracao > 50:
                    print("Limite máximo de iterações foi atingido!")
                    break
                

                iteracao += 1
        
            print(str(iteracao) , " " * self.qtdEspacos(iteracao) , str(a) , " " * self.qtdEspacos(a) , str(b) ,
                  " " *  self.qtdEspacos(b) , str(x0) , " " *  self.qtdEspacos(x0) , str(b-a) , 
                  " " * (30 - self.qtdCaracteres(b-a))  , str(abs(Fx0) ) , " " * (30 - self.qtdCaracteres(Fx0)) ,
                  str(aSinal)  , " " * 6   , str(mSinal)  , " " * 6  , str(bSinal), sep="")
            
            print("\n\n")

    def qtdCaracteres(self,num):
        num = str(num)
        return len(num)

    def qtdEspacos(self, num):
        num = str(num)
        return self.numCasasDecimais * 2 - len(num) + 8


x = metodoFalsaPosicao(-5,5,10**-5, 8)

#print(x.acharIntervalos())

x.MFP()