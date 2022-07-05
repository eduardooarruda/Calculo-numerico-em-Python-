# Para executar no google colab:
# https://colab.research.google.com/drive/1lrKu2v2PgmE7h3z2lzndazr7e9R0LHzV?usp=sharing

# Equações Polinomiais

class PolinomiosNewton:
    def __init__(self, coeficientes, x0, precisao):
        self.coeficientes = coeficientes
        self.x = x0
        self.precisao = precisao
        self.b =[]
    
    def funcao(self, x, mostrar=True):
       
        b = 0 
        i = len(self.coeficientes) - 1
        primeiro = True

        if mostrar:
            print("Funcão:")
             
        for termo in self.coeficientes:
            if termo != '':
                a = termo
                
                if primeiro:
                    b = a
                    self.b.append(b)
                    primeiro = False
                    continue

                if mostrar: 
                    print(f'b{i} = {b}')

                b = a + b*x
                self.b.append(b)
                i -= 1
        if mostrar:    
            print(f'b{i} = {b}')
        else:
            self.b = []
        return b

    def derivada(self, x):
        c = 0
        i = len(self.b) - 1
        primeiro = True
        print("\nDerivada:")
        del(self.b[len(self.b)-1])
        
        if primeiro:
            c = self.b[0]
            print(f"c{i} = {self.b[0]}")

            primeiro = False
            del(self.b[0])

        for b in self.b:
            
            c = b + c * x
            i -= 1
            print(f"c{i} = {c}")
            
        self.b =[]
              
        return c
    
    def metodoNewton(self):
       i = 1
       x = self.x
      
       fx = self.funcao(x, False)
       while abs(fx) > self.precisao:
           print(f"ITERAÇÂO {i}: \n")
           x = x - self.funcao(x) / self.derivada(x)
           print(f"\nx{i} = {x}\n\n")
           fx = self.funcao(x, False)
           
           if i == 50:
               print("O Limite de iterações foi atingido!")
               break
           i += 1

       print(f"RESPOSTA: x = {x}\n ")
      

coeficientes = [1,0,-3,3]
precisao = 10**-6
x0 = -2

x = PolinomiosNewton(coeficientes, x0, precisao)
x.metodoNewton()