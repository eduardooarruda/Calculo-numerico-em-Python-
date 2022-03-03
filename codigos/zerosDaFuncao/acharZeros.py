# coding: latin-1

# Achar zeros de uma função com um algoritmo mais simples, porém menos eficiente:

#início do intervalo: -5
x = -5

xAux = None
fAux = None

primeiro = True

#fim do intervalo: 5
while x <= 5:
    
    f = x**3-9*x+3
     
    if not primeiro:
        if (fAux<0 and f >=0) or (fAux >=0 and f <0):
            print(f"intervalo: ({xAux} , {x})")
            print(f'Ponto médio: {(xAux+x)/2}\n')
        
    fAux = f
    xAux = x
    primeiro = False
   
    x += 0.00001