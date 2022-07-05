# Método de elinamação de Gauss com a possibilidade de usar a estrátegia de pivoteamento parcial.  

# para executar no google colab:
# https://colab.research.google.com/drive/1XeohkEDDNpjxk43_nvSEDG3iUV6IHQBS?usp=sharing

from fractions import Fraction

class EliminacaoDeGauss:
    def __init__(self, matriz):
        self.matriz = matriz
        self.tam = len(self.matriz)

    def mostrarMatriz(self):
        espacos = self.qtdEspaco()
        
        for linha in self.matriz:
            print("|", end=" ")
            for j, coeficiente in enumerate(linha):
                if j == self.tam: print("'", end=" ")
                print(coeficiente, " " * (espacos[j] - len(str(coeficiente))), end=" ")
            print("|") 
        print() 

    def qtdEspaco(self):
        espacos = [0]*(self.tam+1)
        k = 0
        for i in range(self.tam+1):
            for j in range(self.tam):         
                if len(str(self.matriz[j][i])) > espacos[k]: espacos[k] = len(str(self.matriz[j][i]))
            k+=1
        return espacos

    def transformarEmFracao(self):
        fracao = lambda x:[Fraction(item) for item in x]
        self.matriz = list(map(fracao, self.matriz))
    
    def pivoteamentoParcial(self, coluna):
        maior = 0
        posicao = None
        for i in range(coluna, self.tam):
            if abs(maior) < abs(self.matriz[i][coluna]):
                posicao = i
                maior = self.matriz[i][coluna]
        if self.matriz[coluna] != self.matriz[posicao]:
            self.matriz[coluna], self.matriz[posicao] = self.matriz[posicao], self.matriz[coluna]
            print(f'Trocar a posição da linha "{posicao+1}" pela linha "{coluna+1}."\n')
            self.mostrarMatriz()
            
    def eliminacao(self, pivoteamentoParcial):
        print("Matriz estendida:\n")
        self.mostrarMatriz()

        print("Transformação para matriz triângular superior:\n")
        for k in range(self.tam-1):
            if pivoteamentoParcial: self.pivoteamentoParcial(k)
            for i in range(k+1,self.tam):
                m = self.matriz[i][k]/self.matriz[k][k]
                print(f"M({i+1},{k+1}) = {m}")
                for j in range(self.tam+1):
                    self.matriz[i][j] = self.matriz[i][j]- m*self.matriz[k][j]

            print()
            self.mostrarMatriz()

    def resolucaoDoSistema(self):
        x = [0]*self.tam

        for i in reversed(range(self.tam)):
            s = 0
            for j in range(i+1, self.tam):
                s += self.matriz[i][j]*x[j]
            x[i] = (self.matriz[i][-1] - s)/self.matriz[i][i]

        print("Resposta:")

        for i, a in enumerate(x):
            print(f"X{i+1} = {a}")

    def eliminacaoDeGauss(self, fracao=True, pivoteamentoParcial = False):
        if fracao == True: self.transformarEmFracao()
        self.eliminacao(pivoteamentoParcial)
        self.resolucaoDoSistema()
            

matriz =[ [2,2,1,1,7],
    [1,-1,2,-1,1],
    [3,2,-3,-2,4],
    [4,3,2,1,12]]

sistema = EliminacaoDeGauss(matriz)

sistema.eliminacaoDeGauss(pivoteamentoParcial=True)