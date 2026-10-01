"""
Convertir a binario
"""

# Entradas
numero = int(input("Introduzca un número: "))

# Proceso
dividendo = numero
binario = ""
while dividendo > 0:
    residuo = dividendo % 2
    dividendo //= 2
    binario = str(residuo) + binario

# Completar a múltiplo de ocho dígitos
if len(binario) % 8 != 0:
    binario = "0" * (8 - len(binario) % 8) + binario

# Salidas
print(numero, binario)
