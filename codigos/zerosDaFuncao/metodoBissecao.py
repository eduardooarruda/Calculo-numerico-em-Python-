# coding: latin-1

# para executar no google colab:
# https://colab.research.google.com/drive/1rWLHIr5kqqI9BKYDBZHXXOlrkIIpR4OC?usp=sharing

from math import sqrt, log

class Bissecao:
    def __init__(self,a,b, precisao, numDigitos, dominioZero = True):
        # a e b são os intervalos iniciais 
        self.a = a #  início do intervalo
        self.b = b # fim do intervalo
        self.precisao = precisao 
        self.numDigitos = numDigitos - 1 
        self.dominioZero = dominioZero

    def funcao(self, x):
        return x**3-9*x+3
    
    def acharIntervalos(self):
        primeiro = True
        x = self.a
        x2 = None
        Fx2 = None
        raizes = []
        while x <= self.b:
            if not self.dominioZero and x == 0:
                x += 1
                continue
            
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
            print("Não foi possível encontrar raízes!")
        elif len(raizes) == 1:
            print("Foi encontrado 1 raiz")
        else:
            print(f"Foram encontradas {len(raizes)} raízes.\n\n")

        for raiz in raizes:
            a = round(raiz[0], self.numDigitos)
            b = round(raiz[1], self.numDigitos)
            qtdEspacos = self.numDigitos * 2
            iteracao = 1
            n =  qtdEspacos + 1

            print("Iteração" + "  "  + "a" + " " * n + "b" + " "  * n + "m" + " " * n + "b-a" + " " * ( 23 - self.qtdCaracteres(b-a)) + "f(a)"  + "   "  + "f(m)" + "   " + "f(b)")
            
            while b-a > self.precisao:
                m = round((a+b)/2, self.numDigitos)
                Fm = self.funcao(m)
                Fa = self.funcao(a)
                Fb = self.funcao(b)

                aSinal = "+" if Fa > 0 else "-"
                mSinal = "+" if Fm > 0 else "-"
                bSinal = "+" if Fb > 0 else "-" 

                print(str(iteracao) + " " * (10 - self.qtdCaracteres(iteracao)) + str(a) + " " * ( qtdEspacos - self.qtdCaracteres(a) + 2) + str(b) + " " *  ( qtdEspacos - self.qtdCaracteres(b) + 2) + str(m) + " " *  ( qtdEspacos - self.qtdCaracteres(m) + 2) + str(b-a) + " " *  ( 25 - self.qtdCaracteres(b-a) ) + str(aSinal)  + " " * 6   + str(mSinal)  + " " * 6  + str(bSinal))
               
                if Fm * Fa < 0:
                    b = m                                                                 
                elif Fm * Fb < 0:
                    a = m
                if iteracao > 50:
                    print("Limite máximo de iterações foi atingido!")
                    break
                

                iteracao += 1
        
            print(str(iteracao) + " " * (10 - self.qtdCaracteres(iteracao)) + str(a) + " " * ( qtdEspacos - self.qtdCaracteres(a) + 2) + str(b) + " " *  ( qtdEspacos - self.qtdCaracteres(b) + 2) + str(round((a+b)/2, self.numDigitos)) + " " *  ( qtdEspacos - self.qtdCaracteres(round((a+b)/2, self.numDigitos)) + 2) + str(b-a) + " " *  ( 25 - self.qtdCaracteres(b-a)) + str(aSinal)  + " " * 6   + str(mSinal)  + " " * 6  + str(bSinal) )
            
            print("\n\n")

    def qtdCaracteres(self,num):
        num = str(num)
        return len(num)


x = Bissecao(-5,5, 10**-3, 10, False)

#print(x.acharIntervalos())

x.metodoBissecao()