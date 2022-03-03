# versão 01

def binario(numero):
    decimal = int(numero[0])
    for digito in range(1, len(numero)):
        decimal = int(numero[digito]) + 2 * decimal
    return decimal


numero = '1010'

print(binario(numero))
