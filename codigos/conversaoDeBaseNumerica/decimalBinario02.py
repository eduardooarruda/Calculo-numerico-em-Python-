# Decimal para Binário versão 02

def decimalBinario(numero):
    if numero < 2:
        print(numero, end='')
        return
    decimalBinario(numero//2)
    print(numero % 2, end='')


decimalBinario(10)
