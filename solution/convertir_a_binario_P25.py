"""
Convertir un número decimal (base 10) a binario.
"""

# Entradas
numero = int(input("Introduzca el número a convertir: "))

# Proceso
cociente = numero
if numero == 0:
    binario = "0"
else:
    binario = ""
    # Hacer divisiones sucesivas hasta que el cociente de 0
    while cociente > 0:
        residuo = cociente % 2
        cociente = cociente // 2
        # Agregar el nuevo residuo a los anteriores (pero "al revés")
        binario = str(residuo) + binario 

# Salidas
print(f"El número en binario es {binario}.")
