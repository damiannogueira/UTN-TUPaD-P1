# EJERCICIO 10
# Le pido al usuario que ingrese un número, pero lo guardo como una cadena
numero = (input("Ingresa un número y yo te invierto los dígitos: "))

if numero.startswith("-"): # Si el número es negativo
    # Uso función Slicing
    invertido = "-" + numero[:0:-1]  # Invertimos sin el signo y lo concatenamos al inicio
else:
    # Uso función Slicing
    invertido = numero[::-1] # Si es positivo sólo invertimos.

print(f"El número invertido es: {invertido}")