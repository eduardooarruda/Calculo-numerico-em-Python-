# Conversor de bases 1 até 16 para decimal

def binario(numero,  base):
    base_hex = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    try:
        decimal = int(numero[0])
    except ValueError:
        digito = numero[0].upper()
        decimal = base_hex[digito]
    for d in range(1, len(numero)):
        try:
            decimal = int(numero[d]) + base*decimal
        except ValueError:
            d = numero[d].upper()
            digito = base_hex[d]
            decimal = digito + base*decimal
    return decimal


numero = "abcdE"

print(binario(numero, 16))
