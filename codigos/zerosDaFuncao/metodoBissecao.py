# coding: latin-1

# para executar no google colab:
# https://colab.research.google.com/drive/1rWLHIr5kqqI9BKYDBZHXXOlrkIIpR4OC?usp=sharing

from math import sqrt, log, e, sin, cos

class Bissecao:
    def __init__(self,a,b, precisao, numCasasDecimais):
        # a e b são os intervalos iniciais 
        self.a = a #  início do intervalo
        self.b = b # fim do intervalo
        self.precisao = precisao 
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

    def metodoBissecao(self):
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
 
            iteracao = 1
          
            print("Iteração" , " " * self.qtdEspacos("iteracao") , "a" , " " * self.qtdEspacos("a") ,
                  "b" , " "  * self.qtdEspacos("b") , "m" , " " * self.qtdEspacos("m") , "b-a" , " " * (27) , 
                  "f(a)"  , "   "  , "f(m)" , "   " , "f(b)", sep="")
            
            while b-a > self.precisao:
                m = round((a+b)/2, self.numCasasDecimais)
                Fm = self.funcao(m)
                Fa = self.funcao(a)
                Fb = self.funcao(b)

                aSinal = "+" if Fa > 0 else "-"
                mSinal = "+" if Fm > 0 else "-"
                bSinal = "+" if Fb > 0 else "-" 

                print(str(iteracao) , " " * self.qtdEspacos(iteracao) , str(a) , " " * self.qtdEspacos(a) , str(b) , 
                      " " *  self.qtdEspacos(b) , str(m) , " " *  self.qtdEspacos(m) , str(b-a) , 
                      " " * (30 - self.qtdCaracteres(b-a)) , str(aSinal)  , " " * 6 , str(mSinal)  , " " * 6  , str(bSinal), 
                      sep='')
               
                if Fm * Fa < 0:
                    b = m                                                                 
                elif Fm * Fb < 0:
                    a = m
                if iteracao > 50:
                    print("Limite máximo de iterações foi atingido!")
                    break
                

                iteracao += 1
        
            print(str(iteracao) , " " * self.qtdEspacos(iteracao) , str(a) , " " * self.qtdEspacos(a) , str(b) ,
                  " " *  self.qtdEspacos(b) , str(m) , " " *  self.qtdEspacos(m) , str(b-a) , 
                  " " * (30 - self.qtdCaracteres(b-a)) , str(aSinal)  , " " * 6   , str(mSinal)  , " " * 6  , str(bSinal), sep="")
            
            print("\n\n")

    def qtdCaracteres(self,num):
        num = str(num)
        return len(num)

    def qtdEspacos(self, num):
        num = str(num)
        return  self.numCasasDecimais * 2 + 9 - len(num)  

   

x = Bissecao(-5,5, 10**-5, 8)


x.metodoBissecao()


