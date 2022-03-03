# Decimal para binário versão 01

def decimalBinario(numero):
    binario = ""
    while numero >= 2:
        binario = f"{numero%2}{binario}"
        numero = numero//2
    binario = f"{numero}{binario}"
    print(binario)


decimalBinario(10)
